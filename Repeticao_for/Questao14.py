"""14. Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
maior quadrado menor que 38 e 36 (quadrado de 6)."""


from math import sqrt as raiz

numero_n = input('Digite um numero N: ')

valor_n = numero_n
diferenca_raiz = 0

raiz_quadrada = raiz(valor_n)

for i in range(1, numero_n + 1):

	raiz_quadrada_i = raiz(i)

	if raiz_quadrada_i == int(raiz_quadrada_i):
		diferenca_raiz = raiz_quadrada - raiz_quadrada_i 
		if diferenca_raiz < 1:
			quadrado_maior = raiz_quadrada_i ** 2
			quadrado_maior = int(quadrado_maior)
			print('\nO maior quadrado menor que %d eh %d ') % (valor_n,quadrado_maior)