# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-


class View:
    def start(self):
        print("Bem vindo ao Projeto Prioridade\n")
        return self.menu()

    def menu(self):
        print("1 - Criar tabela")
        print("2 - Cadastrar item")
        print("3 - Visualizar lista")
        print("4 - Atualizar item")
        print("9 - Excluir tabela")
        print("0 - Finalizar")
        return int(input("\nDigite a opção: "))

    def getItem(self):
        print("\nDigite o item e os indices")

        item = (input("O item: "))
        indice1 = int(input("O primeiro indice: "))
        indice2 = int(input("O segundo indice: "))
        indice3 = int(input("O terceiro indice: "))
        return item, indice1, indice2, indice3

    def getopcao2(self):
        print("1 - Atualizar a tarefa")
        print("2 - Atualizar o Indice 1")
        print("3 - Atualizar o Indice 2")
        print("4 - Atualziar o Indice 3")
        return int(input("\nDigite a opção: "))

    def getId(self):
        return int(input("\nDigite o Id: "))

    def getnovoitem(self):
        return input("\nDigite o novo item: ")

    def getnovoindice(self):
        return int(input("\nDigite o novo indice: "))

    def finalizar(self):
        print("Programa finalizado!\n")