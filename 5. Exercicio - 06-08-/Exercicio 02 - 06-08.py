""" Faça um programa que imprima a tabuada de um numero informado pelo 
usuário de 1 a 10 utilizando uma função para exibir o resultado
"""

import os
os.system("cls || clear")

# Processamento
def mostrar_tabuada(numero, i):
    return f"{numero} x {i} = {numero * i}"
    
# Entrada de dados

numero = int(input("Digite um número: "))    

# Saida

for i in range(1,11):
    print(mostrar_tabuada(numero, i))
