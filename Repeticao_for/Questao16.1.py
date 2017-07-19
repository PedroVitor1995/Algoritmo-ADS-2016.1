#__*__  encoding:utf8 __*__
"""16. Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2."""
#usando recursividade
def fibonacci(numero_n,anterior1,anterior2):
	if numero_n > 2:
		atual = anterior1 + anterior2
		anterior1 = anterior2
		anterior2 = atual
		numero_n -= 1
		print atual
		fibonacci(numero_n,anterior1,anterior2)
def main():
	numero_n = input('Digite a quantidade de N maior ou igual a 2: ')
	anterior1 = 0
	anterior2 = 1
	if numero_n >= 2:
		print anterior1
		print anterior2
		fibonacci(numero_n,anterior1,anterior2)
	else: 
		print('Numero invalido!')

if __name__ == '__main__':
	main()
