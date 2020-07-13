import os, csv



with open(r'C:/Users/gpimenta/Desktop/snapshot backup/lista_snaps.CSV', 'r') as arquivo_csv:

    # print(arquivo_csv)

    leitor = list(csv.reader(arquivo_csv, delimiter='\n'))

    # print(leitor[2])

    # for linha in leitor:
        
    #     print(linha)

    
    date_index=2
    snap_index=3

    with open('lista_snaps_limpa.CSV', 'w', newline='') as new_doc:

        writer = csv.writer(new_doc)

        writer.writerow(["DATA;ID"])

        while (date_index<14171):

            date = str(leitor[date_index])
            snap = str(leitor[snap_index])

            date = date.replace('"' , '')
            date = date.replace('[' , '')
            date = date.replace(']' , '')
            date = date.replace(' ' , '')
            date = date.replace("'" , '')
            date = date.replace("," , '')
            snap = snap.replace('"' , '')
            snap = snap.replace('[' , '')
            snap = snap.replace(']' , '')
            snap = snap.replace(' ' , '')
            snap = snap.replace("'" , '')
            snap = snap.replace("," , '')
            
            writer.writerow([date+";"+snap])

            date_index+=5
            snap_index+=5

            # print(date)
            # print(snap)





        
