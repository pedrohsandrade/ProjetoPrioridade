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

        elif opcao == 4:
            opcao2 = self.View.getopcao2()
            self.atualiza(opcao2)

        elif opcao == 5:
            id = self.View.getId()
            self.Model.deletaitem(id)

        elif opcao == 6:
            self.Model.exibirprioridade()

        elif opcao == 9:
            self.Model.excluirtabela()

    def atualiza(self, opcao2):
        if opcao2 == 1:
            id = self.View.getId()
            item = self.View.getnovoitem()
            self.Model.atualizaitem(item,id)

        elif opcao2 == 2:
            id = self.View.getId()
            item = self.View.getnovoindice()
            self.Model.atualizaindice1(item,id)

        elif opcao2 == 3:
            id = self.View.getId()
            item = self.View.getnovoindice()
            self.Model.atualizaindice2(item,id)

        elif opcao2 == 4:
            id = self.View.getId()
            item = self.View.getnovoindice()
            self.Model.atualizaindice3(item, id)

    def __init__(self):
        self.Model = Model()
        self.View = View()

if __name__ == "__main__":
    main = Projeto()
    main.start()
