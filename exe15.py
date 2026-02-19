#Função que recebe lista e retorna soma total.

def soma():
    lista = []

    for i in range(5):
        num = int(input("Digite um número: "))
        lista.append(num)

    soma_total = sum(lista)

    print("\n A soma total dos números ", lista, " é: ", soma_total)

soma()