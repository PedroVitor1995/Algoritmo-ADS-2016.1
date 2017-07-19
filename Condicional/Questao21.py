"""21. Realize arredondamentos de numeros utilizando a regra usual da matematica: se a parte fracionaria for
maior do que ou igual a 0,5, o numero e arredondado para o inteiro imediatamente superior, caso
contrario, e arredondado para o inteiro imediatamente inferior."""

numero = input('Digite um numero: ')

resto_numero = numero - int(numero) 


if resto_numero >= 0.5:
	numero_arredondado = numero + 1
	print('O numero arredondado eh %d') % numero_arredondado
else:
	numero_arredondado = numero
	print('O numero arredondado eh %d') % numero_arredondado