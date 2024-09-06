"""Crie um programa que leia números e informe por meio de uma função:
- Quantos números são pares;
- Quantos números são ímpares.
"""

import os
os.system("cls || clear")

def verificar_pares_impares():
    pares = 0
    impares = 0
        
    for i in range(6):
        numero = int(input("Digite um número: "))

        if numero % 2 == 0:
            pares += 1

        else:
            impares += 1

    print(f"\nQuantidade pares: {pares}")           
    print(f"\nQuantidade impares: {impares}") 

# CHAMANDO A FUNÇÃO
verificar_pares_impares()
