#__*__  encoding:utf8 __*__
"""10. Uma palavra é palíndroma se ela não se altera quando lida da direita para esquerda. Por exemplo, raiar
é palíndroma. Escreva um programa que verifique se uma palavra digitada é palíndroma."""
def main():
	palavra = raw_input('Digite uma palavra: ')
	palavra_inversa = palavra[::-1]
	if palavra == palavra_inversa:
		print('A palavra digitada eh palindroma')
	else:
		print('A palavra digitada nao eh palindroma')
if __name__ == '__main__':
	main()