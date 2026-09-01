import math
import pandas as pd

def jump_search(lista, num, inicio):
    
    passos = int(math.sqrt(len(lista)))
    fim = inicio + passos
    
    while lista[int(min(inicio, fim))] <= num:
        inicio += passos
        fim = inicio + passos
        if inicio >= len(lista):
            return -1, -1
    
    fim = inicio
    inicio -= passos
    return inicio, fim

def binary_search(lista, num, inicio, fim):
    if inicio > fim:
        return print(f"O número {num} não foi encontrado")
    
    meio = inicio + (fim - inicio) // 2
    
    if lista[meio] == num:
        print(f"O número {num} foi encontrado na posição {meio}")
        return retornaAproximado(lista, meio)
    
    if lista[meio] < num:
        return binary_search(lista, num, meio + 1, fim)
    
    if lista[meio] > num:
        return binary_search(lista, num, inicio, meio -1)

def retornaAproximado(lista, indice):
    inicio = max(0, indice -2)
    fim = min(len(lista), indice +3)
    
    return lista[inicio:fim]

def pesquisa(lista, num):
    inicio, fim = 0, len(lista)
    
    while fim == len(lista):
        inicio, fim = jump_search(lista, num, inicio)
    
    print(inicio, fim)
    
    return binary_search(lista,num, inicio, fim)
    

def main():
    df = pd.read_csv("datasets/numeros_1M_ordenado.csv")
    leitor = df["numero"].to_list()
    
    print(pesquisa(leitor, 5644))

main()