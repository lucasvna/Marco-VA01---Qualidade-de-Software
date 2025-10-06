import math
import time

def adicao(a, b):
    return f"Resultado: {a + b:.2f}"

def subtracao(a, b):
    return f"Resultado: {a - b:.2f}"

def multiplicacao(a, b):
    return f"Resultado: {a * b:.2f}"

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return f"Resultado: {a / b:.2f}\nResto: {a % b:.2f}"

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não é possível calcular raiz quadrada de número negativo."
    return f"A raiz quadrada de {a:.2f} é {math.sqrt(a):.2f}"

if __name__ == "__main__":
    operacoes = {
        "1": adicao,
        "2": subtracao,
        "3": multiplicacao,
        "4": divisao,
        "5": raiz_quadrada
    }

    while True:
        print("\n=== CALCULADORA SIMPLES ===")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz Quadrada")
        opcao = input("Escolha uma operação (1-5): ")

        func = operacoes.get(opcao)

        if func:
            if opcao == "5":
                num = float(input("Digite um número: "))
                print(func(num))
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                print(func(num1, num2))
        else:
            print("Opção inválida.")

        time.sleep(0.5)
        print("\nDeseja continuar ou encerrar a calculadora?")
        print("1 - Continuar")
        print("2 - Encerrar")
        escolha = input("Escolha: ")

        if escolha == "2":
            print("\nObrigado por utilizar a calculadora!")
            time.sleep(0.5)
            break
