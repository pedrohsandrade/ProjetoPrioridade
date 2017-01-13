# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-

from definebanco import cursor, conn, sqlite3


class Model(object):
    def cadastraritem(self, item, indice1, indice2, indice3):
        try:
            subsql = "INSERT INTO tabela (item, indice1, indice2, indice3) VALUES ('{}', '{}', '{}', '{}')"
            sql = subsql.format(item, indice1, indice2, indice3)
            cursor.execute(sql)
            conn.commit()
            print("Item Cadastrado\n")
        except sqlite3.OperationalError:
            print("Você precisa de uma tabela\n")
        input()

    def criartabela(self):
        try:
            cursor.execute("""CREATE TABLE tabela (id INTEGER PRIMARY KEY, item TEXT,indice1 INTERGER,
                          indice2 INTERGER, indice3 INTERGER)
                      """)
            conn.commit()
            print ("Tabela criada\n")
        except sqlite3.OperationalError:
            print("Tabela ja existe\n")
        input()

    def excluirtabela(self):
        try:
            cursor.execute("DROP TABLE tabela")
            print("Tabela excluida\n")
        except sqlite3.OperationalError:
           print("Não existe tabela para ser excluída")
        input()

    def lertabela(self):
        try:
            cursor.execute("SELECT * FROM tabela ")
            while True:
                row = cursor.fetchone()
                if row == None:
                    break

                print(row[0], row[1], row[2], row[3], row[4])
            print("\n")
        except sqlite3.OperationalError:
            print("Tabela nao existe")
        input()