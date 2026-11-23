def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero!"
    else:
        return a / b


def menu():
    print("\n===== CALCULADORA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Calculadora encerrada!")
        break

    elif opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print("Resultado:", somar(num1, num2))

        elif opcao == "2":
            print("Resultado:", subtrair(num1, num2))

        elif opcao == "3":
            print("Resultado:", multiplicar(num1, num2))

        elif opcao == "4":
            print("Resultado:", dividir(num1, num2))

    else:
        print("Opção inválida! Tente novamente.")
