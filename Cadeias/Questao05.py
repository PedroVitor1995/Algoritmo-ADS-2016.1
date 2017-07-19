#__*__  encoding:utf8 __*__
"""5. Leia uma data no formato DD/MM/AAAA e escreva o mês por extenso (DD de mês de AAAA)."""
def main():
	data = raw_input('Digite uma data no formato DD/MM/AAAA: ')
	dia = data[0:2]
	mes = data[3:5]
	ano = data[6:9]
	if mes == '01':
		print("%s de Janeiro de %s") % (dia,ano)
	elif mes == '02':
		print("%s de Fevereiro de %s") % (dia,ano)
	elif mes == '03':
		print("%s de Marco de %s") % (dia,ano)
	elif mes == '04':
		print("%s de Abril de %s") % (dia,ano)
	elif mes == '05':
		print("%s de Maio de %s") % (dia,ano)
	elif mes == '06':
		print("%s de Junho de %s") % (dia,ano)
	elif mes == '07':
		print("%s de Julho de %s") % (dia,ano)
	elif mes == '08':
		print("%s de Agosto de %s") % (dia,ano)
	elif mes == '09':
		print("%s de Setembro de %s") % (dia,ano)
	elif mes == '10':
		print("%s de Outubro de %s") % (dia,ano)
	elif mes == '11':
		print("%s de Novembro de %s") % (dia,ano)
	elif mes == '12':
		print("%s de Dezembro de %s") % (dia,ano)
if __name__ == '__main__':
	main()