"""19. Leia a altura em metros e peso em Kg de uma pessoa, em seguida calcule o indice de massa corporea
IMC = peso / altura ** 2. Ao final, escreva se a pessoa esta com peso normal IMC abaixo de 25, obeso
IMC entre 25 e 30 ou obesidade morbida IMC acima de 30."""
def main():
	altura = input ('Digite a altura de uma pessoa em metros: ')
	peso = input ('\nDigite o peso de uma pessoa em kg: ')

	IMC = float(peso / float(altura ** 2))

	if IMC < 25 :
		print ('\nNormal')
	elif IMC >= 25 and IMC <= 30 :
		print ('\nObeso')
	elif IMC > 30 :
		print ('\nObesidade morbida')
if __name__ == '__main__':
	main()
