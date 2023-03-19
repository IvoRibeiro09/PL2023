import sys
import re

if __name__ == '__main__':
    aux = sys.stdin.readline()
    linha = "on" + aux.strip() + "off"

    #linha = "on93--28h=gi4923 off847--38onn48374off"
    soma = 0

    matches = re.findall(r'[Oo][Nn]([\w=\- ]*?)[Oo][Ff][Ff]', linha)
    #print(matches)
    for valid in matches:
        digits = re.findall(r'-?\d|=', valid)
        #print(digits)
        for valor in digits:
            if valor == "=":
                print("Valor da soma: "+str(soma))
            else:
                soma += int(valor)
