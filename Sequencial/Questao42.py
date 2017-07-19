from math import sqrt as raiz
def main():
	print ('Ponto 1')
	x1 = input ('X1: ')
	y1 = input ('Y1: ')
	print ('\nPonto 2')
	x2 = input ('X2: ')
	y2 = input ('Y2: ')

	distancia = raiz ((x2 - x1) ** 2  +  (y2 - y1) ** 2)

	print distancia
if __name__ == '__main__':
	main()