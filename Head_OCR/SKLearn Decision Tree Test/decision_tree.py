from sklearn import tree
import image_processing as ip
import numpy as np

def guess(image_file_name):
    features = [] # amostras
    labels = [] # legenda das amostras
    labels = [1, 0, 0, 1, 1, 0, 0, 0, 1, 0] # [MULHER 0] [HOMEM 1]

    i=1
    while i<=10:
        file=str(i)+'.jpg'
        image = ip.open_gray(file) # open image file

        matrix = ip.image_to_matrix(image)
        matrix = ip.threeD_twoD(matrix)
        matrix = ip.twoD_oneD(matrix)
        
        features.append(matrix)
        
        i+=1

    image_file = ip.open_gray(image_file_name)
    image_file = ip.image_to_matrix(image_file)
    image_file = ip.threeD_twoD(image_file)
    image_file = ip.twoD_oneD(image_file)

    # o classificador encontra padrões nos dados de treinamento
    clf = tree.DecisionTreeClassifier() # instância do classificador
    clf = clf.fit(features, labels) # fit encontra padrões nos dados

    # classificar uma nova imagem
    ans = (clf.predict([image_file]))

    if ans==0:
        gender='MULHER'
    elif ans==1:
        gender='HOMEM'

    return gender

A=guess('teste.jpg')
B=guess('teste2.jpg')
C=guess('teste3.jpg')
D=guess('teste4.jpg')

print('TESTE 1:\tRESPOSTA: HOMEM\t\t\tPALPITE: ',A)
print('TESTE 2:\tRESPOSTA: HOMEM\t\t\tPALPITE: ',B)
print('TESTE 3:\tRESPOSTA: MULHER\t\tPALPITE: ',C)
print('TESTE 4:\tRESPOSTA: RATO COM METRALHADORA\tPALPITE: ',D)