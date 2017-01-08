# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-

import sqlite3

from Model.Model import Model
from View.View import View


class Tabela:
    def Addtabela(self):
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE projeto
                 (item TEXT,indice1 INTERGER,
                  indice2 INTERGER, indice3 INTERGER)
              """)
    def start(self):
        opcao = self.View.start()
        while opcao != 0:
            resultado = self.item(opcao)
            self.View.sucesso(resultado)

            opcao = self.View.menu()
        self.View.finalizar()

    def item(self,opcao):

        if opcao == 1:
            item, indice1, indice2, indice3 = self.View.getItem()
            return self.Model.cadastro(item, indice1, indice2, indice3)
        elif opcao == 2:
            return self.Model.lertabela(self)
        elif opcao == 9:
            return self.Model.excluirtabela(self)

    def __init__(self):
        self.Model = Model()
        self.View = View()



if __name__ == "__main__":
    main = Tabela()
    main.start()