"""2. Leia 2 (dois) numeros, calcule e escreva o mmc (minimo multiplo comum) entre os numeros lidos."""

while True:

	numero1 = input('\nDigite o primeiro numero sendo 0 para sair: ')

	if numero1 == 0:
		break
	else:
		numero2 = input('\nDigite o segundo numero: ')
		valor_numero1 = numero1
		valor_numero2 = numero2 

		resto = None 

		while resto != 0:
			resto = valor_numero1 % valor_numero2
			valor_numero1 = valor_numero2
			valor_numero2 = resto
			resultado = numero1 * numero2 / valor_numero1

			print('\nO minimo multiplo comum entre %d e %d eh %d ') % (numero1,numero2,resultado)

