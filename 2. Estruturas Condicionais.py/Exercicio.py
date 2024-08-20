import os
os.system("cls||clean")

# Solicitando dados
aluno = int("Digite seu nome: ")
idade = int(input("Digite sua idade"))
nota1 = float(input("Digite sua primeira nota"))
nota2 = float(input("Digite sua segunda nota"))
nota3 = float(input("Digite sua terceira nota"))


soma = nota1 + nota2 + nota3
media = soma /3


if media > 7:
    resultado = "APROVADO"
else:
    resultado = "REPROVADO"

print("\nEXGIBINDO RESULTADOS")
print(f"Nome: {aluno}. ")
print(f"idade: {idade} anos.")
print(f"nota1: {nota1}. ")
print(f"nota2: {nota2}. ")
print(f"nota3: {nota3}. ")
print(f"resultado: {resultado}. ")


