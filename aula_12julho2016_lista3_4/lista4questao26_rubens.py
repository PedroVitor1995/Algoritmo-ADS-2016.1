def main():
	idade = input('digite sua idade: ')
	soma_idade_otimo = 0
	qtd_otimo = 0
	qtd_regular = 0
	qtd_total = 0
	qtd_bom = 0
	while idade > 0:
		op = int(input('digite sua opniao: '))
		qtd_total = qtd_total + 1
		if op == 1:
			soma_idade_otimo = soma_idade_otimo + idade
			qtd_otimo = qtd_otimo + 1
		elif op == 2:
			qtd_bom = qtd_bom + 1
		elif op == 3:
			qtd_regular = qtd_regular + 1

		idade = input('digite sua idade: ')

	#Apurar os resultados
	media_idade_otimo = soma_idade_otimo / float(qtd_otimo)
	percetual_bom = (qtd_bom / float(qtd_total)) * 100.0
	
	#Resultados
	print 'A media das idades das pessoas que responderam otimo = %.2f' % media_idade_otimo
	print 'a quantidade de pessoas que respondeu regular = %d' % qtd_regular
	print 'o percentual de pessoas que respondeu bom = %.1f %%' % percetual_bom
	

if __name__ == '__main__':
	main()