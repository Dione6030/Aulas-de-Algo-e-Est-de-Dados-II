frases = ("Às vezes ouço passar o vento e só de ouvir o vento passar vale a pena ter nascido Se você quer saber o que é o amor amor é cuidar amor é esperar amor é dar")

listaPalavras = frases.split(" ")

dicionario = {}

for palavra in listaPalavras:
    if(palavra in dicionario):
        dicionario[palavra] += 1
    
    else:
        dicionario[palavra] = 1

print(dicionario)