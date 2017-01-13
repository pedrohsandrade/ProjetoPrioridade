# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect("bancodedados.db")
cursor = conn.cursor()
class encerra():
    def encerraconn(self):
        conn.close()

try:
    with conn:
        cursor.execute("""CREATE TABLE tabela (id INTEGER PRIMARY KEY, item TEXT,indice1 INTERGER,
                          indice2 INTERGER, indice3 INTERGER)
                      """)
        cursor.execute("INSERT INTO tabela (item, indice1, indice2, indice3) VALUES ('processo de manutenção',1,1,1)")
        cursor.execute("INSERT INTO tabela (item, indice1, indice2, indice3) VALUES ('processo de instalação',1,1,2)")
        cursor.execute("INSERT INTO tabela (item, indice1, indice2, indice3) VALUES ('processo de mudança de endereço',1,2,1)")
        cursor.execute("INSERT INTO tabela (item, indice1, indice2, indice3) VALUES ('processo de mudança de comodo',2,1,2)")
except sqlite3.OperationalError:
    pass
