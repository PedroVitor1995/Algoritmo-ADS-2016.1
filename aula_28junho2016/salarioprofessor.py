def calcula_salario(qtd_horas, valor_hora):
	salario = qtd_horas * valor_hora
	return salario


def main():
	print '$$$ Calcula Salario $$$'
	valor_hora_prof1 = input('Valor do hora Prof1: ')
	qtd_horas_prof1 = input('Horas Prof1: ')
	valor_hora_prof2 = input('Valor do hora Prof2: ')
	qtd_horas_prof2 = input('Horas Prof2: ')
	
	salario_prof1 = calcula_salario(qtd_horas_prof1, valor_hora_prof1)
	salario_prof2 = calcula_salario(qtd_horas_prof2, valor_hora_prof2)

	#Compara os salarios
	print 'Professor 1 ganha R$ %.2f' % salario_prof1
	print 'Professor 2 ganha R$ %.2f' % salario_prof2

	if salario_prof1 > salario_prof2:
		print 'Professor 1 ganha mais.'
	elif salario_prof1 < salario_prof2:
		print 'Professor 2 ganha mais.'
	else:
		print 'Salario sao iguais.'

if __name__ == '__main__':
	main()




