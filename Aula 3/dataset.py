from pathlib import Path
import hashlib
import json


# ============================================================
# CONFIGURAÇÃO DO DATASET
# ============================================================

DATASETS = [
    ("1M",   1_000_000),
    # ("10M",  10_000_000),
    # ("100M", 100_000_000),
]

OUTPUT_DIR = Path("datasets")

# Não é uma "seed aleatória".
# É uma constante pertencente à especificação do dataset.
SEED = 0x5EED2026

# Quantidade de linhas acumuladas antes de escrever no disco.
# Isso reduz o número de operações de I/O sem exigir muita RAM.
CHUNK_LINES = 100_000

HEADER = b"numero\n"

ALGORITHM_VERSION = "AED2-DATASET-v1"


# ============================================================
# GERAÇÃO DETERMINÍSTICA DOS VALORES
# ============================================================

def value_at(index: int) -> int:
    """
    Retorna o valor numérico correspondente ao índice.

    Propriedades:
    - determinístico;
    - inteiro;
    - não decrescente;
    - permite valores repetidos.
    """

    return (
        1
        + index // 2
        + index // 5
        + index // 11
    )


# ============================================================
# PERMUTAÇÃO DETERMINÍSTICA
# ============================================================

def permute_power_of_two(x: int, mask: int) -> int:
    """
    Permutação bijetiva sobre um domínio de tamanho potência de 2.

    Todas as operações utilizadas são determinísticas.

    As multiplicações são feitas por constantes ímpares,
    o que mantém a operação invertível no domínio 2^k.
    """

    x = (x + (SEED & mask)) & mask

    x ^= x >> 7
    x &= mask

    x = (x * 0x9E3779B1) & mask

    x ^= x >> 11
    x &= mask

    x = (x * 0x85EBCA6B) & mask

    x ^= x >> 13
    x &= mask

    return x


def permute_index(index: int, n: int, mask: int) -> int:
    """
    Converte um índice [0, n) em outro índice [0, n).

    Utiliza cycle walking para garantir que o resultado
    pertença ao intervalo válido.

    Como a transformação é bijetiva, cada índice de
    [0, n) aparece exatamente uma vez.
    """

    x = index

    while True:
        x = permute_power_of_two(x, mask)

        if x < n:
            return x


# ============================================================
# UTILITÁRIOS DE ESCRITA
# ============================================================

def write_chunk(file, sha256, lines):
    """
    Escreve um bloco de linhas utilizando ASCII e LF explícito.

    Isso evita diferenças entre Windows, Linux e macOS.
    """

    data = "".join(lines).encode("ascii")

    file.write(data)
    sha256.update(data)


# ============================================================
# CSV ORDENADO
# ============================================================

def generate_ordered(path: Path, n: int):
    print(f"Gerando {path.name}...")

    sha256 = hashlib.sha256()

    with path.open("wb") as file:

        file.write(HEADER)
        sha256.update(HEADER)

        buffer = []

        for i in range(n):

            value = value_at(i)

            buffer.append(f"{value}\n")

            if len(buffer) >= CHUNK_LINES:
                write_chunk(file, sha256, buffer)
                buffer.clear()

        if buffer:
            write_chunk(file, sha256, buffer)

    return {
        "file": path.name,
        "rows": n,
        "ordered": True,
        "sha256": sha256.hexdigest(),
        "bytes": path.stat().st_size,
    }


# ============================================================
# CSV EMBARALHADO
# ============================================================

def generate_shuffled(path: Path, n: int):
    print(f"Gerando {path.name}...")

    sha256 = hashlib.sha256()

    # Menor potência de 2 capaz de representar n elementos.
    bits = (n - 1).bit_length()

    # Exemplo:
    #
    # bits = 20
    # domínio = 2^20
    # mask = 2^20 - 1

    mask = (1 << bits) - 1

    with path.open("wb") as file:

        file.write(HEADER)
        sha256.update(HEADER)

        buffer = []

        for i in range(n):

            shuffled_index = permute_index(
                i,
                n,
                mask
            )

            value = value_at(shuffled_index)

            buffer.append(f"{value}\n")

            if len(buffer) >= CHUNK_LINES:
                write_chunk(file, sha256, buffer)
                buffer.clear()

        if buffer:
            write_chunk(file, sha256, buffer)

    return {
        "file": path.name,
        "rows": n,
        "ordered": False,
        "sha256": sha256.hexdigest(),
        "bytes": path.stat().st_size,
    }


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    manifest = {
        "algorithm": ALGORITHM_VERSION,
        "seed": SEED,
        "files": []
    }

    # --------------------------------------------------------
    # FASE 1
    # Gera primeiro TODOS os datasets ordenados.
    # --------------------------------------------------------

    print()
    print("==========================================")
    print("FASE 1 - DATASETS ORDENADOS")
    print("==========================================")
    print()

    for label, size in DATASETS:

        path = OUTPUT_DIR / f"numeros_{label}_ordenado.csv"

        metadata = generate_ordered(
            path,
            size
        )

        manifest["files"].append(metadata)

    # --------------------------------------------------------
    # MANIFESTO
    # --------------------------------------------------------

    manifest_path = OUTPUT_DIR / "manifest.json"

    with manifest_path.open(
        "w",
        encoding="utf-8",
        newline="\n"
    ) as file:

        json.dump(
            manifest,
            file,
            indent=2,
            sort_keys=True
        )

        file.write("\n")

    # --------------------------------------------------------
    # RESULTADO
    # --------------------------------------------------------

    print()
    print("==========================================")
    print("GERAÇÃO CONCLUÍDA")
    print("==========================================")
    print()

    for item in manifest["files"]:

        print(item["file"])
        print(f"  registros: {item['rows']:,}")
        print(f"  SHA-256:   {item['sha256']}")
        print()

    print(f"Manifesto: {manifest_path}")


if __name__ == "__main__":
    main()