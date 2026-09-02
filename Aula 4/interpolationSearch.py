# Um projeto por Dione F. Pinheiro

valores = [10, 15, 20, 25, 30, 35, 40, 45, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Quantidade de valores
quantidade = len(valores)

# Nosso tesouro
x = 30

# Onde os indices testados serão guardadas
tentativas = []

# Algoritmo
def pesquisaPorInterpolacao(lista, inicio, fim, objetivo):
    
    # Para garantir que o nosso objetivo vai ser um numero dentro dos valores e haverá mais de um valor na lista
    if (inicio < fim and objetivo >= valores[inicio] and objetivo <= valores[fim]):
        
        # Posição aproximada
        posicao = inicio + ((objetivo - lista[inicio]) * (fim - inicio)) // (lista[fim] - valores[inicio])
        
        # Se achar o valor, apresenta o indice da posição
        if valores[posicao] == x:
            
            # Checa se houveram tentativas
            if len(tentativas) > 0:
                return print(f"Seu valor está na posição: {posicao} \n Antes de encontrar, ele passou pelas:", tentativas)
            
            # Foi de primeira
            else:
                return print(f"Seu valor está na posição: {posicao}")
        
        # Se não achou de primeira, procura de novo com menos informações
        if valores[posicao] < x :
            tentativas.append(posicao)
            return pesquisaPorInterpolacao(lista, posicao + 1, fim, objetivo)
        
        # Se não achou de primeira, procura de novo com menos informações
        if valores[posicao] > x :
            tentativas.append(posicao)
            return pesquisaPorInterpolacao(list, inicio, posicao - 1, objetivo)
    
    # Evita divisões por zero
    if (inicio == fim):
        return print("Deve haver pelo menos dois valores no indice!")
    
    # Se não tem, não acha.
    return print("Número não encontrado.")

# o que será apresentado no terminal
indice = pesquisaPorInterpolacao(valores, 0, quantidade -1 , x)


#=======================/RESPOSTA DAS QUESTÕES\=============================#

# a) Ele não procura pelo meio, pois ele busca o indice mais próximo possível do que está procurando e se não acha, ele recalcula, tirando o que ele já tentou, para tentar encontrar.

# b) Ele funciona em dados que estão ordenados e, ele precisa que os dados esteja distribuidos de um jeito uniforme, com um padrão de salto bem definido para o indice, exemplos: dicionário (pois as primeiras letras, se estiverem em ordem alfabetica, podem ser mapeados por números de 1 a 26), logs e cronogramas (que são gerados em intervalos regulares) e códigos de cores em hexadecimal.

