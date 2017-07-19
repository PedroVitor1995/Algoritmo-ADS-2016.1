def main():
	string = input('Digite uma string no formato hh:mm:ss: ').split(':')
	hora = string[0]
	minuto = string[1]
	segundo = string[2]
	print('{} hora(s), {} minuto(s) e {} segundo(s) '.format(hora,minuto,segundo))
if __name__ == '__main__':
	main()