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

def main():
    valores = [10, 5, 2, 7, 15, 12, 20]
    arvore = None
    
    # Construindo a árvore usando o laço de repetição
    for valor in valores:
        arvore = inserir(arvore, valor)
        
    print("Travessia em Pré-ordem:")
    preOrdem(arvore)

if __name__ == "__main__":
    main()