"""23. Uma determinada empresa armazena para cada funcionario uma ficha contendo o codigo, o numero de
horas trabalhadas e o seu numero de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salario sao feitos descontos de 8,5%  para o INSS e 5%  para IR.
Escreva um algoritmo que leia o codigo, numero de horas trabalhadas e numero de dependentes de N
funcionarios. Apos a leitura de cada ficha, escreva os valores descontados para cada imposto e o salario
liquido do funcionario."""
def main():
	quantidade_funcionario = input('Digite a quantidade de funcionarios que trabalham na empresa: ')

	for i in range(1, quantidade_funcionario + 1):

		codigo_funcionario = input('\nDigite o codigo do funcionario: ')
		numero_horas_trabalhadas = input('\nDigite o numero de horas trabalhadas pelo funcionario: ')
		numero_dependentes = input('\nDigite o numero de dependentes do funcionario: ')

		valor_horas_trabalhadas = numero_horas_trabalhadas * 12.00
		valor_dependentes = numero_dependentes * 40.00

		salario_bruto = valor_horas_trabalhadas + valor_dependentes

		descontos_inss = salario_bruto * 0.085
		descontos_ir = salario_bruto * 0.05

		salario_liquido = salario_bruto - descontos_inss - descontos_ir

		print('\nO valor descontado do funcionario de imposto em INSS eh %.2f ') % descontos_inss
		print('\nO valor descontado do funcionario de imposto em IR eh %.2f ') % descontos_ir
		print('\nO salario do funcionario liquido eh %.2f ') % salario_liquido
if __name__ == '__main__':
	main()
