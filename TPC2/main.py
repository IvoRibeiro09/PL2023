# This is a sample Python script.
import sys

lista = []

if __name__ == '__main__':
   lista = list(map(str, sys.stdin.readline().split()))
   soma = 0
   count = 0
   for valor in lista:
      if(valor.lower() == "off"): count = 1
      elif (valor.lower() == "on"): count = 0
      elif (valor.lower() == "="): print(soma)
      if (count == 0 and valor.isdigit()): soma += int(valor)


