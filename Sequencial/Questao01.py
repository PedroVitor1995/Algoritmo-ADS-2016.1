#__*__  encoding:utf8 __*__
"""1. Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)"""
def calcula_velocidade(velocidade):
	velocidade_total = velocidade * 3.6
	return velocidade_total
def main():
	velocidade = input ('Digite a velocidade em m/s: ')
	velocidade_total = 0
	velocidade_total = calcula_velocidade(velocidade)
	print velocidade_total

if __name__ == '__main__':
	main()