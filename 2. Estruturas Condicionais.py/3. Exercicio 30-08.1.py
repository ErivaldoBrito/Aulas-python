""" Escreva um algoritmo que leia três notas de um aluno caso seja menor que 0 ou maior de 10, mostre a pergunta novamente.
Apos receber as notas dentro dos parâmetros acima, calcule a média e verifique se o aluno esta Aprovado, recuperação ou reprovado considerando os seg9intes critérios:
- Se a média for apartir de 7, Aprovado;
- Se a média for entre 5 e 6,9, o aluno esta em recuperação;
Caso seja menor que 5, o aluno esta Reprovado"""


import os

os.system("cls || clear")

QUANTIDADE_DE_NOTAS = 3

soma = 0

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input(f"Digite {i+1} nota: "))
    
        if nota < 0 or nota > 10:
            print("Nota invalida! \nDigite novamente...")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_DE_NOTAS

if media>= 7:
    print("Aprovado. ")

elif media>= 5:
    print("Recuperação. ")
    
else:     
    print("Reprovado. ")


print("===FIM===")    
