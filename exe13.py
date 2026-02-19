#Função que verifica se número é par ou ímpar.

def par_Impar():
    num = int(input("Digite um número: "))

    if(num % 2 == 0):
        print("par")
    else:
        print("ímpar")

par_Impar()