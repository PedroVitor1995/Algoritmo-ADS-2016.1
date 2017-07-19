def main():
	qtd_testes = int(input())

	for i in range(qtd_testes):
		qtd_alunos = int(input())
		alunos = input().split()

		#convert para inteiro
		for j in range(qtd_alunos):
			alunos[j] = int(alunos[j])

		#copia ordenada decrescente de alunos
		alunos_desc = sorted(alunos, reverse=True)

		#Contar alunos que nao precisam mudar de posicao
		resultado = 0
		for k in range(qtd_alunos):
			if alunos[k] == alunos_desc[k]:
				resultado += 1

		#Imprimir Resultado
		print(resultado)



if __name__ == '__main__':
	main()