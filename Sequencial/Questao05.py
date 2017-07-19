#__*__  encoding:utf8 __*__
"""5. Leia um nmero inteiro (3 digitos), calcule e escreva a soma de seus elementos (C + D + U)."""
def calcula_soma(numero):
	C = numero / 100
	D = (numero % 100) / 10
	U = numero % 10
	soma = C + D + U
	return soma

def main():
	numero = input ('Digite um numero inteiro de 3 digitos: ')
	soma = calcula_soma(numero)
	print soma

if __name__ == '__main__':
	main()