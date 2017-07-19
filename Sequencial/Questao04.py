#__*__  encoding:utf8 __*__
"""4. Leia o valor do dolar e um valor em dolar, calcule e escreva o equivalente em real."""
def calcula_real(valor_dolar,valor_em_dolar):
	valor_reais = valor_em_dolar * valor_dolar
	return valor_reais
def main():
	valor_dolar = input ('Digite o valor do dolar: ')
	valor_em_dolar = input ('Digite um valor em dolar: ')
	valor_reais = calcula_real(valor_dolar,valor_em_dolar)
	print valor_reais

if __name__ == '__main__':
	main()