import re
import sys
import json

def media(lista):
    return somar(lista)/len(lista)

def somar(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def convertjson(lista):
    with open('output.json', 'w') as arquivo:
        json.dump(lista, arquivo, indent=5, ensure_ascii=False)

if __name__ == '__main__':

    lista = []
    dict = {}
    onleitura = 0
    pattern = r'(\w+)\{(\d+),(\d+)\}:*:*((\w+))*'
    operation = ""

    try:
        with open(sys.argv[1], 'r') as ficheiro:
            conteudo = ficheiro.read()

        linha = re.split(r'\n', conteudo)
        for elemento in re.split(r',(?![\d,]+})', linha[0]):
            if re.search(pattern, elemento) and onleitura == 0:
                match = re.search(pattern, elemento)
                numero = match.group(3)
                if match.group(4):
                    operation = match.group(4)
                onleitura = int(numero)
                dict[elemento] = ""
            elif onleitura > 0:
                onleitura -= 1
            else:
                dict[elemento] = ""
        print(dict)

        chaves = list(dict.keys())
        for i in range(1, len(linha)):
            dict_aux = {}
            info = re.split(r',', linha[i])
            dataaux = []
            aux = 0
            for j in range(0, len(info)):
                if onleitura > 0:
                    if len(info[j]) > 0:
                        dataaux.append(int(info[j]))
                    onleitura -= 1
                    if onleitura == 0:
                        #ver se ha sum se houver fazer a operaçao
                        if operation == "sum":
                            dict[chaves[aux]] = somar(dataaux)
                        elif operation == "media":
                            dict[chaves[aux]] = media(dataaux)
                        else:
                            dict[chaves[aux]] = dataaux
                        dict[re.search(pattern, chaves[aux]).group(1)] = dict.pop(chaves[aux])
                elif re.search(pattern, chaves[j]):
                    numero = int(re.search(pattern, chaves[j]).group(3))
                    onleitura = numero - 1
                    dataaux.append(int(info[j]))
                    aux = j
                else:
                    dict[chaves[j]] = info[j]
            dict_aux.update(dict)
            lista.append(dict_aux)
        print(lista)

        convertjson(lista)

    except Exception as e:
        print(e)