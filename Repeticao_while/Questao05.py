"""5. Leia dois numeros X e N. A seguir, escreva o resultado das divisoes de X por N onde, apos cada
divisao, X passa a ter como conteudo o resultado da divisao anterior e N e decrementado de 1 em 1, ate
chegar a 2."""

valor_x = input('Digite o valor de X: ')
valor_n = input('\nDigite o valor de N: ')

print('\nApos cada divisao, X passa ter como conteudo o resultado da divisao anterior ')
print('\nE N eh decrementado de 1 em 1, ate chegar a 2 ')

while valor_x > 0 and valor_n > 0:

	divisao = float(valor_x / valor_n)

	if valor_n < 2:
		break
	else:
		valor_x = divisao
		valor_n = valor_n - 1
		print('\nO resultado da divisao de X por N eh %.2f ') %  divisao

print('\nFIM.')


