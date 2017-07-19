from math import sqrt

def main():
	x1, y1 = input('X1: '), input('Y1: ')
	x2, y2 = input('X2: '), input('Y2: ')

	distancia = distancia_pontos(x1, y1, x2, y2)

	print 'Distancia = %.4f ' % distancia


def distancia_pontos(x1, y1, x2, y2):
	distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return distancia


if __name__ == '__main__':
	main()