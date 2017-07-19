"""4. Leia as variaveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressao
Geometrica que tem por valor inicial A0 e razao R."""
def main():
	variavel_a = input('\nDigite o valor da variavel A0: ')
	limite = input('\nDigite o limite da progressao: ')
	valor_r = input('\nDigite o valor de R: ')

	print('\nA sequencia da progressao geometrica eh')

	fim = limite

	print variavel_a

	for i in range(1, fim + 1):

		progressao = variavel_a * valor_r

		if progressao < limite:
			print progressao
			variavel_a = progressao
		else:
			break
if __name__ == '__main__':
	main()