#__*__  encoding:utf8 __*__
"""6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)"""
def calcula_velocidade(velocidade):
	velocidade_total = velocidade / 3.6
	return velocidade_total
def main():
	velocidade = input ('Digite a velocidade em km/h: ')
	velocidade_total = calcula_velocidade(velocidade)
	print velocidade_total
if __name__ == '__main__':
	main()