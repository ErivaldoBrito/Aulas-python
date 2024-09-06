""" Crie uma função que receba um número e mostre uma mensagem informando 
se o número é par ou ímpar.
"""


import os
os.system("cls || clear")


# Processamento
def numero_par(numero):
    if numero %2 == 0:
      print("Número Par")

    else:
        print("Número Ímpar")

 # Saida

numero = int(input("Digite um numero: "))
numero_par(numero)

print("===FIM===")