def main():
	qtd_elementos = input('Qtd: ')
	print 0, 1,
	fibonacci(0, 1, qtd_elementos)

def fibonacci(anterior1, anterior2, contador):
	if contador <= 2:
		print 'FIM.'
	else:
		print anterior1 + anterior2,
		fibonacci(anterior2, anterior1 + anterior2, contador - 1)

if __name__ == '__main__':
	main()