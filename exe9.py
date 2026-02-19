#Peça 6 números e mostre quantos são pares.

lista = []

for i in range(6):
    num = int(input("Digite um número: "))
    

    if(num % 2 == 0):
        lista.append(num)
    else:
        print("erro")

print(lista)