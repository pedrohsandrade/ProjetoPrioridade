# Projeto Prioridade
# Por pedrohsandrade
# -*- coding: utf-8 -*-

class View:
    def start(self):
        print("Bem vindo ao Projeto Prioridade\n")
        return self.menu()

    def menu(self):
        print("1 - Cadastrar item")
        print("2 - Visualizar lista")
        print("9 - Excluir tabela")
        print("0 - Finalizar")


        return int(input("\nDigite a opção: "))

    def getItem(self):
        print("\nDigite o item e os indices")

        item = str(input("O item: "))
        indice1 = int(input("O primeiro indice: "))
        indice2 = int(input("O segundo indice: "))
        indice3 = int(input("O terceiro indice: "))

        return item, indice1, indice2, indice3

    def sucesso(self, item, indice1, indice2, indice3):
        print ("O item %s foi cadastrado com sucesso, com os seguintes indices:\n"
               "Indice 1: %d"
               "Indice 2: %d"
               "Indice 3: %d" % item, indice1, indice2, indice3)

    def finalizar(self):
        print ("Programa finalizado!")
