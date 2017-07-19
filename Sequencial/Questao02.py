#__*__  encoding:utf8 __*__
"""2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos."""
def calcula_minutos(valor_horas,valor_minutos):
	valor_total_minutos = (valor_horas * 60 ) + valor_minutos
	return valor_total_minutos

def main():

	valor_horas = input ('Digite um valor em horas: ')
	valor_minutos = input ('Digite um valor em minutos: ')

	valor_total_minutos = calcula_minutos(valor_horas,valor_minutos)
	print valor_total_minutos
	
if __name__ == '__main__':
	main()