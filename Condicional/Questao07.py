"""7. Leia 3 tres numeros cada numero corresponde a um lado do triangulo, verifique e escreva se os 3
tres numeros formam um triangulo a soma de dois lados nao pode ser menor que o terceiro lado. Se
formam, verifique se formam um triangulo equilatero 3 lados iguais, isosceles 2 lados iguais ou
escaleno 3 lados diferentes. Nao existe lado com tamanho 0 zero."""
def o_triangulo_eh(numero1,numero2,numero3):
	if numero1 > 0 and numero2 > 0 and numero3 > 0 :
		if numero1 + numero2 >= numero3 :
			if numero1 == numero2 and numero1 == numero3 and numero2 == numero3 :
				print ('\nTriangulo equilatero')
			elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3 :
				print ('\nTriangulo isosceles')
			else :
				print ('\nTriangulo escaleno')
		else :
			print ('\nOs lados nao formam um triangulo')
	else :
		print ('\nNao existe triangulo com lado igual a zero ')
def main():
	numero1 = input ('Digite o valor do primeiro lado : ')
	numero2 = input ('\nDigite o valor do segundo lado: ')
	numero3 = input ('\nD|igite o valor do terceiro lado: ')
	o_triangulo_eh(numero1,numero2,numero3)
if __name__ == '__main__':
	main()