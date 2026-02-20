#Programa com menu para adicionar números, mostrar lista e calcular média.

def validar_numero():
    while True:
        try:
            return float(input("Digite um número: "))
        except ValueError:
            print("Erro: Digite apenas números válidos.")

def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def menu():
    numeros = []
    
    while True:
        print("\n--- MENU DE NÚMEROS ---")
        print("1. Adicionar número")
        print("2. Mostrar lista")
        print("3. Calcular média")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            num = validar_numero()
            numeros.append(num)
            print("Número", num, "adicionado!")
            
        elif opcao == '2':
            print("\nLista atual:", numeros if numeros else "Vazia")
            
        elif opcao == '3':
            media = calcular_media(numeros)
            print("\nA média dos números é: ", media)
            
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            
menu()