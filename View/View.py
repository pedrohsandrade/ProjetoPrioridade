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

    def finalizar(self):
        print("Programa finalizado!\n")