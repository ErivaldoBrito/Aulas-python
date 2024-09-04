""" CONTANDO NÚMEROS NEGATIVOS
 ENUNCIADO:
     - Desenvolva um programa que conte quantos números negativos foram inseridos pelo usuário usando laço While. 
     - O programa deve para quando o usuário inserir 0 ou um numero positivo. Mostre a quantidade de numeros positivos.
     - DICA: Utilize uma variável para contar os números negativos e continue solicitando números até que um numero positivo ou 0 seja inserido.
"""

import os 
os.system("cls || clear")

while True:
    numero = int(input("Digite um número: "))

    if numero < 0:
        contador = contador +1

    if numero == 0:
        break

while(f"Quantidade de números Negativos: {contador}")     

