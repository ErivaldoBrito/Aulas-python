# ENCONTRANDO O PRIMEIRO NÚMERO DIVISÍVEL POR 7
#Enunciado: Escreva um programa que use o laço while para encontrar o 1º numero maior que 50 que seja divisível por 7. Exia esse número.


import os
os.system("cls||clear")

# SOLICITAÇÃO
 
numero = 2

# Verificando se o número é divisível por 7

while numero % 7 != 0:
    
    numero += 2

    #Imprimindo o resultado do número

print("O PRIMEIRO NÚMERO DIVISÍVEL POR 7 É:", numero)

