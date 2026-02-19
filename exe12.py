#Crie função que recebe lista e retorna média.

def media_Lista():
    lista = []

    for i in range(4):
        num = int(input("Digite um número: "))
        lista.append(num)

    media = (sum(lista)) / 4

    print("\n A média dos números ", lista, " é: ", media)

media_Lista()