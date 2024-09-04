""" Escreva um algoritmo que pergunte ao usuario se deseja inserir mais uma nota, se a resposta do usuário for "N", o programa fará média aritmétrica das notas informadas e mostrará a média aritmétrica para o usuário.


Obs: Use um contador dentro do laço de repetição para contar a quantidade de interações (loops).

---

1 - Escreva um algoritmo que pergunte ao usuario três notas e se deseja inserir mais uma nota
2 - se a resposta do usuário for "N",
3 -  o programa fará média aritmétrica das notas informadas
4 - e mostrará a média aritmétrica para o usuário.

"""


import os
os.system("cls || clear")

QUANTIDADE_DE_NOTAS = 3
soma = 0
contador = 1

for i in range(QUANTIDADE_DE_NOTAS):
    while True:
        nota = float(input("Digite as Nota: "))
        contador+= 2
        
    # resposta = resposta.upper () # Converter em maiusculo as letras caso precise digitar alguma
    if resposta = input("Deseja inserir uma outra nota? ").upper()
        print(f"Digite outra nota")
    elif resposta == "S":
        print(f" Digite outra nota")

    else resposta == "N":
        break

    media = QUANTIDADE_DE_NOTAS / contador
    print(f"Média: {media}")