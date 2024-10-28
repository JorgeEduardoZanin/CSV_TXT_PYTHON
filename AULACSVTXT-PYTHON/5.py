import pandas as pd 

tabela = pd.read_csv("pessoas.csv")
print(tabela)
print(tabela["idade"].sum())
print(len(tabela["idade"]))


soma_idades = tabela["idade"].sum()


quantidade_idades = len(tabela["idade"])

media_idade = soma_idades / quantidade_idades

print(media_idade)