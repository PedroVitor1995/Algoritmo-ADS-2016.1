#__*__  encoding:utf8 __*__
"""8. Leia uma string no formato hh:mm:ss e escreva o resultado na seguinte forma: “hh hora(s), mm
minuto(s) e ss segundo(s)”."""
def main():
	horas = raw_input('Digite uma string no formato hh:mm:ss: ')
	hora = horas[0:2]
	minuto = horas[3:5]
	segundo = horas[6:9]
	print('%s hora(s), %s minuto(s) e %s segundo(s) ') % (hora,minuto,segundo)
if __name__ == '__main__':
	main()