"""Leia uma lista de numeros e que para cada numero lido, escreva o proprio numero e a relacao de seus
divisores. (flag numero = 0)."""

while True:
	numero = input('Digite um numero sendo que 0 eh para sair: ')
	cont = numero

	if numero == 0:
		break
	else:
		while cont != 0:
			if(numero > 0 and cont > 0):
				if((numero % cont) == 0):
					print('O numero %d e divisivel por: %d ') % (numero,cont)
				cont = cont - 1
			elif(numero < 0):
				numero = input('Opca de saida invalida! Digite 0 para sair: ')
			else:
				break
print('\nFIM.')

