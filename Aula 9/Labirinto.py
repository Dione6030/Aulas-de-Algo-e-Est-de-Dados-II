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

print("Busca na mão:")
caminho = [(2,0), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (8,7), (8,6), (9,6), (9,5), (9,4), (9,3), (9,2), (8,2), (7,2), (7,3), (7,4)]
print("Passos até a saída:",len(caminho))
desenhar(labirinto, caminho)
print("\n")

caminho_dfs = []
def dfs(grafo, inicio, saida, visitados): 
    visitados.add(inicio)
    
    if inicio == saida:
        return caminho_dfs
    
    for passo in grafo[inicio]:
        if passo not in visitados:
            caminho_dfs.append(passo)
            
            passo_atual = dfs(grafo, passo, saida, visitados)
            if passo_atual is not None:
                return caminho_dfs
    return None

print("Busca por Profundidade:")
dfs(grafo, (2,0), (7,4), set())
print("Passos até a saída:",len(caminho_dfs))
desenhar(labirinto, caminho_dfs)
print("\n")

caminho_bfs = []
from collections import deque
def bfs(grafo, inicio, saida): 
    visitados = {inicio}
    fila = deque([inicio])
    
    while fila:
        v = fila.popleft()
        caminho_bfs.append(v)
        if v == saida:
            return caminho_bfs
        for passo in grafo[v]:
            if passo not in visitados:
                visitados.add(passo)
                fila.append(passo)

print("Busca por Largura:")
bfs(grafo, (2,0), (7,4))
print("Passos até a saída:",len(caminho_bfs))
desenhar(labirinto, caminho_bfs)
print("\n")

import heapq

caminho_da_gulosa = []
def h(v, saida): 
    return abs(v[0] - saida[0]) + abs(v[1] - saida[1])

def gulosa(grafo, inicio, saida):
    visitados = {inicio}
    fronteira = [(h(inicio, saida), inicio)]
    
    while fronteira:
        _, v= heapq.heappop(fronteira)
        caminho_da_gulosa.append(v)
        if v == saida:
            return caminho_da_gulosa
        for passo in grafo[v]:
            if passo not in visitados:
                visitados.add(passo)
                heapq.heappush(fronteira, (h(passo, saida), passo))
    

print("Busca Gulosa:")
gulosa(grafo, (2,0), (7,4))
print("Passos até a saída:",len(caminho_da_gulosa))
desenhar(labirinto, caminho_da_gulosa)
print("\n")

# cada uma devolve (caminho, casas_visitadas)