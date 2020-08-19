from sklearn import tree
import numpy as np
import csv

def limpar(text): # removes unnecessary characters
    text = str(text)
    text = text.replace("\n",'')
    text = text.replace('"' , '')
    text = text.replace('[' , '')
    text = text.replace(']' , '')
    text = text.replace(' ' , '')
    text = text.replace("'" , '')
    text = text.replace("," , '')
    return text

def cpu_guess(spaces): # ML to preview moves
    features = [] # amostras
    labels = [] # legenda das amostras

    with open(r'feature.csv', 'r') as csv_file: # open csv
        csv_info = list(csv.reader(csv_file, delimiter='\n')) # read csv info
        for line in csv_info:
            x=str(line)
            x=list(limpar(x))

            print(x)
            features.append(x)
    csv_file.close()
    print(features)
    
    with open(r'label.csv', 'r') as csv_file: # open csv
        csv_info = list(csv.reader(csv_file, delimiter='\n')) # read csv info
        for line in csv_info:
            text=str(line)
            text=limpar(text)
            labels.append(text)
    csv_file.close()

    # o classificador encontra padrões nos dados de treinamento
    clf = tree.DecisionTreeClassifier() # instância do classificador
    clf = clf.fit(features, labels) # fit encontra padrões nos dados

    # previsão
    ans = (clf.predict([spaces]))
    ans = limpar(str(ans))
    return ans

#     if ans==0:
#         gender='MULHER'
#     elif ans==1:
#         gender='HOMEM'

#     return gender

# A=guess('teste.jpg')
# B=guess('teste2.jpg')
# C=guess('teste3.jpg')
# D=guess('teste4.jpg')

# print('TESTE 1:\tRESPOSTA: HOMEM\t\t\tPALPITE: ',A)
# print('TESTE 2:\tRESPOSTA: HOMEM\t\t\tPALPITE: ',B)
# print('TESTE 3:\tRESPOSTA: MULHER\t\tPALPITE: ',C)
# print('TESTE 4:\tRESPOSTA: RATO COM METRALHADORA\tPALPITE: ',D)

space=[1,1,0,0,0,0,0,0,0]
print(guess(space))