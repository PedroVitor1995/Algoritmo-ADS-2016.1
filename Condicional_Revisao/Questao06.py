#__*__ encoding:utf8 __*__
"""6. Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme"""
def main():
	turno = raw_input('Digite o turno que estuda "M - Matutino" "V - Vespertino" "N - Noturno": ')
	if turno == 'M' or turno == 'm':
		print('Bom Dia!')
	elif turno == 'V' or turno == 'v':
		print('Boa Tarde!')
	elif turno == 'N' or turno == 'n':
		print('Boa Noite!')
	else:
		print('Valor Inválido!')
if __name__ == '__main__':
	main()