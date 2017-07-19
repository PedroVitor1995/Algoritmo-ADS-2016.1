"""7. Leia um numero e, a seguir, leia uma lista de numeros ate achar um igual ao primeiro numero lido."""

numero = input('Digite um numero: ')
cont = 0 

while cont < numero:
	print('A lista de numero ate achar um numero igual ao numero digitado eh: %d ') % cont
	cont = cont + 1
print('\nFIM.')
