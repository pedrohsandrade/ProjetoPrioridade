# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-

from definebanco import cursor, conn, sqlite3


class Model(object):


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
        input("Aperte qualquer tecla para prosseguir")

    def cadastraritem(self, item, indice1, indice2, indice3):
        try:
            subsql = "INSERT INTO tabela (item, indice1, indice2, indice3) VALUES ('{}', '{}', '{}', '{}')"
            sql = subsql.format(item, indice1, indice2, indice3)
            cursor.execute(sql)
            conn.commit()
            print("Item Cadastrado\n")
        except sqlite3.OperationalError:
            print('\033[31m' + 'Você precisa de uma tabela' + '\033[0;0m')
        input("Aperte qualquer tecla para prosseguir")

    def atualizaitem(self,item,id):
        try:
            atualizar = (item,id)
            cursor.execute("UPDATE tabela SET item=? WHERE id=?",atualizar)
            conn.commit()
            print("Tarefa atualizada com sucesso")
        except sqlite3.OperationalError:
            print('\033[31m'+'Não foi possível atualizar o item'+'\033[0;0m')
        input("Aperte qualquer tecla para prosseguir")

    def atualizaindice1(self,indice1,id):
        try:
            atualizar = (indice1,id)
            cursor.execute("UPDATE tabela SET indice1=? WHERE id=?",atualizar)
            conn.commit()
            print("Indice1 da tarefa atualizado com sucesso")
        except sqlite3.OperationalError:
            print('\033[31m'+'Não foi possível atualizar o indice1 da tarefa'+'\033[0;0m')
        input("Aperte qualquer tecla para prosseguir")

    def atualizaindice2(self, indice2, id):
        try:
            atualizar = (indice2,id)
            cursor.execute("UPDATE tabela SET indice2=? WHERE id=?",atualizar)
            conn.commit()
            print("Indice2 da tarefa atualizado com sucesso")
        except sqlite3.OperationalError:
            print('\033[31m'+'Não foi possível atualizar o indice2 da tarefa'+'\033[0;0m')
        input("Aperte qualquer tecla para prosseguir")

    def atualizaindice3(self, indice3, id):
        try:
            atualizar = (indice3,id)
            cursor.execute("UPDATE tabela SET indice3=? WHERE id=?",atualizar)
            conn.commit()
            print("Indice3 da tarefa atualizado com sucesso")
        except sqlite3.OperationalError:
            print('\033[31m'+'Não foi possível atualizar o indice3 da tarefa'+'\033[0;0m')
        input("Aperte qualquer tecla para prosseguir")

    def deletaitem(self,id):
        try:
            cursor.execute("DELETE FROM tabela WHERE id=?",(id,))
            conn.commit()
            print("Item deletado")
        except sqlite3.OperationalError:
            print('\033[31m' + 'Não foi possível deletar o item' + '\033[0;0m')
        input("Aperte qualquer tecla para prosseguir")

    def lertabela(self):
        try:
            cursor.execute("SELECT * FROM tabela")
            while True:
                row = cursor.fetchone()
                if row is None:
                    break

                print(row[0], row[1], row [2], row [3],row [4],)
            print("\n")
        except sqlite3.OperationalError:
            print("Tabela nao existe")
        input("Aperte qualquer tecla para prosseguir")

    def exibirprioridade(self):
        cursor.execute("SELECT item, (indice1*1) + (indice2*2) + (indice3*3) AS 'a.ordem' FROM tabela "
                       "ORDER BY 'a.ordem' ASC")
        try:
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                separador = ':'
                print(row[0], separador, row[1])
            print("\n")
        except sqlite3.OperationalError:
            print("Tabela nao existe")
        input("Aperte qualquer tecla para prosseguir")