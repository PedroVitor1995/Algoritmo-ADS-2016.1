"""30. Escreva um algoritmo que leia o nome de um produto, o preco e a quantidade comprada. Escreva o
nome do produto comprado e o valor total a ser pago, considerando que sao oferecidos descontos pelo
numero de unidades compradas, segundo a tabela abaixo: FLAG: nome do produto = FIM.
a. Ate 10 unidades: valor total
b. de 11 a 20 unidades: 10%  de desconto
c. de 21 a 50 unidades: 20%  de desconto
d. acima de 50 unidades: 25%  de desconto"""
def main():
	print('\nPara ganhar descontos so comprando acima de 10 unidades')
	while  True:
		nome_produto = raw_input('\nDigite o nome de um produto comprado sendo FIM ou fim para sair: ')
		if nome_produto == 'FIM' or nome_produto == 'fim':
			break
		else:
			preco_produto = input('\nDigite o preco de um produto: ')
			quantidade_comprada = input('\nDigite a quantidade comprada: ')

			valor_a_pagar = preco_produto * quantidade_comprada

			valor_a_pagar = float(valor_a_pagar)

			if quantidade_comprada <= 10:
				print('\nA compra nao tem desconto porque foram compradas menos de 10 unidades ')
				print('\nO valor a ser pago por %d %s eh %.2f reais') % (quantidade_comprada,nome_produto,valor_a_pagar)
			elif quantidade_comprada >= 11 and quantidade_comprada <= 20:
				valor_a_pagar_desconto10 = valor_a_pagar - (valor_a_pagar * 10) / 100
				print('\nA conta tera desconto de 10 % ')
				print('\nO valor a ser pago por %d %s eh %.2f reais') % (quantidade_comprada,nome_produto,valor_a_pagar_desconto10)
			elif quantidade_comprada >= 21 and quantidade_comprada <= 50:
				valor_a_pagar_desconto20 = valor_a_pagar - (valor_a_pagar * 20) / 100
				print('\nA conta tera desconto de 20 % ')
				print('\nO valor a ser pago por %d %s eh %.2f reais') % (quantidade_comprada,nome_produto,valor_a_pagar_desconto20)
			else:
				valor_a_pagar_desconto25 = valor_a_pagar - (valor_a_pagar * 25) / 100
				print('\nA conta tera desconto de 25 % ')
				print('\nO valor a ser pago por %d %s eh %.2f reais') % (quantidade_comprada,nome_produto,valor_a_pagar_desconto25)
	print('\nFIM')
if __name__ == '__main__':
	main()

	

		