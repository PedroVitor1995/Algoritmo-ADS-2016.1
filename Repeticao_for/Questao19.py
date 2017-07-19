#__*__  encoding:utf8 __*__
def main():
	valor_n = input('Digite o tamanho de N: ')
	Soma = 0
	contador = 0
	for i in range(1,valor_n+1):
		if i % 2 != 0:
			Soma += (i / float(valor_n - contador))
		else:
			Soma -= ((valor_n - contador) / float(i))
		contador += 1
	print Soma

if __name__ == '__main__':
	main()