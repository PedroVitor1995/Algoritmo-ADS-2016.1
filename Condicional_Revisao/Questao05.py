#__*__  encoding:utf8 __*__
"""5. Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
sempre pelo mais barato."""
def main():
	preco_produto1 = input('Digite o preco do primeiro produto: ')
	preco_produto2 = input('Digite o preco do segundo produto: ')
	preco_produto3 = input('Digite o preco do terceiro produto: ')
	if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
		print('O produto a ser comprado eh o produto 1')
	elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
		print('O produto a ser comprado eh o produto 2')
	else:
		print('O produto a ser comprado eh o produto 3')


if __name__ == '__main__':
	main()