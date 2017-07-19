def main():
	vetor = []
	
	#ler valores
	for i in range(100):
		vetor.append(float(input()))

	#escrever valores
	for i in range(100):
		if vetor[i] <= 10:
			print('A[%d] = %.1f' % (i, vetor[i]))

if __name__ == '__main__':
	main()