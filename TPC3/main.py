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

        frase = "Doc.danificado"

        for linha in texto.split("\n"):
            i = 0
            if frase in linha:
                j = 3
                #print("ERROR")
            else:
                for elemento in linha.split("::"):
                    if i == 1:
                        ano = elemento.split("-")
                        if frequencia['ano'].get(ano[0]) is not None:
                            frequencia['ano'][ano[0]] += 1
                        else:
                            frequencia['ano'][ano[0]] = 1
                    elif i > 1:
                        nomes = elemento.split(",")
                        nome = nomes[0].split(" ")

                        if frequencia['nomeP'].get(nome[0]) is not None:
                            frequencia['nomeP'][nome[0]] += 1
                        else:
                            frequencia['nomeP'][nome[0]] = 1

                        if frequencia['apelido'].get(nome[-1]) is not None:
                            frequencia['apelido'][nome[-1]] += 1
                        else:
                            frequencia['apelido'][nome[-1]] = 1

                        if len(nomes) > 1 and nomes[1] is not None:
                            parente = nomes[1].split(".")
                            if frequencia['parentesco'].get(parente[0]) is not None:
                                frequencia['parentesco'][parente[0]] += 1
                            else:
                                frequencia['parentesco'][parente[0]] = 1
                    i += 1
        print(frequencia['ano'])
        print(frequencia['nomeP'])
        print(frequencia['apelido'])
        print(frequencia['parentesco'])

    except Exception as e:
        print(e)

    # frequencia por ano segundo elemento da linha AAAA-MM-DD
    # frequencia por nome proprio 3 elemento da linha
    # frequencia por apelido 3 elemento da linha
    # frequancia de parantesco 3 para frente
