# Sistema de lista de compras com funções para adicionar e remover.

lista_compras = []

def adicionar():
    item = input("O que deseja adicionar? ")
    lista_compras.append(item)
    print("Um", item, "foi adicionado!")

def remover():
    item = input("O que deseja remover? ")
    if item in lista_compras:
        lista_compras.remove(item)
        print("Um", item, " removido com sucesso.")
    else:
        print("Item não encontrado na lista.")

def mostrar():
    for item in lista_compras:
        print(item)


adicionar()
mostrar()