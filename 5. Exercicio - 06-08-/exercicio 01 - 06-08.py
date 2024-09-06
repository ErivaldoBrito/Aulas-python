
""" Crie funções que recebam 2 numeros e retorne a soma. subtração, 
divisão e a multiplicação destes numeros informados
Obs: Crie uma função para cada operação.
"""

import os
os.system("cls || clear")

# Funções


def operacao_adicao(numero1,numero2):
    adicao=numero1+numero2
    return adicao
def operacao_subtracao(numero1,numero2):
    subtracao=numero1-numero2
    return subtracao
def operacao_mutiplicacao(numero1,numero2):
    multiplicacao=numero1*numero2
    return multiplicacao
def operacao_divisao(numero1,numero2):
    divisao=numero1/numero2
    return divisao 

numero1=float(input("Digite o numero: "))
numero2=float(input("Digite o numero: "))
   
import os
os.system("cls || clear")

adicao=operacao_adicao(numero1,numero2)
subtracao=operacao_subtracao(numero1,numero2)
multiplicacao=operacao_mutiplicacao(numero1,numero2)
divisao=operacao_divisao(numero1,numero2)

print(f"A Soma dos numeros é: {adicao}")
print(f"A subtracao dos numeros é: {subtracao}")
print(f"A Multiplicacao dos numeros é: {multiplicacao}")
print(f"A divisao dos numeros é: {divisao}")


