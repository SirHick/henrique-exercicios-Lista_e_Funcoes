#Função que solicita número inteiro válido com try/except.

def validacao():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))

            if(num % 2 == 0):
                print("PAR")
                
            else:
                print("ÍMPAR")
            break
        except ValueError:
            print("Valor Inválido")

validacao()