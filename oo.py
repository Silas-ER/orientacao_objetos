from decimal import Decimal
from conta import Conta
import random

#n_agencia, n_conta, titular, sobrenome_titular, saldo_inicial, limite

conta = Conta(1339, 10777, "silas", "eduardo", 1000, 3000)
print(conta)
conta2 = Conta(1339, 10779, "rodriguez", "santos", 50, 5000)
print(conta2)
print(conta.nome)
conta.saldo_extrato()