import os
os.system("cls || clear")

# Solicitação

resultado = 0

primeiro_numero = int(input(f"Digite o primeiro número: "))
segundo_numero = int(input(f"Digite o segundo número: "))
opcao = input("Digite uma opção (+ - * /): ")

match(opcao):
    case '+':
        resultado = primeiro_numero + segundo_numero
    case '-':
        resultado = primeiro_numero - segundo_numero
    case '*':
        resultado = primeiro_numero * segundo_numero
    case '/':    
        resultado = primeiro_numero / segundo_numero
    case _: ("Opção Inválida.")

print(f"Resultado: {resultado}")
print("=== FIM ===")