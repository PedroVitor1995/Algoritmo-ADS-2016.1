"""16. Leia duas notas de um aluno e escreva na tela a palavra Aprovado se a media das duas notas for maior
ou igual a 7,0. Caso a media seja inferior a 7,0, o programa deve ler a nota do exame e calcule a media
final. Se esta media for maior ou igual a 5,0, o programa deve escreva Aprovado, caso contrario deve
escreva Reprovado. 
Escreva um algoritmo para ler um número e verificar se ele obedece a esta característica."""
def main():
	nota1 = input ('Digite a primeira nota: ')
	nota2 = input ('\nDigite a segunda nota: ')

	media = (nota1 + nota2) / 2

	if media >= 7.0 :
		print ('\nAprovado ')
	else :
		nota_exame = input ('\nDigite a nota do exame final: ')
		media_final = (media + nota_exame) / 2
	        if media_final >= 5.0 :
	        	print ('\nAprovado ')
	        else :
	        	print ('\nReprovado ')
if __name__ == '__main__':
	main()


