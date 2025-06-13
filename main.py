# from os import system
import matplotlib.pyplot as mpl
import src.actions as act

while True:
    print("Seja bem-vindo ao gerador de gráficos.\n\nPor favor, selecione a função desejada:\n")
    print("[1] Novo gráfico\n[2] Carregar gráfico existente\n[3] Sair\n")
    op = int(input("Digite aqui: "))

    match op:
        case 1:
            act.system("clear")
            act.cria()
        case 3:
            print("\nObrigado por utilizar meu programa. :D")
            break
        case _:
            print("\nDesculpe comando não encontrado, digite outro.")
