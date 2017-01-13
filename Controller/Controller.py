# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-


from Model.Model import Model
from View.View import View


class Projeto:
    def start(self):
        opcao = self.View.start()
        while opcao != 0:
            self.item(opcao)
            opcao = self.View.menu()

        self.View.finalizar()


    def item(self, opcao):

        if opcao == 1:
            self.Model.criartabela()
        elif opcao == 2:
            item, indice1, indice2, indice3 = self.View.getItem()
            self.Model.cadastraritem(item, indice1, indice2, indice3)
        elif opcao == 3:
            self.Model.lertabela()
#            retorno = self.View.retorno()
#            while retorno != 's':
#                retorno = self.View.retorno()
        elif opcao == 9:
            self.Model.excluirtabela()

    def __init__(self):
        self.Model = Model()
        self.View = View()

if __name__ == "__main__":
    main = Projeto()
    main.start()
