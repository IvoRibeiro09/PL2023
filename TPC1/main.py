# TPC1 de PL;Ivo Ribeiro;A96726
import csv
import matplotlib.pyplot as plt


def menu(dict0, dict1, dict2, dict3, dict4):
    opcao = 0
    opaux = 0
    while opcao != 4:
        opcao = int(input("Selecione uma opçao:\n"
                          "1-Distribuição da doença consuante o sexo;\n"
                          "2-Distribuiçõa da doença pelos diferentes escaloes étarios;\n"
                          "3-Distribuição da doença pelos diferentes niveis de colestrol;\n"
                          "4-sair.\n"))
        if opcao != 4:
            opaux = int(input("1-Tabela\n"
                              "2-Grafico\n"))
        if opaux == 1 and opcao == 1:
            tabSexo(dict0)
        elif opaux == 2 and opcao == 1:
            grafSexo(dict0)
        elif opaux == 1 and opcao == 2:
            tabIdade(dict1, dict2)
        elif opaux == 2 and opcao == 2:
            grafIdade(dict1, dict2)
        elif opaux == 1 and opcao == 3:
            tabColestrol(dict3, dict4)
        elif opaux == 2 and opcao == 3:
            grafColestrol(dict3, dict4)


def grafSexo(dict0):
    width = 0.4
    plt.title('Distribuição da doença consuante o género')
    plt.bar(["Male", "Female"], dict0['doente'], color='orange', width=-width, align='edge')
    plt.ylabel('Unidades')
    plt.bar(["Male", "Female"], dict0['não doente'], color='blue', width=width, align='edge')
    plt.legend(dict0.keys())
    plt.show()


def grafIdade(dict0, dict2):
    width = 2.6
    plt.title('Distribuição da doença consuante os escalões etários')
    plt.bar(dict0.keys(), dict0.values(), color='orange', width=-width, align='edge')
    plt.ylabel('Unidades')
    plt.bar(dict2.keys(), dict2.values(), color='blue', width=width, align='edge')
    plt.ylabel('Idades')
    aux = ['Doentes', 'Não doentes']
    plt.legend(aux)
    plt.show()


def grafColestrol(dict0, dict2):
    width = 3.6
    plt.title('Distribuição da doença consuante os níveis de colestrol')
    plt.bar(dict0.keys(), dict0.values(), color='orange', width=-width, align='edge')
    plt.ylabel('Unidades')
    plt.bar(dict2.keys(), dict2.values(), color='blue', width=width, align='edge')
    plt.ylabel('níveis de colestrol')
    aux = ['Doentes', 'Não doentes']
    plt.legend(aux)
    plt.show()


def tabSexo(dict0):
    print("Distribuição da doença consuante o género")
    print("Género\t\t\tDoentes\t\tNão Doentes")
    print("-----------------------------------------")
    print("Masculino:\t\t%d\t\t\t%d" % (dict0['doente'][0], dict0['não doente'][0]))
    print("Feminino:\t\t%d\t\t\t%d" % (dict0['doente'][1], dict0['não doente'][1]))
    print("-----------------------------------------")


def tabIdade(dict0, dict2):
    print("Distribuição da doença consuante a escalões etários")
    print("Idade\t\t\tDoentes\t\tNão Doentes")
    print("----------------------------------------")
    for chave in dict0.keys():
        print("%d-%d:\t\t\t%d\t\t\t%d" % (chave, chave + 5, dict0[chave], dict2[chave]))
    print("----------------------------------------")


def tabColestrol(dict0, dict2):
    print("Distribuição da doença consuante os níveis de colestrol")
    print("Nível de Colestrol\t\tDoentes\t\tNão Doentes")
    print("------------------------------------------------")
    for chave in dict0.keys():
        print("\t%3d-%3d:\t\t\t%d\t\t\t%d" % (chave, chave + 10, dict0[chave], dict2[chave]))
    print("------------------------------------------------")


if __name__ == '__main__':
    data = []
    dataSexo = {'doente': [0, 0], 'não doente': [0, 0]}
    dataColestrol_doente = {}
    dataColestrol_ndoente = {}
    dataIdade_doente = {}
    dataIdade_ndoente = {}

    try:
        with open('myheart.csv', 'r') as ficheiro:
            conteudo = csv.reader(ficheiro)

            next(conteudo)  # passar a primeira linha à frente
            colestrolmin = 1000
            colestrolmax = 0
            datamin = 1000
            datamax = 0

            for linha in conteudo:
                # validar as linhas do csv
                # guardar no data a idade|sexo|colestrol|tem doença
                if int(linha[0]) > 0 and int(linha[3]) > 0 and (int(linha[5]) == 0 or int(linha[5]) == 1):
                    if int(linha[3]) < colestrolmin:
                        colestrolmin = int(linha[3])
                    if int(linha[3]) > colestrolmin:
                        colestrolmax = int(linha[3])
                    if int(linha[0]) < datamin:
                        datamin = int(linha[0])
                    if int(linha[0]) > datamax:
                        datamax = int(linha[0])
                    dic = {'idade': int(linha[0]), 'sexo': linha[1], 'colestrol': int(linha[3]),
                           'doente': int(linha[5])}
                    data.append(dic)

            while colestrolmin < colestrolmax:
                dataColestrol_doente[colestrolmin] = 0
                dataColestrol_ndoente[colestrolmin] = 0
                colestrolmin += 10

            aux = datamin // 10
            datamin = aux * 10
            while datamin < datamax:
                dataIdade_doente[datamin] = 0
                dataIdade_ndoente[datamin] = 0
                datamin += 5

            for linha in data:
                if linha['sexo'] == 'M' and linha['doente'] == 1:
                    dataSexo['doente'][0] += 1
                elif linha['sexo'] == 'M' and linha['doente'] == 0:
                    dataSexo['não doente'][0] += 1
                elif linha['sexo'] == 'F' and linha['doente'] == 1:
                    dataSexo['doente'][1] += 1
                elif linha['sexo'] == 'F' and linha['doente'] == 0:
                    dataSexo['não doente'][1] += 1
                if linha['doente'] == 1:
                    for chave in dataColestrol_doente.keys():
                        if chave <= linha['colestrol'] < chave + 10:
                            dataColestrol_doente[chave] += 1
                            break
                    for chave in dataIdade_doente.keys():
                        if chave <= linha['idade'] < chave + 5:
                            dataIdade_doente[chave] += 1
                            break
                else:
                    for chave in dataColestrol_ndoente.keys():
                        if chave <= linha['colestrol'] < chave + 10:
                            dataColestrol_ndoente[chave] += 1
                            break
                    for chave in dataIdade_ndoente.keys():
                        if chave <= linha['idade'] < chave + 5:
                            dataIdade_ndoente[chave] += 1
                            break

            menu(dataSexo, dataIdade_doente, dataIdade_ndoente, dataColestrol_doente, dataColestrol_ndoente)
    except Exception as e:
        print(e)