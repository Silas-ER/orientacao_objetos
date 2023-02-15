class Conta:
    def __init__(self, agencia, conta, nome, sobrenome, saldo, cheque):
        self.__agencia = agencia
        self.__conta = conta
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__saldo = saldo
        self.__cheque = cheque
    
    def saldo_extrato(self):
        print("O saldo atual da conta do titular {} é R$ {}!".format(self.__nome, self.__saldo))
        pass

    def deposito(self, valor):
        self.__saldo += valor
    
    def saque(self, valor):
        self.__saldo -= valor

    def transferencia(self,recebe,valor):
        self.saque(valor)
        recebe.deposito(valor)

    def set_limite(self, limite):
        self.__limite = limite