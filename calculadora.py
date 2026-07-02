import os 
import math 
historico = []

def somar(a, b): 
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero!")
    return a / b

def porcentagem(a, b):
    return (a * b) / 100

def potencia(a, b):
    a ** b

def raiz_quadrada(a, _):
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo!")
    return math.sqrt(a)

def resto_divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível calcular o resto da divisão por zero!")
    return a % b

def divisao_inteira(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível calcular a divisão inteira por zero!")
    return a // b

OPERACOES_UNARIAS = {"7"}

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número.")

def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("--- Básicas ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("--- Extras ---")
    print("5 - Porcentagem  (ex: 20% de 350)")
    print("6 - Potência     (ex: 2³)")
    print("7 - Raiz quadrada")
    print("8 - Resto da divisão")
    print("9 - Divisão inteira")
    print("--- Histórico ---")
    print("H - Ver histórico")
    print("S - Salvar histórico em arquivo")
    print("0 - Sair")

def salvar_historico(): 
    with open("historico.txt", "w", encoding="utf-8") as arquivo: # Corrigido: encoding
        for linha in historico:
            arquivo.write(linha + "\n")
    print("Histórico salvo em 'historico.txt'.")

def executar_operacao(opcao, operacoes):
    nome, funcao, simbolo = operacoes[opcao]

    a = ler_numero("Digite o número: ")

    # Operações unárias só precisam de um número
    if opcao in OPERACOES_UNARIAS:
        b = None
        resultado = funcao(a, None)
        registro = f"{simbolo}{a} = {resultado}"
    else:
        # Mensagem personalizada para porcentagem
        if opcao == "5":
            b = ler_numero("Digite a porcentagem (%): ")
        else:
            b = ler_numero("Digite o segundo número: ")
        resultado = funcao(a, b)
        registro = f"{a} {simbolo} {b} = {resultado}"

    print(f"Resultado: {resultado}")
    historico.append(registro)

def main():
    operacoes = {
        "1": ("Soma",            somar,          "+"),
        "2": ("Subtração",       subtrair,       "-"),
        "3": ("Multiplicação",   multiplicar,    "*"),
        "4": ("Divisão",         dividir,        "/"),
        "5": ("Porcentagem",     porcentagem,    "%"),
        "6": ("Potência",        potencia,       "**"),
        "7": ("Raiz quadrada",   raiz_quadrada,  "√"),
        "8": ("Resto divisão",   resto_divisao,  "%"),
        "9": ("Divisão inteira", divisao_inteira,"//"),
    }

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "0":
            print("Encerrando a calculadora. Até logo!")
            break

        elif opcao == "H":
            if not historico:
                print("Histórico vazio.")
            else:
                print("\n--- HISTÓRICO ---")
                for i, linha in enumerate(historico, start=1):
                    print(f"{i}. {linha}")

        elif opcao == "S":
            salvar_historico()

        elif opcao in operacoes:
            try:
                executar_operacao(opcao, operacoes)
            except (ZeroDivisionError, ValueError) as e:
                print(f"Erro: {e}")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()