#__*__  encoding:utf8 __*__
"""12. As companhias de transportes aéreos costumam representar os nomes dos passageiros no formato último
sobrenome/nome. Por exemplo, o passageiro Carlos Drummond de Andrade seria indicado por
Andrade/Carlos. Escreva um programa que leia um nome completo e o escreva no formato acima."""
def main():
	nome_completo = raw_input('Digite seu nome completo: ')
	nome_completo = nome_completo.split()
	nome = ''
	ultimo_sobrenome = ''
	for i in range(len(nome_completo)):
		nome = nome_completo[0]
	for i in range(len(nome_completo)-1,-1,-1):
		ultimo_sobrenome = nome_completo[-1]
	nome = nome.capitalize()
	ultimo_sobrenome = ultimo_sobrenome.capitalize()
	print('%s/%s') % (ultimo_sobrenome,nome)
if __name__ == '__main__':
	main()