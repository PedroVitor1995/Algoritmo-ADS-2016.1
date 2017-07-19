"""8. Leia data atual dia, mes e ano e data de nascimento dia, mes e ano de uma pessoa, calcule e escreva
sua idade exata em anos."""
def calcula_idade(dia_atual,mes_atual,ano_atual,dia,mes,ano):
	if dia_atual >= 1 or dia_atual <= 31 and mes_atual >= 1 or mes_atual <= 12 :
		if  dia >= 1 or dia <= 31 and mes >= 1 or mes <= 12 :
			idade_exata = ano_atual - ano
			print ('\nA idade exata em anos dessa pessoa e %d anos ') % (idade_exata)
def main():
	print ('Data Atual')
	dia_atual,mes_atual,ano_atual = input ('Dia: '), input ('\nMes: '), input ('\nAno: ')

	print ('\nData de Nascimento ')
	dia,mes,ano = input ('\nDia: '), input ('\nMes: '), input ('\nAno: ')
	calcula_idade(dia_atual,mes_atual,ano_atual,dia,mes,ano)

if __name__ == '__main__':
	main()
