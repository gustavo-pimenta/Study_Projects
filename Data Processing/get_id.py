import csv, time

with open('snaps_2012_2015_ID.CSV', 'r') as id_list:

    id_doc = open('ID.txt','r')
    id_from_doc = str(id_doc.read()) 

    leitor = list(csv.reader(id_list, delimiter='\n'))

    index=0
    for line in leitor:

        # print(line)

        id_from_list = str(line)
        id_from_list = id_from_list.replace("\n",'')
        id_from_list = id_from_list.replace('"' , '')
        id_from_list = id_from_list.replace('[' , '')
        id_from_list = id_from_list.replace(']' , '')
        id_from_list = id_from_list.replace(' ' , '')
        id_from_list = id_from_list.replace("'" , '')
        id_from_list = id_from_list.replace("," , '')

        # print(id_from_doc)
        # print(id_from_list)
        # print(id_from_doc==id_from_list)
        # time.sleep(10)
        
        if (str(id_from_doc)==str(id_from_list)):
            doc_write = open('ID.txt','w')

            next_id = str(str(leitor[index+1]))
            next_id = next_id.replace('[' , '')
            next_id = next_id.replace(']' , '')
            next_id = next_id.replace("'" , '')
            doc_write.write(next_id)

            doc_write.close()
            break

        index+=1
    
    id_doc.close()
    
        
        
      