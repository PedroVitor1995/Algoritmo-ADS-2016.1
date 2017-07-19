#__*__  encoding:utf8 __*__
"""8. Leia uma string no formato hh:mm:ss e escreva o resultado na seguinte forma: “hh hora(s), mm
minuto(s) e ss segundo(s)”."""
def main():
	string = raw_input('Digite uma string no formato (hh mm ss):')
	string = string.split()
	for i in range(len(string)):
		hora = string[0]
		minuto = string[1]
		segundo = string[2]
	resultado = ("%s hora(s), %s minuto(s) e %s segundo(s) ") % (hora,minuto,segundo)
	print resultado
if __name__ == '__main__':
	main()