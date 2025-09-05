import csv
import math

with open('pratica7/data/datalog_treinamento.csv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.DictReader(csvfile)

    tempos = []

    for row in spamreader:
        tempo = float(row['tempo_execucao_segundos'])
        tempos.append(tempo)
        print(row['modelo'], tempo)

    media = sum(tempos) / len(tempos)

    variancia = sum((t - media) ** 2 for t in tempos) / len(tempos)
    desvioPadrao = math.sqrt(variancia)

    print(f"A quantidade de linhas do arquivo é {len(tempos)}")
    print(f"A média do tempo de execução é {media:.2f}")
    print(f"O desvio padrão do tempo de execução é {desvioPadrao:.2f}")
