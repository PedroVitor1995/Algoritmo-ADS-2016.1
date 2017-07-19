"""29. Escreva um algoritmo que calcula o retorno de um investimento financeiro. O usuario deve informar
quanto sera investido por mes e qual sera a taxa de juros mensal. O algoritmo deve informar o saldo do
investimento apos um ano (soma das aplicacoes mensais + juros compostos), e perguntar ao usuario se
deseja calcular o ano seguinte, sucessivamente. Por exemplo, caso o usuario deseje investir R$ 100,00
por mes, e tenha uma taxa de juros de 1%  ao mes, o algoritmo forneceria a seguinte saida:
Saldo do investimento apos 1 ano: 1268.25
Deseja processar mais um ano (S/N) ?"""
def main():
	while True:

		quantidade_de_anos = input('\nDigite a quantidade de anos do seu investimento sendo 0 para sair: ')
		quantidade_de_meses = quantidade_de_anos * 12

		if quantidade_de_anos == 0:
			break
		else:
			investimento_mes = input('\nDigite o quanto sera investido: ')
			taxa_juro_mensal = input('\nDigite qual sera a taxa de juros mensal: ')
			taxa_juro_mensal = float(taxa_juro_mensal)
			taxa_juro_mensal = taxa_juro_mensal / 100

			saldo_investimento_ano = investimento_mes * ((1 + taxa_juro_mensal) ** quantidade_de_meses)
			print('\nO saldo do investimento apos um ano eh %.2f ') % saldo_investimento_ano
			ano_seguinte = raw_input('\nDeseja processar mais um ano (SIm/sim ou NAo/nao): ')

			if ano_seguinte == 'SIM' or ano_seguinte == 'sim':
				saldo_investimento_ano =  investimento_mes * (1 + taxa_juro_mensal) ** (quantidade_de_meses + 12)
				print('\nO saldo do investimento apos um ano mais o ano seguinte ao ano eh %.2f ') % saldo_investimento_ano
				continue
if __name__ == '__main__':
	main()



