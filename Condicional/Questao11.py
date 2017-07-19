"""11. Leia quatro numeros (opcao, num 1, num2, num3) e que escreva o valor de num1 se opcao igual a 1; o
valor de num2 se opcao for igual a 2; e o valor de num3 se opcao for igual a 3. Os unicos valores
possiveis para a variavel opcao sao 1, 2 e 3."""
def main():
	numero1 = input ('Digite o primeiro numero: ')
	numero2 = input ('\nDigite o segundo numero: ')
	numero3 = input ('\nDigite o terceiro numero: ')
	opcao = input ('\nDigite a opcao 1 numero1,2 numero2,3 numero3: ')

	if opcao == 1 :
		print ('\nO numero correspondente a opcao 1 e %d ') % (numero1)
	elif opcao == 2 :
		print ('\nO numero correspondente a opcao 2 e %d ') % (numero2)
	elif opcao == 3 :
		print ('\nO numero correspondente a opcao 3 e %d ') % (numero3)
	else :
		print ('\nOpcao invalida ') 
if __name__ == '__main__':
	main()