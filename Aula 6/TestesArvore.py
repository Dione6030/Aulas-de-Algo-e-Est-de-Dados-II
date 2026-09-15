class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def inserir(raiz, valor):
    if raiz is None:
        return Node(valor)
    if valor < raiz.valor:
        raiz.esq = inserir(raiz.esq, valor)
    else:
        raiz.dir = inserir(raiz.dir, valor)
    return raiz

def preOrdem(raiz):
    if raiz is not None:
        # 1. Visita a raiz (imprime o valor)
        print(raiz.valor, end=" ")
        # 2. Vai para a subárvore esquerda
        preOrdem(raiz.esq)
        # 3. Vai para a subárvore direita
        preOrdem(raiz.dir)


def emOrdem(raiz):
    if raiz is not None:
        # 1. olha o da esquerda primeiro
        emOrdem(raiz.esq)
        # 2. visita o node
        print(raiz.valor, end=" ")
        # 3. olha a direita no final
        emOrdem(raiz.dir)

def posOrdem(raiz):
    if raiz is not None:
        posOrdem(raiz.esq)
        posOrdem(raiz.dir)
        print(raiz.valor, end=" ")

def main():
    valores = [10, 5, 2, 7, 15, 12, 20]
    arvore = None
    
    # Construindo a árvore usando o laço de repetição
    for valor in valores:
        arvore = inserir(arvore, valor)
        
    print("Travessia em Pré-ordem:")
    preOrdem(arvore)
    print("\n Travessia em ordem:")
    emOrdem(arvore)
    print("\n Travessia Pos-ordem:")
    posOrdem(arvore)

if __name__ == "__main__":
    main()