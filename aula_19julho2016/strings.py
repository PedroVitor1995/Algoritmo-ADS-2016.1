def main():

	palavra = 'Instituto Federal'
	i = 0
	tamanho = len(palavra)
	print('Tamanho = %d' % tamanho)
	while i < tamanho:
		print(i, palavra[i])
		i = i + 1

if __name__ == '__main__':
	main()