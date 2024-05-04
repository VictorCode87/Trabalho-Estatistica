# Script para formatar uma planilha CSV para obter colunas

import pandas as pd

# Carregando o arquivo CSV
caminho_arquivo_csv = "C:/Users/Victor Hugo/Downloads/Retail Transiction/archive/Retail_Transaction_Dataset.csv"
dados = pd.read_csv(caminho_arquivo_csv, sep=",")

# Visualizando os dados
print("Dados originais:")
print(dados)

# Salvando os dados formatados em um novo arquivo Excel
caminho_novo_arquivo_excel = "C:/Users/Victor Hugo/Downloads/Retail Transiction/archive/Retail_Transaction_Dataset.xlsx"
dados.to_excel(caminho_novo_arquivo_excel, index=False)

print("Dados formatados salvos em Excel com sucesso!")
