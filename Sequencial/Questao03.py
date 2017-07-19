#__*__  encoding:utf8 __*__
"""3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos."""
def calcula_horas(valor_minutos):
	valor_horas = valor_minutos / 60
	return valor_horas
def calcula_minutos(valor_minutos):
	valor_minutos_restante = valor_minutos % 60
	return valor_minutos_restante

def main():
	valor_minutos = input ('Digite um valor em minutos: ')
	valor_horas = calcula_horas(valor_minutos)
	valor_minutos = calcula_minutos(valor_minutos)
	print valor_horas,valor_minutos

if __name__ == '__main__':
	main()