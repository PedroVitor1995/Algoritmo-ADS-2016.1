def main():
	numeros = input().split(' ')
	jogadores = int(numeros[0])
	rodadas = int(numeros[1])
	pontos = input().split()
	jogadas = []
	pontuacao = []
	pontos_total = []
	soma = 0
	jogador = 0
	for i in range(jogadores * rodadas):
		jogada = int(pontos[i])
		jogadas.append(jogada)
	for i in range(jogadores):
		ponto = jogadas[i::jogadores]
		pontuacao.append(ponto)
	for i in range(len(pontuacao)):
		for j in range(len(pontuacao[i])):
			soma += pontuacao[i][j]
		pontos_total.append(soma)
		soma = 0
	ganhador = 0
	for i in range(len(pontos_total)):
		if pontos_total[i] >= pontos_total[ganhador]:
			ganhador = i
		ganhador = ganhador
	print(ganhador+1)
if __name__ == '__main__':
	main()