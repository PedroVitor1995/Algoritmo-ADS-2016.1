def main():
	emprestimo = 3000
	pagamento = 200
	contador = 1
	while emprestimo > 0:
		percentual = (emprestimo - pagamento) * (0.85 / 100)
		emprestimo = emprestimo - pagamento + percentual
		contador += 1
	print('Quantidade de dias uteis para pagar o emprestimo eh %d'%contador)
if __name__ == '__main__':
	main()