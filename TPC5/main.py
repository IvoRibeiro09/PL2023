import os
import re


def devolverSaldo(saldo):
    euro, cent = divmod(saldo, 1)
    print("troco: " + str(int(euro)) + "e" + str(int(cent * 100)) + "c; Volte sempre!")
    return 0


def inserirNumero(saldo):
    print("Insira o numero de telefone.")
    num = input()
    custo = 0
    tipo = ""
    if re.match(r'(641|601)[0-9]{6}', num):
        print("Numero invalido...\nChamada Bloqueada.")
        return -1
    elif re.match(r'00[0-9]{7}', num):
        custo = 1.5
        tipo = "Internacional"
    elif re.match(r'2[0-9]{8}', num):
        custo = 0.25
        tipo = "Nacional"
    elif re.match(r'800[0-9]{6}', num):
        custo = 0
        tipo = "Chamada Verde"
    elif re.match(r'808[0-9]{6}', num):
        custo = 0.1
        tipo = "Chamada Azul"
    elif re.match(r'[0-9]{9}', num):
        custo = 0.5
        tipo = "Normal"
    else:
        print("Numero invalido...")
        return -1
    if saldo >= custo:
        print("Chamada " + tipo + " iniciada")
        saldo -= custo
        return saldo
    else:
        print("Saldo insuficiente\nSeu saldo: " + str(saldo) + ", saldo necessario " + str(custo))
        return -1


def moedaValida(moeda):
    # MOEDA 10c, 20c, 50c, 1e, 2e.
    if moeda == "10c":
        return 0.10
    elif moeda == "20c":
        return 0.20
    elif moeda == "50c":
        return 0.50
    elif moeda == "1e":
        return 1
    elif moeda == "2e":
        return 2
    elif re.search(r'[A-z0-9]+', moeda):
        return 0
    else:
        return -1


def inserirSaldo(saldo):
    print("Insira as moedas:")
    moeda = input()
    while (moedaValida(moeda) >= 0):
        if moedaValida(moeda) == 0:
            print("Moeda invalida: " + moeda)
        else:
            saldo += moedaValida(moeda)
        moeda = input()
    return saldo


def menu(estados):
    #os.system('clear' if os.name == 'nt' else 'clear') #limpar o terminal
    if estados == 2:
        print("1- levantar o telefone;")
    if estados == 1 or estados == 2:
        print("2- inserir moedas;")
    if estados == 1:
        print("3- Escolher numero;")
    if estados == 1 or estados == 3:
        print("4- Pousar o telefone;")
        print("5- Abortar operação;")
    opcoesValidasE1 = [2, 3, 4, 5]
    opcoesValidasE2 = [1, 2]
    opcoesValidasE3 = [4, 5]
    opcao = input("Escolha uma opção: ")
    if estados == 1:
        while opcao not in str(opcoesValidasE1):
            opcao = input("Opção inválida. Escolha uma opção: ")
    elif estados == 2:
        while opcao not in str(opcoesValidasE2):
            opcao = input("Opção inválida. Escolha uma opção: ")
    else:
        while opcao not in str(opcoesValidasE3):
            opcao = input("Opção inválida. Escolha uma opção: ")
    return int(opcao)


if __name__ == '__main__':

    estado = 2
    saldo = 0.00
    # 1 levantar telefone
    # 2 pousar telemovel
    # 3 em chamada

    while True:
        opcao = int(menu(estado))
        if opcao == 1:
            estado = 1
        elif opcao == 2:
            saldo = inserirSaldo(saldo)
        elif opcao == 3:
            troco = inserirNumero(saldo)
            if saldo > 0:
                saldo = troco
                estado = 3
        elif opcao == 4:
            estado = 2
            saldo = devolverSaldo(saldo)
        elif opcao == 5:
            estado = 2
            saldo = devolverSaldo(saldo)
        else:
            print("Opção invalida")
