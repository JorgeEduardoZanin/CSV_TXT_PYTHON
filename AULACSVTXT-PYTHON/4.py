import csv



# Código para ler e imprimir o arquivo CSV
with open("exemplo.txt", "r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
   
    #print(arquivo_csv)
   
    for i,linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabecalho"+str(linha))
        else:
            print("Valor"+str(linha))

