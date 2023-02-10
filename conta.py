class Conta:
    def __init__(self, agencia, conta, nome, sobrenome, saldo, cheque):
        self.agencia = agencia
        self.conta = conta
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo
        self.cheque = cheque
    
    def saldo_extrato(self):
        print("O saldo atual da conta do titular {} é R$ {}".format(self.nome, self.saldo))
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        self.saldo -= valor