def main():
	quantidade_teste = int(input('Quantidade de teste: '))
	for i in range(quantidade_teste):
		valores = input('Valores de X e Y: ').split(' ')
		valor_x = int(valores[0])
		valor_y = int(valores[1])
		funcao_r = ((3*valor_x)**2) + (valor_y**2)
		funcao_b = (2*(valor_x**2)) + ((5*valor_y)**2)
		funcao_c = (-100*valor_x) + (valor_y**3)
		if funcao_r > funcao_b and funcao_r > funcao_c:
			print('Rafael ganhou')
		elif funcao_b > funcao_c:
			print('Beto ganhou')
		else:
			print('Carlos ganhou')
if __name__ == '__main__':
	main()