"""23. Leia 2 datas (cada data e composta por 3 variaveis inteiras: dia, mes e ano) e escreva qual delas e a mais
recente."""

print('Primeira Data:')
dia_data1,mes_data1,ano_data1 = input('Dia: '),input('Mes: '),input('Ano: ')
print('Segunda Data:')
dia_data2,mes_data2,ano_data2 = input('Dia: '),input('Mes: '),input('Ano: ')


if dia_data1 >= 1 and dia_data1 <= 30 and mes_data1 >= 1 and mes_data1 <= 12 and ano_data1 > 0:
	if dia_data2 >= 1 and dia_data2 <= 30 and mes_data2 >= 1 and mes_data2 <= 12 and ano_data2 >0:
		if ano_data1 == ano_data2:
			if mes_data1 == mes_data2:
				if dia_data1 < dia_data2:
					print('A data mais recente eh %d / %d / %d') % (dia_data2,mes_data2,ano_data2)
				else:
					print('A data mais recente eh %d / %d / %d') % (dia_data1,mes_data1,ano_data1)
			else:
				if mes_data1 < mes_data2:
					print('A data mais recente eh %d / %d / %d') % (dia_data2,mes_data2,ano_data2)
				else:
					print('A data mais recente eh %d / %d / %d') % (dia_data1,mes_data1,ano_data1)
		else:
			if ano_data1 < ano_data2:
				print('A data mais recente eh %d / %d / %d') % (dia_data2,mes_data2,ano_data2)
			else:
				print('A data mais recente eh %d / %d / %d') % (dia_data1,mes_data1,ano_data1)
	else:
		print('A segunda data estar invalida!')
else:
	print('A primeira data estar invalida!')


