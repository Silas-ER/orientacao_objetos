class Conta:
    def __init__(self, agencia, conta, nome, sobrenome, saldo, cheque):
        self.__agencia = agencia
        self.__conta = conta
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__saldo = saldo
        self.__limite = cheque

    @property
    def saldo(self):
        print(self.__saldo)
    
    @property
    def limite(self):
        print(self.__limite)

    @limite.setter
    def limite(self, limite):
       self.__limite = limite

    def saldo_extrato(self):
        print("O saldo atual da conta do titular {} é R$ {}!".format(self.__nome, self.__saldo))
        pass

    def deposito(self, valor):
        self.__saldo += valor
    
    def saque(self, valor):
        if(self.__saldo + self.__limite) <= valor:
            saldo_total = self.__saldo + self.__limite 
            negativado = valor - saldo_total
            print("O valor de R$ {} ultrapassa em R$ {} o valor do seu limite disponivel!".format(valor,negativado))
        self.__saldo -= valor

    def transferencia(self,recebe,valor):
        self.saque(valor)
        recebe.deposito(valor)

   

    #Métodos de leitura dos atributos, os getters
    #Métodos de modifição dos atributos, os setters
    