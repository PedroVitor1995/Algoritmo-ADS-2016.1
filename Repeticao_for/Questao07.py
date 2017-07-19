"""7. Leia um numero N, some todos os numeros inteiros entre 1 e N e escreva o resultado obtido."""

numero_n = input('Digite uum numero N: ')

for i in range(1, numero_n):
	
	soma_numeros = numero_n * (numero_n + 1) / 2
	
	if i == numero_n - 1:
		print('\nA soma de todos os numero entre 1 e %d eh %d ') % (numero_n,soma_numeros)