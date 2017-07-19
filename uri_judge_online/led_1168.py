def main():

	mapa = {'1':2, '2': 5, '3': 5, '4': 4, \
		'5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

	qtd = input()
	numeros = []
	for i in range(qtd):
		numeros.append(raw_input())

	for i in range(qtd):
		qtd_leds = 0
		numero_atual_em_string = numeros[i]
		for i in numero_atual_em_string:
			qtd_leds += mapa[i]
		print '{} leds'.format(qtd_leds)


if __name__ == '__main__':
	main()