#__*__  encoding:utf8 __*__
def main():
	valor_n = input('Digite o valor de N:')
	Soma = 0
	for i in range(1,valor_n+1):
		Soma = Soma + float(1 / float(i))
	print Soma	
if __name__ == '__main__':
	main()
