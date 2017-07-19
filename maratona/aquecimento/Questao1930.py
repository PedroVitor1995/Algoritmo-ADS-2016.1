def main():
	numeros = input().split(' ')
	T1 = int(numeros[0])
	T2 = int(numeros[1])
	T3 = int(numeros[2])
	T4 = int(numeros[3])
	qtd = T1 + T2 + T3 + T4
	qtd_tomadas = qtd - 3
	print(qtd_tomadas)
if __name__ == '__main__':
	main()