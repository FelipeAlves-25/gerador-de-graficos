import json
from os import system
from pathlib import Path

# Função para criar arquivo de configuração do gráfico
def cria():
    # variáveis globais
    content = {}
    dir = Path("src/graphs")

    # configurações iniciais
    title = input("Por favor, digite aqui o título do seu gráfico: ") # título
    content["title"] = title
    g_type = input("Digite aqui o tipo de gráfico que você deseja criar (linha, coluna, pizza): ") # tipo do gráfico
    content["graphic-type"] = g_type

    # Verifica se há arquivos não nomeados
    arch_unamed = "unamed_"
    count = 1
    for i in dir.glob("*.json"):
        if i == dir / f"{arch_unamed + str(count)}.json":
            count += 1
    
    arch_unamed += f"{str(count)}.json"
    arch_name = input(f"Digite agora o nome desejado para o arquivo (padrão: \"{arch_unamed}\"): ")
    if len(arch_name) > 0:
        content["archive-name"] = arch_name
    else:
        content["archive-name"] = arch_unamed

    with open(f"{dir}/{content['archive-name']}", "w") as o:
        json.dump(content, o)
