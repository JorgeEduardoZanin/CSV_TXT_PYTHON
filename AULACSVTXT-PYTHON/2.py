import csv


pessoas = [
    {"nome": "Joao", "idade": 25, "peso": 70.5, "altura": 1.75},
    {"nome": "Maria", "idade": 30, "peso": 65.0, "altura": 1.68},
    {"nome": "Carlos", "idade": 28, "peso": 80.2, "altura": 1.80},
    {"nome": "Ana", "idade": 22, "peso": 55.4, "altura": 1.60},
]

arquivo_csv = "pessoas.csv"


with open(arquivo_csv, mode="w", newline="") as arquivo:
    escritor_csv = csv.DictWriter(arquivo, fieldnames=["nome", "idade", "peso", "altura"])#cria o objeto para escrever os dicionarios no arquivo
    
    
    escritor_csv.writeheader()#escreve cabecalho
    
    
    for pessoa in pessoas:
        escritor_csv.writerow(pessoa)#itera sobre o dicionario e escreve os dados

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")


