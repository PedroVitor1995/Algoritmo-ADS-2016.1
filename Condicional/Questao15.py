"""15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
Escreva na tela qual dos professores tem salario total maior."""
def main():
	horas_prof1 = input ('Digite a quantidade de horas aula dadas pelo professor 1: ')
	valor_horas_prof1 = input ('\nDigite o valor da hora aula dada pelo professor 1: ')
	horas_prof2 = input ('\nDigite a quantidade de horas aula dadas pelo professor 2: ')
	valor_horas_prof2 = input ('\nDigite o valor da hora aula dada pelo professor 2: ')

	salario_prof1 = horas_prof1 * valor_horas_prof1
	salario_prof2 = horas_prof2 * valor_horas_prof2

	if salario_prof1 > salario_prof2 :
		print ('\nO professor 1 tem um salario maior que o professor 2 ')
	else :
		print ('\nO professor 2 tem um salario maior que o professor 1 ')
if __name__ == '__main__':
	main()


