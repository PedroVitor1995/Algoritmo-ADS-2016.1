"""11. Leia informacoes de alunos (matricula, nota1, nota2, nota3) com o fim das informacoes indicado por
matricula = 0. Para cada aluno deve ser calculada a media final de acordo com a seguinte formula:
Media Final = (2 * nota1) + (3 * nota2) + (5 * nota3)/10"""
def main():
	quantidade_aprovados = 0
	quantidade_reprovados = 0
	while True:
		matricula = input('Digite a matricula de um aluno ou 0 para sair: ')

		if matricula == 0:
			break
		else:
			nota1 = input('Digite a primeira nota de um aluno: ')
			nota2 = input('Digite a segunda nota de um aluno: ')
			nota3 = input('Digite a terceira nota de um aluno: ')

			media_final = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / float(10)
			if media_final >= 7:
				quantidade_aprovados = quantidade_aprovados + 1
				print('Aluno Aprovado')
			else:
				quantidade_reprovados = quantidade_reprovados + 1
				print('Aluno Reprovado')
	print('A quantidade de alunos aprovados %d')%quantidade_aprovados
	print('A quantidade de alunos reprovados %d')%quantidade_reprovados

if __name__ == '__main__':
	main()