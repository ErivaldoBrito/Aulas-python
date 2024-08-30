""" Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota. Mostre em menu conforme o descrito abaixo:
S - Inserir mais uma nota;
P - Ver quantas notas foram inseridas.
N - Calcular a média aritmétrica para o usuário.
"""

import os
import time

while True:

    print("""
    \t=== MENU ===")
    S - Inserir uma Notas
    P - Ver quantas notas foram inseridas
    N - Calcular a média aritimétrica
          """)

resposta = input("Deseja inserir uma nota: "). upper()

match resposta:
    case "S":
        nota =float(input("\nDigite uma Nota: "))
        soma += nota
        quantidadeNotas += 1

    case "P":
        if quantidadeNotas == 0
break