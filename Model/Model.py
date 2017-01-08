# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor=conn.cursor()

class Model(object):
    def cadastro(self, item, indice1, indice2, indice3):
        try:
            valores = [item, indice1, indice2, indice2]
            sql = 'INSERT INTO projeto VALUES (?,?,?,?)'
            cursor.execute(sql,valores)
            conn.commit()
        except:
            print ("Deu ruim")
    def excluirtabela (self):
        try:
            cursor.execute ("DROP TABLE IF EXISTS projeto")
        except:
            print("Deu ruim")
    def lertabela (self):
        try:
            cursor.execute("""
            SELECT * FROM projeto;
            """)
            for linha in cursor.fetchall():
                print(linha)
            conn.close()
        except:
            print("Deu ruim")