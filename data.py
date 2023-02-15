class Data:
    def __init__(self,dia,mes,ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formatacao(self):
        print("O dia de hoje é {}/{}/{}".format(self.__dia,self.__mes,self.__ano))