#Sistema de notas usando funções (ler, calcular média e mostrar).

def Leitura():
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    return nota1, nota2

def calc_Media(nota1, nota2):
    return (nota1 + nota2) / 2

def notas():
    valor1, valor2 = Leitura()

    media_final = calc_Media(valor1, valor2)
    
    print("Sua média é: ", media_final)

notas()