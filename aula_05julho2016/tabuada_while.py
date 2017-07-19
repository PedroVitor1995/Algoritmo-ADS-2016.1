def principal():
	numero = input('Numero: ')
	inicio = input('Inicio: ')
	tabuada(numero, inicio)

def tabuada(numero, inicio):
	while inicio <= 10:
		print "{} x {} = {}".format(numero,inicio,numero * inicio)
		inicio = inicio + 1

if __name__ == '__main__':
	principal()