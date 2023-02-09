from decimal import Decimal
from conta import Conta
import random

def calculo_de_limite(pontos):
    limite = 0
    if(pontos >= 0 and pontos <= 250):
        limite = random.uniform(0,500)
    elif(pontos >= 251 and pontos <= 500):
        limite = random.uniform(501,1500)
    else:
        limite = random.uniform(1501,2500)
    return Decimal(limite)

def armazenar(agencia, conta, nome, sobrenome, saldo, cheque):
    contas = {"Agência": agencia, "Conta": conta, "Nome": nome, "Sobrenome": sobrenome, "Saldo": saldo, "Limite": cheque}
    return contas

def sacar(conta, valor):
    conta["Saldo"] -= valor

def depositar(conta, valor):
    conta["Saldo"] += valor

def saldo_extrato(conta):
    print("O saldo atual da conta é R$ {}".format(conta["Saldo"]))

def criar_conta():
    n_agencia = 1339
    print("A agência atual é a {}\n".format(n_agencia))   
    n_conta = int(input("Digite o número da conta: "))
    titular = input("Digite o primeiro nome do titular da conta: ")
    sobrenome_titular = input("Digite o sobrenome do titular da conta: ")
    saldo_inicial = Decimal(input("Digite o valor inicial da conta: R$ ")) 
    score_client = int(input("Digite o valor do score do cliente (entre 0 e 1000): "))
    limite = calculo_de_limite(score_client)
    conta = Conta(n_agencia, n_conta, titular, sobrenome_titular, saldo_inicial, limite)
    print(conta)

