# _*_ coding: utf-8 _*_

"""6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180º). Se formam,
verifique se formam um triângulo acutângulo (3 ângulos < 90º), retângulo (1 ângulo = 90º) ou
obtusângulo (1 ângulo > 90º). Não existe ângulo com tamanho 0º (zero grau)."""
def eh_angulo(numero1,numero2,numero3,soma_angulos):
	if numero1 != 0 or numero2 != 0 or numero3 != 0 :
		if soma_angulos == 180 :
			if numero1 < 90 and numero2 < 90 and numero3 < 90 :
				print ('\nAcutangulo')
			elif numero1 == 90 or numero2 == 90 or numero3 == 90 :
				print ('\nRetangulo')
			elif  numero1 > 90 or numero2 > 90 or numero3 > 90 :
				print ('\nObtusangulo')
		else :
			print ('\nOs angulos nao formam um triangulo ')
	else :
		print ('\nNao existe angulo com tamanho igual a zero ')

def main():
	numero1 = input ('Digite o primeiro numero corresponde a um angulo interno do triangulo: ')
	numero2 = input ('Digite o segundo numero corresponde a um angulo interno do triangulo: ')
	numero3 = input ('Digite o terceiro numero corresponde a um angulo interno do triangulo: ')

	soma_angulos = numero1 + numero2 + numero3
	eh_angulo(numero1,numero2,numero3,soma_angulos)

if __name__ == '__main__':
	main()



