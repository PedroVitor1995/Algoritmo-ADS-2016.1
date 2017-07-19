import teste
import sys


print 'Hello teste2'

print sys.argv

#print 'Soma 4 e 7 = ', teste.soma(4,7)

def alinhado_direita(texto):
	count_spaces = 70 - len(texto)
	print (' ' * count_spaces)+texto

alinhado_direita('Rogerio')
alinhado_direita('Rogerio da Silva')
alinhado_direita('Instituto Federal do Piaui')
