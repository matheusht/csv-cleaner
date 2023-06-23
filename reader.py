import csv
anterior = ''
with open("./input.csv", 'r',encoding='utf8') as file:

    csvcontent = csv.reader(file)

    with open("./output.csv", 'w',encoding='utf8') as file2:
        writer = csv.writer(file2)
        for row in csvcontent:
            print(row)
            if len(row)>0 and row[3] != '':
                if anterior != row[3]:
                    writer.writerow(row)
            
                anterior = row[3]