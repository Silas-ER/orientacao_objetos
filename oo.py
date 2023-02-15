from decimal import Decimal
from conta import Conta
from data import Data
from cliente import Cliente
import random

#n_agencia, n_conta, titular, sobrenome_titular, saldo_inicial, limite
datahj = Data(13,2,2023)
datahj.formatacao()
conta = Conta(1339, 10777, "silas", "eduardo", 1000, 3000)
conta2 = Conta(1339, 10779, "rodriguez", "santos", 50, 5000)
conta.saldo_extrato()
conta2.saldo_extrato()
v = 200
conta.transferencia(conta2,v)
conta.saldo_extrato()
conta2.saldo_extrato()