def main():
	valor = int(float(input())*100)

	cedulas = [100, 50, 20, 10, 5, 2]
	moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
	
	print('NOTAS:')
	for cedula in cedulas:
		qtd = valor // (cedula*100)
		valor = valor % int(cedula*100)
		print('%d nota(s) de R$ %.2f' % (qtd, cedula))
	
	
	print('MOEDAS:')
	for moeda in moedas:
		qtd = valor // (moeda*100)
		valor = valor % int(moeda*100)
		print('%d moeda(s) de R$ %.2f' % (qtd, moeda))


if __name__ == '__main__':
	main()