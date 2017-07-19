#__*__  encoding:utf8 __*__
"""16. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
Até 5 Kg Acima de 5 Kg
File R$ 4,90 por Kg R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
Picanha R$ 6,90 por Kg R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
cliente receberá ainda um desconto de 5%  sobre o total a compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar."""
def main():
	tipo_carne = raw_input('Digite o tipo de carne: ')
	quantidade_carne = input('Digite a quantidade de carne: ')
	tipo_pagamento = raw_input('Digite o tipo de pagamento cartao ou dinheiro: ')
	print('                              Cupom Fiscal                      \n')
	print('                Hipermecado Tabajara                            \n')
	preco_total_desconto = 0
	preco_total_sem_desconto = 0
	desconto = 0
	if tipo_pagamento == 'cartao':
		print('            A compra teve descontos\n')
		if tipo_carne == 'File' or tipo_carne == 'file':
			if quantidade_carne <= 5:
				preco_total_sem_desconto = quantidade_carne * 4.9
			elif quantidade_carne > 5:
				preco_total_sem_desconto = quantidade_carne * 5.8
			desconto = preco_total_sem_desconto * 0.05
			preco_total_desconto = preco_total_sem_desconto - desconto
			print('    Tipo de carne comprada %s') % tipo_carne
			print('    A quantidade de comprada %.2f') % quantidade_carne
			print('    O preco total %.2f') % preco_total_sem_desconto
			print('    O tipo de pagamento %s') % tipo_pagamento
			print('    O valor do desconto %.2f') % desconto
			print('    O total a pagar eh %.2f ') % preco_total_desconto
		elif tipo_carne == 'Alcatra' or tipo_carne == 'alcatra':
			if quantidade_carne <= 5:
				preco_total_sem_desconto = quantidade_carne * 5.9
			elif quantidade_carne > 5:
				preco_total_sem_desconto = quantidade_carne * 6.8
			desconto = preco_total_sem_desconto * 0.05
			preco_total_desconto = preco_total_sem_desconto - desconto
			print('    Tipo de carne comprada %s') % tipo_carne
			print('    A quantidade de comprada %.2f') % quantidade_carne
			print('    O preco total %.2f') % preco_total_sem_desconto
			print('    O tipo de pagamento %s') % tipo_pagamento
			print('    O valor do desconto %.2f') % desconto
			print('    O total a pagar eh %.2f ') % preco_total_desconto
		elif tipo_carne == 'Picanha' or tipo_carne == 'picanha':
			if quantidade_carne <= 5:
				preco_total_desconto = quantidade_carne * 5.9
			elif quantidade_carne > 5:
				preco_total_sem_desconto = quantidade_carne * 6.8
			desconto = preco_total_sem_desconto * 0.05
			preco_total_desconto = preco_total - desconto
			print('    Tipo de carne comprada %s') % tipo_carne
			print('    A quantidade de comprada %.2f') % quantidade_carne
			print('    O preco total %.2f') % preco_total_sem_desconto
			print('    O tipo de pagamento %s') % tipo_pagamento
			print('    O valor do desconto %.2f') % desconto
			print('    O total a pagar eh %.2f ') % preco_total_desconto
	elif tipo_pagamento == 'dinheiro':
		print('            A compra nao teve descontos\n')
		if tipo_carne == 'File' or tipo_carne == 'file':
			if quantidade_carne <= 5:
				preco_total_sem_desconto = quantidade_carne * 4.9
			elif quantidade_carne > 5:
				preco_total_sem_desconto = quantidade_carne * 5.8
			print('    Tipo de carne comprada %s') % tipo_carne
			print('    A quantidade de comprada %.2f') % quantidade_carne
			print('    O preco total %.2f') % preco_total_sem_desconto
			print('    O tipo de pagamento %s') % tipo_pagamento
			print('    O total a pagar eh %.2f ') % preco_total_sem_desconto
		elif tipo_carne == 'Alcatra' or tipo_carne == 'alcatra':
			if quantidade_carne <= 5:
				preco_total_sem_desconto = quantidade_carne * 5.9
			elif quantidade_carne > 5:
				preco_total_sem_desconto = quantidade_carne * 6.8
			print('    Tipo de carne comprada %s') % tipo_carne
			print('    A quantidade de comprada %.2f') % quantidade_carne
			print('    O preco total %.2f') % preco_total_sem_desconto
			print('    O tipo de pagamento %s') % tipo_pagamento
			print('    O total a pagar eh %.2f ') % preco_total_sem_desconto
		elif tipo_carne == 'Picanha' or tipo_carne == 'picanha':
			if quantidade_carne <= 5:
				preco_total_sem_desconto = quantidade_carne * 5.9
			elif quantidade_carne > 5:
				preco_total_sem_desconto = quantidade_carne * 6.8
			print('    Tipo de carne comprada %s') % tipo_carne
			print('    A quantidade de comprada %.2f') % quantidade_carne
			print('    O preco total %.2f') % preco_total_sem_desconto
			print('    O tipo de pagamento %s') % tipo_pagamento
			print('    O total a pagar eh %.2f ') % preco_total_sem_desconto


if __name__ == '__main__':
	main()