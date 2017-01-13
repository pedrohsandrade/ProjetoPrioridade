import sqlite3
import sys
import time
con = sqlite3.connect("teste.db")
cursor = con.cursor()
"""
sql = 'CREATE TABLE tabela (item TEXT,indice1 INTERGER,indice2 INTERGER, indice3 INTERGER)'
cursor.execute(sql)
con.commit()
"""
item = "pedro"
indice1 = 2
indice2 = 1
indice3 = 8
valores = (item, indice1, indice2, indice3)

subsql = "INSERT INTO tabela (item, indice1, indice2, indice3) VALUES ('{}')"
sql = subsql.format(valores)

cursor.executemany(sql,valores)
con.commit()
#time.sleep(3)

cursor.execute("SELECT * FROM tabela")

while True:
    row = cursor.fetchone()
    if row == None:
        break
    print (row [0], row [1], row [2], row [3])
con.close()
"""
last = cursor.lastrowid
print ("The last Id of the inserted row is %d" % last)
"""

"""
NÂO FUNCIONA DÀ O ERRO tuple indices must be integers or slices, not str

while True:
    con.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM fornecedor ORDER BY indice3")
    rows = cursor.fetchall()
    for row in rows:
        print ("%d" (row["indice3"]))
"""
"""
teste ="dwlkdsldj"
teste2 = item
with con:
    cursor.execute("UPDATE fornecedor SET item=? WHERE indice2 = ?", (teste, teste2))
    con.commit()
# print ("Number of rows updated: %d" % cursor.rowcount)
"""

"""
cursor.execute("SELECT * FROM fornecedor ORDER BY indice3")


while True:
    row = cursor.fetchone()
    if row == None:
        break
    print (row [0], row [1], row [2], row [3])
#con.close()
"""