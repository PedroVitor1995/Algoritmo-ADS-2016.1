def main():
	qtd_testes = int(input())

	for i in range(qtd_testes):
		#input só para atender o formato da entrada
		input()

		#Recebe a linha, faz split e converte cada itens do split em Int()
		alunos = [int(i) for i in input().split(' ')]

		#Atribue a alunos_desc os alunos ordenados descrecente.
		alunos_desc = sorted(alunos, reverse=True)

		# Soma 1 para item de alunos que seja igual em alunos_desc na mesma posicao
		resultado = sum([1 for i in range(len(alunos)) if alunos[i] == alunos_desc[i]])

		print(resultado)


if __name__ == '__main__':
	main()