import csv
anterior = []
with open("./input.csv", 'r',encoding='utf8') as file:

    csvcontent = csv.reader(file)

    with open("./output.csv", 'w',encoding='utf8') as file2:
        writer = csv.writer(file2)
        for row in csvcontent:
            if len(row)>0 and row[3] != '':
                if row[3] not in anterior:
                    writer.writerow(row)
            
                anterior.append(row[3])
print(anterior)