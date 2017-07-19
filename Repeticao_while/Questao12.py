#__*__  encoding:utf8 __*__
"""12. Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e
responda quem ganha a partida. A partida chega ao final se:
· Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
· Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma
diferença de 2 pontos sobre o adversário."""
def main():
	ponto_jogador1 = 0
	ponto_jogador2 = 0
	diferenca1 = 0
	diferenca2 = 0
	while True:
		codigo = input('Digite o codigo (1 ou 2) quem ganhou o ponto: ')
		if codigo == 1:
			ponto_jogador1 = ponto_jogador1 + 1
		elif codigo == 2:
			ponto_jogador2 = ponto_jogador2 + 1

		diferenca1 = ponto_jogador1 - ponto_jogador2
		diferenca2 = ponto_jogador2 - ponto_jogador1
		if ponto_jogador1 == 21 and diferenca1 >= 2:
			print('O ganhador foi o jogador 1')
			print('Fim')
			break
		elif ponto_jogador2 == 21 and diferenca2 >= 2:
			print('O ganhador foi o jogador 2')
			print('Fim')
			break
		else:
			if ponto_jogador1 >= 21 and diferenca1 >= 2:
				print('O ganhador foi o jogador 1')
				print('Fim')
				break
			elif ponto_jogador2 >= 21 and diferenca2 >= 2:
				print('O ganhador foi o jogador 2')
				print('Fim')
				break






if __name__ == '__main__':
	main()