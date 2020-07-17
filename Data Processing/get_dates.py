import os, csv
import re



with open(r'C:/Users/gpimenta/Desktop/snapshot backup/limpando os anos/lista_snaps_limpa.CSV', 'r') as arquivo_csv:

    # print(arquivo_csv)

    leitor = list(csv.reader(arquivo_csv, delimiter='\n'))

    with open(r'C:/Users/gpimenta/Desktop/snapshot backup/limpando os anos/snaps_2012_2015.CSV', 'w', newline='') as new_doc:



        

        for linha in leitor:

            escrever = True

            l = str(linha)
            
            if (re.search('2017', l, re.IGNORECASE)):
                print(l+' foi excluido')
                escrever = False
            if (re.search('2016', l, re.IGNORECASE)):
                print(l+' foi excluido')
                escrever = False
            if (re.search('2018', l, re.IGNORECASE)):
                print(l+' foi excluido')
                escrever = False
            if (re.search('2019', l, re.IGNORECASE)):
                print(l+' foi excluido')
                escrever = False
            if (re.search('2020', l, re.IGNORECASE)):
                print(l+' foi excluido')
                escrever = False

            if escrever==True:
                
                writer = csv.writer(new_doc)
                writer.writerow(linha)

                

        
    # date_index=2
    # snap_index=3

    # with open('lista_snaps_limpa.CSV', 'w', newline='') as new_doc:

    #     writer = csv.writer(new_doc)

    #     writer.writerow(["DATA;ID"])

    #     while (date_index<14171):

    #         date = str(leitor[date_index])
    #         snap = str(leitor[snap_index])

    #         date = date.replace('"' , '')
    #         date = date.replace('[' , '')
    #         date = date.replace(']' , '')
    #         date = date.replace(' ' , '')
    #         date = date.replace("'" , '')
    #         date = date.replace("," , '')
    #         snap = snap.replace('"' , '')
    #         snap = snap.replace('[' , '')
    #         snap = snap.replace(']' , '')
    #         snap = snap.replace(' ' , '')
    #         snap = snap.replace("'" , '')
    #         snap = snap.replace("," , '')
            
    #         writer.writerow([date+";"+snap])

    #         date_index+=5
    #         snap_index+=5

    #         # print(date)
    #         # print(snap)





        
