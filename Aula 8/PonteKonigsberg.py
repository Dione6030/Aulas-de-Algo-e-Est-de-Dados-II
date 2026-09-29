ponte = {
    'A': ['B', 'B', 'C', 'C', 'D'],
    'B': ['A', 'A', 'D'],
    'C': ['A', 'A', 'D'],
    'D': ['A', 'B', 'C']
}

def dfs(grafo, v, visitados):
    visitados.add(v)
    
    print(v)
    for w in grafo[v]:
        if w not in visitados:
            dfs(grafo, w, visitados)

dfs(ponte, 'A', set())