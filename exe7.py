#Peça 4 notas e calcule a média.


lista = []

for i in range(4):
    num = int(input("Digite um número: "))
    lista.append(num)

    media = (sum(lista)) / 4

print("\n A média dos números ", lista, " é: ", media)