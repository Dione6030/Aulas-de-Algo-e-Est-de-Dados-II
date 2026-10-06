labirinto = [
    ".########.",
    "........#.",
    "I####.#.#.",
    "##..#.#.#.",
    "......#...",
    "#######.##",
    "...#..#.#.",
    ".#..F##...",
    ".#.###..#.",
    ".......#..",
]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))

inicio = achar(labirinto, 'I')
saida = achar(labirinto, 'F') 

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)] # ↑ → ↓ ←

def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo

grafo = montar_grafo(labirinto)

def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))

caminho = [(2,0), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (8,7), (8,6), (9,6), (9,5), (9,4), (9,3), (9,2), (8,2), (7,2), (7,3), (7,4)]

desenhar(labirinto, caminho)


# def dfs(grafo, inicio, saida): ...
# def bfs(grafo, inicio, saida): ...
# def gulosa(grafo, inicio, saida): ...
# cada uma devolve (caminho, casas_visitadas)