import os
os.system("cls || clear")

# FUNÇÕES COM RETORNO.
def desconto_salario(salario_bruto):
    vale_transporte = 200
    vale_refeicao = 150
    plano_de_saude = 300

    resultado = salario_bruto - vale_transporte - vale_refeicao - plano_de_saude

    return resultado

salario_bruto = float(input("Digite o valor do seu salário bruto:"))

salario_liquido = desconto_salario(salario_bruto)

print(f"Salário Líquido: {salario_liquido}")
