import os 
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

def ler_numero(mensagem): 
    while True:
        try: 
            return float(mensagem) # Corrigido: float
        except ValueError:
            print("Valor inválido. Digite um número.")

def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Ver histórico")
    print("6 - Salvar histórico em arquivo")
    print("0 - Sair")

def salvar_historico(): 
    with open("historico.txt", "w", encoding="utf-8") as arquivo: # Corrigido: encoding
        for linha in historico:
            arquivo.write(linha + "\n")
    print("Histórico salvo em 'historico.txt'.")

def main(): 
    operacoes = {
        "1": ("Soma", somar, "+"),
        "2": ("Subtração", subtrair, "-"),
        "3": ("Multiplicação", multiplicar, "*"),
        "4": ("Divisão", dividir, "/"),
    }

    # Toda essa lógica agora está devidamente indentada dentro da main()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando a calculadora. Até logo!")
            break
        elif opcao == "5":
            if not historico:
                print("Histórico vazio.")
            else:
                print("\n--- HISTÓRICO ---")
                for linha in historico:
                    print(linha)
        elif opcao == "6":
            salvar_historico()
        elif opcao in operacoes:
            nome, funcao, simbolo = operacoes[opcao]
            a = ler_numero(input("Digite o primeiro número: ")) # Ajustado para ler o input corretamente
            b = ler_numero(input("Digite o segundo número: "))
            try:
                resultado = funcao(a, b) # Corrigido: resultado
                registro = f'{a} {simbolo} {b} = {resultado}'
                print(f"Resultado: {resultado}")
                historico.append(registro)
            except ZeroDivisionError as e:
                print(f"Erro: {e}")
        else: # Alinhado corretamente com os outros 'if/elif' da opção
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()