import os, csv
import re

with open(r'vol_id.csv', 'r') as arquivo_csv: # open csv

    leitor = list(csv.reader(arquivo_csv, delimiter='\n')) # read csv info

    # set inicial var
    volume_id_atual = 'ID ainda inexistente' 
    ano_atual = 0
    mes_atual = 0
    dia_atual = 0
    hora_atual = 0
    minuto_atual = 0
    segundo_atual = 0

    for linha in leitor: # loop to read each line of csv
        
        line = str(linha)
        line = line.replace('"' , '')
        line = line.replace('[' , '')
        line = line.replace(']' , '')
        line = line.replace(' ' , '')
        line = line.replace("'" , '')
        line = line.replace("," , '')

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
            ano = ano.replace('[' , '')
            ano = ano.replace(']' , '')
            ano = ano.replace(' ' , '')
            ano = ano.replace("'" , '')
            ano = ano.replace("," , '')
            ano = int(ano)
            # print(ano)

            mes = list(data[5])+list(data[6])
            mes = str(mes)
            mes = mes.replace('[' , '')
            mes = mes.replace(']' , '')
            mes = mes.replace(' ' , '')
            mes = mes.replace("'" , '')
            mes = mes.replace("," , '')
            mes = int(mes)
            # print(mes)      
            
            dia = list(data[8])+list(data[9])
            dia = str(dia)
            dia = dia.replace('[' , '')
            dia = dia.replace(']' , '')
            dia = dia.replace(' ' , '')
            dia = dia.replace("'" , '')
            dia = dia.replace("," , '')
            dia = int(dia)
            # print(dia)

            hora = list(data[11])+list(data[12])
            hora = str(hora)
            hora = hora.replace('[' , '')
            hora = hora.replace(']' , '')
            hora = hora.replace(' ' , '')
            hora = hora.replace("'" , '')
            hora = hora.replace("," , '')
            hora = int(hora)
            # print(hora)

            minuto = list(data[14])+list(data[15])
            minuto = str(minuto)
            minuto = minuto.replace('[' , '')
            minuto = minuto.replace(']' , '')
            minuto = minuto.replace(' ' , '')
            minuto = minuto.replace("'" , '')
            minuto = minuto.replace("," , '')
            minuto = int(minuto)
            # print(minuto)
              
            segundo = list(data[17])+list(data[18])
            segundo = str(segundo)
            segundo = segundo.replace('[' , '')
            segundo = segundo.replace(']' , '')
            segundo = segundo.replace(' ' , '')
            segundo = segundo.replace("'" , '')
            segundo = segundo.replace("," , '')
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

            


                            



            




        



   
