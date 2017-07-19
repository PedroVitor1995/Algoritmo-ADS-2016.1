def main():

	qtd = input()
	for i in range(qtd):
		palavra = raw_input()

		#passo 1: Deslocar letra(Minus e Maius) 3+
		nova_palavra = ''
		for letra in palavra:
			if letra.isalpha():
				nova_palavra = nova_palavra + chr(ord(letra)+3)
			else:
				nova_palavra = nova_palavra + letra

		#passo 2: Inverter
		nova_palavra = nova_palavra[::-1]

		#passo 3: quebrar em dois
		meio = len(nova_palavra) / 2
		parte1 = nova_palavra[:meio]
		parte2 = nova_palavra[meio:]

		parte2_v2 = ''
		for letra in parte2:
			parte2_v2 = parte2_v2 + chr(ord(letra)-1)

		# Resultado
		print parte1 + parte2_v2

if __name__ == '__main__':
	main()