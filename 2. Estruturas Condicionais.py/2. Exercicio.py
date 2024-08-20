import os
os.system("cls||clear")

# Solicitando dados.
numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))
              
soma = numero_1 + numero_2
media = soma / 2
produto = (numero_1 * numero_2)

if  (numero_1 > numero_2):
    maior = numero_1
    menor = numero_2
else:
    maior = numero_2
    menor = numero_1

print(f"numero_1: {numero_1}. ")
print(f"numero_2: {numero_2}. ")
print(f"soma: {soma}. ")
print(f"media: {media}. ")
print(f"produto: {produto}. ")

              