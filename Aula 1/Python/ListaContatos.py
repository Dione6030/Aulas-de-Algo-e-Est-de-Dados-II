Contatos = {
    "Yago": "991935134",
    "Diego": "991987654",
    "Pedro": "991123456",
    "Igor": "991526798",
    "Paulo": "99512619"
    }

def listar():
    print(Contatos)

def pesquisar(nome):
    print(Contatos[f"{nome}"])

while True:
    print("Menu principal")
    print("1. Listar contatos.")
    print("2. Pesquisar contato.")
    print("3. Sair.")
    print("")
    
    opcao = input("Opção: ")
    if opcao == "1":
        print("")
        listar()
        print("")
    elif opcao == "2":
        nome = input("Qual seria o nome? ")
        print("")
        pesquisar(nome)
        print("")
    else:
        break