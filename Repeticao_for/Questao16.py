"""16. Leia um numero N, calcule e escreva os N primeiros termos de sequencia de Fibonacci
(0,1,1,2,3,5,8,...). O valor lido para N sempre sera maior ou igual a 2."""

numero_n = input('Digite um numero N: ')

primeiro_termo = 0
segundo_termo = 1

print primeiro_termo
print segundo_termo

for i in range(1, numero_n + 1):

	sequencia_fibonacci = primeiro_termo + segundo_termo

	if numero_n > 2:
		print sequencia_fibonacci
		primeiro_termo = segundo_termo
		segundo_termo = sequencia_fibonacci

