import heapq
import json
import re

def show_os_cinco_maiores(dict1, dict2):
    # mostrar os 5 mais usados
    # nome proprio
    mais_usados = heapq.nlargest(5, frequencia['nomeP'].items(), key=lambda x: x[1])
    print("Os cinco  nomes Propios mais usados são:")
    for i in mais_usados:
        aux = re.split(r'-', i[0])
        print("\t"+aux[0]+" no seculo de "+aux[1]+" num total de: "+str(i[1]))
    # apelido
    apelidos_mais_usados = heapq.nlargest(5, frequencia['apelido'].items(), key=lambda x: x[1])
    print("Os cinco Apelidos mais usados são:")
    for i in apelidos_mais_usados:
        aux = re.split(r'-', i[0])
        print("\t" + aux[0] + " no seculo de " + aux[1] + " num total de: " + str(i[1]))

if __name__ == '__main__':

    try:
        with open('processos.txt', 'r') as ficheiro:
            texto = ficheiro.read()

        frequencia = {
            'ano': {},
            'nomeP': {},
            'apelido': {},
            'parentesco': {}
        }
        frase = "Doc.danificado."
        frase2 = "Em Anexo"

        dados = []

        aux = 0
        for line in re.split(r'\n', texto):
            #eliminar os danificados
            if re.search(frase, line) is None:
                parte = re.split(r' *:: *', line)

                nomesarray = []
                parentesarray = []

                if len(parte) >= 2:
                    #parte 1 data
                    # frequencia por ano segundo elemento da linha AAAA-MM-DD
                    data = re.split(r"-", parte[1])
                    if frequencia['ano'].get(data[0]) is not None:
                        frequencia['ano'][data[0]] += 1
                    else:
                        frequencia['ano'][data[0]] = 1
                    for i in range(2, len(parte)):
                        if len(parte[i]) > 0:
                            pattern = re.compile(r',(\w+(?: \w+)*)\.')
                            pattern2 = re.compile(r'[A-Z][a-z]+(?: [A-Z][a-z]+)+')
                            if len(pattern.findall(parte[i])) > 0:
                                parentes = pattern.findall(parte[i])
                                for j in parentes:
                                    if frequencia['parentesco'].get(j) is not None:
                                        frequencia['parentesco'][j] += 1
                                    else:
                                        frequencia['parentesco'][j] = 1
                                    parentesarray.append(j)
                            if len(pattern2.findall(parte[i])) > 0:
                                nomes = pattern2.findall(parte[i])
                                for j in nomes:
                                    if frequencia['parentesco'].get(j) is None and re.search(frase2, j) is None:
                                        #split nos espaços e guardar a frequencia
                                        nome = re.split(r' ', j)
                                        if frequencia['nomeP'].get(nome[0] +"-"+ data[0][:2]) is not None:
                                            frequencia['nomeP'][nome[0] +"-"+ data[0][:2]] += 1
                                        else:
                                            frequencia['nomeP'][nome[0] +"-"+ data[0][:2]] = 1
                                        if frequencia['apelido'].get(nome[-1] +"-"+ data[0][:2]) is not None:
                                            frequencia['apelido'][nome[-1] +"-"+ data[0][:2]] += 1
                                        else:
                                            frequencia['apelido'][nome[-1] +"-"+ data[0][:2]] = 1
                                        nomesarray.append(j)
                if aux < 20:
                    registo = {
                        'numero': parte[0],
                        'data': parte[1],
                        'nomes': nomesarray,
                        'grau de parentesco': parentesarray
                    }
                    dados.append(registo)
            aux += 1

        #print(frequencia['ano'])
        #print(frequencia['nomeP'])
        #print(frequencia['apelido'])
        #print(frequencia['parentesco'])
        #print(dados)
        show_os_cinco_maiores(frequencia['nomeP'], frequencia['apelido'])

        with open('processos.json', 'w') as f:
            json.dump(dados, f)

    except Exception as e:
        print(e)

    # frequencia por ano segundo elemento da linha AAAA-MM-DD
    # frequencia por nome proprio 3 elemento da linha
    # frequencia por apelido 3 elemento da linha
    # frequancia de parantesco 3 para frente
