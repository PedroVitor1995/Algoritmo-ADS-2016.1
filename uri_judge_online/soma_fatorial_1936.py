import math
def main():

	n = int(input())
	maximo = 10**5
	fatoriais = [1, 2] #inicializado com fatoriais simples
	i = 3
	fat = 2

	#Criar lista de fatoriais até o máximo estabelecido
	while fat < maximo:
		fat = math.factorial(i)
		fatoriais.append(fat)
		i += 1

	fatoriais.sort(reverse=True)
	
	# Verifica com divisoes inteiras
	qtd_fatoriais = 0
	for f in fatoriais:
		qtd = n // f
		n = n % f
		if qtd > 0:
			qtd_fatoriais += qtd

	print(qtd_fatoriais)


if __name__ == '__main__':
	main()