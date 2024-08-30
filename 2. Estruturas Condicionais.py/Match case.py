import os
os.system("cls || clear")

print("""
  1 - cadastrar usuário
  2 - excluir usuário
  3 - sair do sistema
      """)             

opcao = int(input("Digite uma opção: "))

match(opcao):
    case 1:
        print("Opção de Cadastrar Usuário.")
    case 2:
        print("Opção de Excluir Usuário.")
    case 3:
        print("Opção de Sair do Sistema.")   
    case _: ("Opção Inválida.")

print("=== FIM ===")