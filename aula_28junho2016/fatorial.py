def fatorial(numero):
	if numero == 0:
		return 1
	else:
		resultado = numero * fatorial(numero - 1)
		return resultado

def main():
	numero = input('Digite um numero: ')
	resposta = fatorial(numero)
	print 'Fatorial de {} eh {}'.format(numero, resposta)
	print 'Fatorial de %d eh %d' % (numero, resposta)

if __name__ == '__main__':
	main()