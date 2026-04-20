import math


def menu():
    print("\n" + "="*45)
    print("         CALCULADORA COMPLETA")
    print("="*45)
    print("  1  - Soma")
    print("  2  - Subtração")
    print("  3  - Multiplicação")
    print("  4  - Divisão")
    print("  5  - Média")
    print("  6  - Equação de 2º grau")
    print("  7  - Fatorial")
    print("  8  - Conversão de unidades")
    print("  9  - Tabuada")
    print(" 10  - Fibonacci")
    print("  0  - Sair")
    print("="*45)

#  1. SOMA 
def soma():
    n = int(input("Quantos números deseja somar? "))
    total = 0
    for i in range(1, n + 1):
        valor = float(input(f"  Digite o {i}º número: "))
        total += valor
    print(f"\nResultado: {total}")

#  2. SUBTRAÇÃO 
def subtracao():
    a = float(input("Digite o 1º número: "))
    b = float(input("Digite o 2º número: "))
    print(f"\nResultado: {a} - {b} = {a - b}")

#  3. MULTIPLICAÇÃO
def multiplicacao():
    a = float(input("Digite o 1º número: "))
    b = float(input("Digite o 2º número: "))
    print(f"\nResultado: {a} × {b} = {a * b}")

#  4. DIVISÃO 
def divisao():
    a = float(input("Digite o dividendo: "))
    b = float(input("Digite o divisor: "))
    if b == 0:
        print("\nErro: não é possível dividir por zero!")
    else:
        print(f"\nResultado: {a} ÷ {b} = {a / b:.3f}")

#  5. MÉDIA 
def media():
    n = int(input("Quantos números? "))
    soma = 0
    for i in range(1, n + 1):
        valor = float(input(f"  Digite o {i}º número: "))
        soma += valor
    print(f"\nSoma: {soma}")
    print(f"Média: {soma / n:.4f}")

#  6. EQUAÇÃO DE 2º GRAU 
def equacao_segundo_grau():
    print("Equação: ax² + bx + c = 0")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    if a == 0:
        print("\nErro: 'a' não pode ser zero (não seria de 2º grau).")
        return

    delta = b**2 - 4 * a * c
    print(f"\nDelta = {delta}")

    if delta < 0:
        print("Sem raízes reais (delta negativo).")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Uma raiz real: x = {x:.4f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Duas raízes reais:")
        print(f"  x1 = {x1:.4f}")
        print(f"  x2 = {x2:.4f}")

#  7. FATORIAL 
def fatorial():
    n = int(input("Digite um número inteiro positivo: "))
    if n < 0:
        print("Erro: fatorial não existe para negativos.")
        return
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    print(f"\n{n}! = {resultado}")

#  8. CONVERSÃO DE UNIDADES 
def conversao():
    print("\nEscolha a conversão:")
    print("  1 - Celsius → Fahrenheit")
    print("  2 - Fahrenheit → Celsius")
    print("  3 - Km → Milhas")
    print("  4 - Milhas → Km")
    print("  5 - Kg → Libras")
    print("  6 - Libras → Kg")
    opcao = input("Opção: ")

    valor = float(input("Digite o valor: "))

    if opcao == "1":
        print(f"\n{valor}°C = {valor * 9/5 + 32:.2f}°F")
    elif opcao == "2":
        print(f"\n{valor}°F = {(valor - 32) * 5/9:.2f}°C")
    elif opcao == "3":
        print(f"\n{valor} km = {valor * 0.621371:.4f} milhas")
    elif opcao == "4":
        print(f"\n{valor} milhas = {valor / 0.621371:.4f} km")
    elif opcao == "5":
        print(f"\n{valor} kg = {valor * 2.20462:.4f} libras")
    elif opcao == "6":
        print(f"\n{valor} libras = {valor / 2.20462:.4f} kg")
    else:
        print("Opção inválida.")

#  9. TABUADA 
def tabuada():
    n = int(input("Digite o número para a tabuada: "))
    print(f"\n── Tabuada do {n} ──")
    for i in range(1, 11):
        print(f"  {n} x {i} = {n * i}")

#  10. FIBONACCI
def fibonacci():
    n = int(input("Quantos termos da sequência de Fibonacci? "))
    if n <= 0:
        print("Erro: informe um valor positivo.")
        return

    print("\nSequência de Fibonacci:")
    a, b = 0, 1
    for i in range(n):
        print(f"  F({i}) = {a}")
        a, b = b, a + b

#  PROGRAMA PRINCIPAL
opcoes = {
    "1": soma,
    "2": subtracao,
    "3": multiplicacao,
    "4": divisao,
    "5": media,
    "6": equacao_segundo_grau,
    "7": fatorial,
    "8": conversao,
    "9": tabuada,
    "10": fibonacci,
}

while True:
    menu()
    escolha = input("Escolha uma opção: ").strip()

    if escolha == "0":
        print("\nAté logo!")
        break
    elif escolha in opcoes:
        opcoes[escolha]()
    else:
        print("\nOpção inválida. Tente novamente.")