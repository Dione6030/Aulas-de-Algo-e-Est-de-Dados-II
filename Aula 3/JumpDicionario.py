import math
import pandas as pd

def jump_search(lista, num, inicio, fim):
    
    passos = math.sqrt(len(lista))
    
    while lista[int(min(passos, fim)-1)]:
        inicio = passos
        passos += math.sqrt(len(lista))
        if inicio >= fim:
            return -1
    
    return inicio, fim

def binary_search(lista, num, inicio, fim):
    meio = inicio + (fim - inicio) // 2
    
    if lista[meio] == num:
        return lista[]

def pesquisa(lista, num):
    inicio, fim = 0, len(lista)
    
    while inicio <= num:
        jump_search(lista, num, inicio, fim)
    
    while inicio <= num:
        binary_search(lista,num, inicio, fim)
    

def main():
    df = pd.read_csv("/Aula 3/datasets/numeros_1M_ordenado.csv")
    leitor = df["numero"].to_list
    
    print(pesquisa(leitor, 5644))

main()