def main():
	mapa = {'1':2, '2': 5, '3': 5, '4': 4, \
		'5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

	qtd_testes = input()

	resultados = []

	for i in range(qtd_testes):

		numero = raw_input()

		qtd_led = 0

		for letra in numero:
			qtd_led += mapa[letra]
		
		resultados.append(qtd_led)

	for r in resultados:
		print "%d leds" % r

if __name__ == '__main__':
	main()