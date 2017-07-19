"""
    Numero pares entre 1 e N
"""
def  main():
	qtd = input('N: ')
	for i in range(2, qtd+1, 2):
		print i

if __name__ == '__main__':
	main()