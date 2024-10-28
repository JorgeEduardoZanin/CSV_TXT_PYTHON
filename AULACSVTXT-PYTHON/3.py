import csv

def fat(n):#fatorial
    resultado=1
    resultados_intermediarios = []
    for i in range(2,n+1):
            resultado =resultado* i #1x2 2x3 6x4 24x5
            resultados_intermediarios.append(resultado) #2, 6 , 24, 120
    return resultados_intermediarios

num = 5
resultado_fat = fat(num)


arquivo_fat = "fat.csv"


with open(arquivo_fat, mode="w", newline="") as arquivo: 
    escrever_csv = csv.writer(arquivo)
    print(escrever_csv)
    escrever_csv.writerow(["Position", "Number"])#cabecalho


    for i, numero in enumerate(resultado_fat):#iteracao sobre a posicao e numero
        escrever_csv.writerow([ i+1, numero])#para cada posicao um numero

