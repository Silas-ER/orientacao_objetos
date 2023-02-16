from decimal import Decimal
from conta import Conta
from data import Data
from cliente import Cliente
import random

#n_agencia, n_conta, titular, sobrenome_titular, saldo_inicial, limite
datahj = Data(13,2,2023)
datahj.formatacao
conta1 = Conta(1339, 10777, "silas", "eduardo", 1000, 3000)
#conta2 = Conta(1339, 10779, "rodriguez", "santos", 50, 5000)
conta1.saldo
conta1.limite
conta1.limite = 1000
conta1.limite