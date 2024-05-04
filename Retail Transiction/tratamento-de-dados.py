# Bibliotecas para realizar tratativas de dados
import pandas as pd
import numpy as np
from datetime import datetime, date
import locale
# Biblioteca para leitura de diretórios
from glob import glob
from xlsxwriter import workbook, worksheet
import os
# Bibliotecas para visualização de dados
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns

# Setando a localização
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Fazendo leitura dos arquivos
arquivo_clientes = glob(
    "C:/Users/Victor Hugo/Downloads/Retail Transiction/archive/Retail_Transaction_Dataset.xlsx")
dataframe_lista_clientes = []
for arquivo in arquivo_clientes:
    dataframe_temp_clientes = pd.read_excel(io=arquivo)
    dataframe_lista_clientes.append(dataframe_temp_clientes)
dataframe_clientes_raw = pd.concat(dataframe_lista_clientes)

# Excluindo Coluna
dataframe_clientes = dataframe_clientes_raw.drop(
    columns=["StoreLocation", "ProductID"])

# Formatando Colunas
dataframe_clientes['TransactionDate'] = pd.to_datetime(
    dataframe_clientes['TransactionDate']).dt.floor('d').dt.date  # Convertendo a Data para datetime
dataframe_clientes["Price"] = dataframe_clientes["Price"].map(
    lambda x: locale.currency(x, grouping=True))  # Convertendo os preços para o sistema monetário do Brasil
dataframe_clientes["TotalAmount"] = dataframe_clientes["TotalAmount"].map(
    lambda x: locale.currency(x, grouping=True))  # Convertendo o total para o sistema monetário do Brasil
dataframe_clientes["DiscountApplied(%)"] = (
    dataframe_clientes["DiscountApplied(%)"] / 100)  # Colocando a coluna de discontos na casa decimal correta
dataframe_clientes["DiscountApplied(%)"] = (
    dataframe_clientes["DiscountApplied(%)"] * 100).apply(lambda x: '{:.2f}%'.format(x))  # Convertendo para porcentagem e mostrando apenas 2 casas depois da virgula

# Debug
# print(dataframe_clientes.count())
# print(dataframe_clientes.head())
# print(dataframe_clientes["TransactionDate"].head())
# print(dataframe_clientes["Price"].head())
# print(dataframe_clientes["TotalAmount"].head())
# print(dataframe_clientes["DiscountApplied(%)"].head())
# print(dataframe_clientes.dtypes)

caminho_novo_arquivo_excel = "C:/Users/Victor Hugo/Downloads/Retail Transiction/archive/Retail_Transaction_Dataset_Formatado.xlsx"
dataframe_clientes.to_excel(
    caminho_novo_arquivo_excel, index=False, engine='xlsxwriter')

print("Dados formatados salvos em Excel com sucesso!")
