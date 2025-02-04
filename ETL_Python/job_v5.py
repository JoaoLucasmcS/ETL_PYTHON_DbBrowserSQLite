import csv
import sqlite3

def removeponto(valor):
    return int(round(float(valor.replace('.', '')), 0))

def funcstatuspreco(valor):
    if int(valor) >= 15:
        return 'Caro'
    else:
        return 'Barato'

with open ('producao_alimentos.csv', 'r') as file:

    reader = csv.reader(file)

    next(reader)

    conn = sqlite3.connect('dsadb.db')

    conn.execute('DROP TABLE IF EXISTS producao')

    conn.execute('''CREATE TABLE producao (
                 produto TEXT,
                 quantidade INTEGER,
                 preco_medio REAL,
                 receita_total INTEGER,
                 margem_lucro REAL,
                 status_preco TEXT
                ) ''')
    
    for row in reader:
        if int(row[1]) > 10:

            row[3] = removeponto(row[3])
            

            margemlucro = round((row[3] / float(row[1])) - float(row[2]), 2)
            status_preco = funcstatuspreco(row[2])

            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro, status_preco) VALUES (?, ?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margemlucro, status_preco))


    conn.commit()
    conn.close()

print("Job concluído com sucesso")
                


