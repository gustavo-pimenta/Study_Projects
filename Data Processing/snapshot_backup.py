import csv 
import time
import re
import os

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

loop = 1 # times to repeat
while loop<=10:
    print('\n______________________________LOOP ',loop,'______________________________\n')

    # SCRIPT TO CREATE THE VOLUME WITH THE SNAPSHOT
    print('\nRODANDO O PRIMEIRO SH\n')
    # to run the shell script we can use "os.system()" or "subprocess.Popen()" or "subprocess.call()" or "subprocess.run()"
    os.system('shell1.sh')
    time.sleep(2)

    # SCRIPT TO SAVE THE NEW LIST OF VOLUME ID IN "vol_id.csv"
    print('\nRODANDO O SEGUNDO SH\n')
    os.system('shell2.sh')
    time.sleep(2)
    
    # FIND THE NEWEST VOLUME ID OF THE LIST AND SAVE IN "volume.txt"
    with open(r'vol_id.csv', 'r') as arquivo_csv: # open csv

        read = list(csv.reader(arquivo_csv, delimiter='\n')) # read csv info

        # set inicial var
        volume_id_atual = 'ID ainda inexistente' 
        ano_atual = 0
        mes_atual = 0
        dia_atual = 0
        hora_atual = 0
        minuto_atual = 0
        segundo_atual = 0 

        for linha in read: # loop to read each line of csv
            
            line = str(linha)
            line = limpar(line)

            if (re.search('VolumeId', line, re.IGNORECASE)): # get the line of volume ID
                volume_id = line
                volume_id = volume_id.replace('VolumeId:','')
                # print(volume_id)
            
            if (re.search('CreateTime', line, re.IGNORECASE)): # get the line of date
                data = line
                data = data.replace('CreateTime:','')
                # print(data)

                ano = list(data[0])+list(data[1])+list(data[2])+list(data[3]) 
                ano = str(ano)
                ano = limpar(ano)
                ano = int(ano)
                # print(ano)

                mes = list(data[5])+list(data[6])
                mes = str(mes)
                mes = limpar(mes)
                mes = int(mes)
                # print(mes)      
                
                dia = list(data[8])+list(data[9])
                dia = str(dia)
                dia = limpar(dia)
                dia = int(dia)
                # print(dia)

                hora = list(data[11])+list(data[12])
                hora = str(hora)
                hora = limpar(hora)
                hora = int(hora)
                # print(hora)

                minuto = list(data[14])+list(data[15])
                minuto = str(minuto)
                minuto = limpar(minuto)
                minuto = int(minuto)
                # print(minuto)
                
                segundo = list(data[17])+list(data[18])
                segundo = str(segundo)
                segundo = limpar(segundo)
                segundo = int(segundo)
                # print(segundo)

                
                # test if the current Volume is the newst 
                if ano>ano_atual: 
                    ano_atual = ano
                    mes_atual = mes 
                    dia_atual = dia
                    hora_atual = hora
                    minuto_atual = minuto 
                    segundo_atual = segundo
                    volume_id_atual = volume_id

                elif ano==ano_atual:
                    
                    if mes>mes_atual:
                        ano_atual = ano
                        mes_atual = mes 
                        dia_atual = dia
                        hora_atual = hora
                        minuto_atual = minuto 
                        segundo_atual = segundo
                        volume_id_atual = volume_id

                    elif mes==mes_atual:

                        if dia>dia_atual:
                            ano_atual = ano
                            mes_atual = mes 
                            dia_atual = dia
                            hora_atual = hora
                            minuto_atual = minuto 
                            segundo_atual = segundo
                            volume_id_atual = volume_id
                        
                        elif dia==dia_atual:

                            if hora>hora_atual:
                                ano_atual = ano
                                mes_atual = mes 
                                dia_atual = dia
                                hora_atual = hora
                                minuto_atual = minuto 
                                segundo_atual = segundo
                                volume_id_atual = volume_id
                            
                            elif hora==hora_atual:

                                if minuto>minuto_atual:
                                    ano_atual = ano
                                    mes_atual = mes 
                                    dia_atual = dia
                                    hora_atual = hora
                                    minuto_atual = minuto 
                                    segundo_atual = segundo
                                    volume_id_atual = volume_id
                                
                                elif minuto==minuto_atual:

                                    if segundo>=segundo_atual:
                                        ano_atual = ano
                                        mes_atual = mes 
                                        dia_atual = dia
                                        hora_atual = hora
                                        minuto_atual = minuto 
                                        segundo_atual = segundo
                                        volume_id_atual = volume_id

                                    else:
                                        pass

        # Data output with the newst Volume and your date
        # print(ano_atual)
        # print(mes_atual)
        # print(dia_atual)
        # print(hora_atual)
        # print(minuto_atual)
        # print(segundo_atual)
        # print(volume_id_atual)

        doc = open(r'volume.txt','w')
        doc.write(volume_id_atual)
        doc.close()
        arquivo_csv.close()
        print('\nvolume.txt ATUALIZADO\n')
    time.sleep(2) # time interval

    # SCRIPT TO CONECT THE VOLUME AT THE VM
    print('\nRODANDO O TERCEIRO SH\n')
    os.system('shell3.sh')
    time.sleep(2)

    # GET THE NEXT SNAPSHOT ID OF THE LIST AND SAVE IN "ID.txt"
    with open('snaps_2012_2015_ID.CSV', 'r') as id_list: # open snapshot ID list

        id_doc = open('ID.txt','r')
        id_from_doc = str(id_doc.read()) 
        leitor = list(csv.reader(id_list, delimiter='\n'))

        index=0
        for line in leitor: # read the lines of the list

            id_from_list = str(line)
            id_from_list = limpar(id_from_list)
            
            if (str(id_from_doc)==str(id_from_list)): # find the current ID inside the list
                doc = open('ID.txt','w')

                next_id = leitor[index+1] # select the next ID of the list
                next_id = limpar(next_id)
                
                doc.write(next_id) # write the next ID in "ID.txt"
                doc.close()

                break # break the loop after find and write ID

            index+=1
        
        id_doc.close() # close ID.txt
        id_list.close() # close the snapshot ID list
        print('\nID.txt ATUALIZADO\n')
    time.sleep(2) # time interval

    loop+=1
        


    