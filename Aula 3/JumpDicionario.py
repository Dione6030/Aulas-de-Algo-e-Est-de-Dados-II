import csv
import math
import pandas as pd

def jump_search(lista, num):
    
    passos = math.sqrt(lista)
    numeros_proximos = []
    
    anterior = 0
    
    df = pd.read_csv("datasets/numeros_1M_ordenado.csv")
    dado_csv = df["numero"].to_list()
    
    while dado_csv[int(min(passos, lista))] < num:
        anterior = passos
        passos += math.sqrt(lista)
        
        if anterior >= lista:
            return -1
        
    metade_do_caminho = anterior
    fim_da_metade_do_caminho = anterior + passos
    distancia = fim_da_metade_do_caminho - metade_do_caminho
    anterior = 0
    passos = math.sqrt(distancia)
    
    while dado_csv[int(min(metade_do_caminho, fim_da_metade_do_caminho))] < num:
        anterior = passos
        passos += math.sqrt(distancia)
        if anterior >= distancia:
            return - 1
    
    metade_do_caminho = anterior
    fim_da_metade_do_caminho = anterior + passos
    distancia = fim_da_metade_do_caminho - metade_do_caminho
    anterior = 0
    passos = math.sqrt(distancia)
    
    while dado_csv[int(min(metade_do_caminho, fim_da_metade_do_caminho))] < num:
        anterior = passos
        passos += math.sqrt(distancia)
        if anterior >= distancia:
            return - 1
    
    metade_do_caminho = anterior
    fim_da_metade_do_caminho = anterior + passos
    
    while dado_csv[int(anterior)] <= fim_da_metade_do_caminho:
        numeros_proximos.append(anterior)
    
    return numeros_proximos

def conta_linhas_csv():
    df = pd.read_csv("datasets/numeros_1M_ordenado.csv")
    leitor = df["numero"].to_list()
        
    total_linhas = len(list(leitor))
    return total_linhas

def main():
    total_linhas = conta_linhas_csv()
    
    print(jump_search(total_linhas, 5644))

main()