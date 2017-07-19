from medalhas import obter_pais_por_id
def consultas(medalhas, paises):
	cabecalho = "\n **** Consultas e Estatisticas **** \n"
	menu_consulta = " 1 - Medalhas por Pais \n 2 - Medalhas por Continente \n"\
	" 3 - Paises Sem Medalhas \n 4 - Medalhas por Sexo \n"\
	" 5 - Pais-Medalhas por habitante/atleta \n" \
	" 6 - Pesquisa por Nome do Atleta\n" \
	" 7 - Pesquisa por Nome do Pais \n" \
	" 8 - Pesquisa por Nome do Esporte" \
	"\n 0 - Voltar \n opcao >>> "

	while True:
		opcao = input(cabecalho + menu_consulta)

		if opcao == 0:
			return
		elif opcao == 1:
			medalhas_por_pais(medalhas, paises)
		elif opcao == 2:
			medalhas_por_continente(medalhas, paises)
		elif opcao == 3:
			paises_sem_medalhas(medalhas, paises)
		elif opcao == 4:
			medalhas_por_sexo(medalhas)
		elif opcao == 5:
			medalhas_pais_habitantes_atletas(medalhas, paises)
		elif opcao == 6:
			medalhas_por_nome_do_atleta(medalhas, paises)
		elif opcao == 7:
			medalhas_por_nome_do_pais(medalhas, paises)
		elif opcao == 8:
			medalhas_por_nome_do_esporte(medalhas, paises)
		else:
			print 'Opcao invalida.'


def medalhas_por_pais(medalhas, paises):

	for pais in paises:
		qtd_ouro = qtd_medalha_por_pais(medalhas, pais['id'], 'Ouro')
		qtd_prata = qtd_medalha_por_pais(medalhas, pais['id'], 'Prata')
		qtd_bronze = qtd_medalha_por_pais(medalhas, pais['id'], 'Bronze')
		print '%s -> Ouro: %d -> Prata: %d -> Bronze: %d' % (pais['nome'], qtd_ouro, qtd_prata, qtd_bronze )


def qtd_medalha_por_pais(medalhas, pais_id, tipo_medalha):
	qtd = 0
	for medalha in medalhas:
		if medalha['pais_id'] == pais_id and medalha['medalha'] == tipo_medalha:
			qtd += 1

	return qtd


def medalhas_por_continente(medalhas, paises):
	continentes = ['AMERICA', 'EUROPA', 'ASIA', 'OCEANIA', 'AFRICA']

	for continente in continentes:
		qtd_ouro = qtd_medalha_por_continente(medalhas, paises, continente, 'Ouro')
		qtd_prata = qtd_medalha_por_continente(medalhas, paises, continente, 'Prata')
		qtd_bronze = qtd_medalha_por_continente(medalhas, paises, continente, 'Bronze')
		print '%s -> Ouro: %d -> Prata: %d -> Bronze: %d' % (continente, qtd_ouro, qtd_prata, qtd_bronze )


def qtd_medalha_por_continente(medalhas, paises, continente, tipo_medalha):
	qtd = 0

	for medalha in medalhas:
		pais = obter_pais_por_id(medalha['pais_id'], paises)
		if pais['continente'] == continente and medalha['medalha'] == tipo_medalha:
			qtd += 1

	return qtd

def paises_sem_medalhas(medalhas, paises):

	nomes_paises_medalhistas = paises_com_medalhas(medalhas, paises)

	for pais in paises:
		if pais['nome'] not in nomes_paises_medalhistas:
			print "%s" % pais['nome']



def paises_com_medalhas(medalhas, paises):
	lista_nomes_paises_medalhista = []
	for medalha in medalhas:
		pais = obter_pais_por_id(medalha['pais_id'], paises)
		if pais['nome'] not in lista_nomes_paises_medalhista:
			lista_nomes_paises_medalhista.append(pais['nome'])

	return lista_nomes_paises_medalhista


def medalhas_por_sexo(medalhas):
	qtd_masculinho = 0
	qtd_feminino = 0

	for medalha in medalhas:
		if medalha['modalidade'] == 'Feminino':
			qtd_feminino += 1
		else:
			qtd_masculinho += 1

	print "Medalhas: Feminino --> %d & Masculinho --> %d" % (qtd_feminino, qtd_masculinho)

def medalhas_pais_habitantes_atletas(medalhas, paises):
	maior_por_habitante = 0
	pais_maior_habitante = ''
	maior_por_atleta = 0
	pais_maior_atleta = ''

	for pais in paises:
		qtd_medalhas = qtd_medalhas_qq_tipo(medalhas, pais)
		medalhas_por_habitante = qtd_medalhas / float(pais['populacao'])
		medalhas_por_atletas = qtd_medalhas / float(pais['atletas'])

		if medalhas_por_habitante > maior_por_habitante:
			maior_por_habitante = medalhas_por_habitante
			pais_maior_habitante = pais

		if medalhas_por_atletas > maior_por_atleta:
			maior_por_atleta = medalhas_por_atletas
			pais_maior_atleta = pais

	print "Maior Medalhista por Habitante = %s == %.10f" % (pais_maior_habitante['nome'], maior_por_habitante)
	print "Maior Medalhista por Atletas = %s == %f" % (pais_maior_atleta['nome'], maior_por_atleta)


def qtd_medalhas_qq_tipo(medalhas, pais):
	qtd = 0
	for medalha in medalhas:
		if medalha['pais_id'] == pais['id']:
			qtd += 1
	return qtd


def medalhas_por_nome_do_atleta(medalhas, paises):
	parte_nome = raw_input('Nome do atleta: ')

	for medalha in medalhas:
		if parte_nome.upper() in medalha['atleta'].upper():
			pais = obter_pais_por_id(medalha['pais_id'], paises)
			print '%s - %s - %s  - %s' % (medalha['atleta'], medalha['esporte'], medalha['medalha'], pais['nome'])

def medalhas_por_nome_do_pais(medalhas, paises):

	parte_nome = raw_input('Nome do Pais: ')

	for pais in paises:
		if parte_nome.upper() in pais['nome'].upper():
			for medalha in medalhas:
				if medalha['pais_id'] == pais['id']:
					print '%s - %s - %s  - %s' % (medalha['atleta'], medalha['esporte'], medalha['medalha'], pais['nome'])


def medalhas_por_nome_do_esporte(medalhas, paises):

	parte_nome = raw_input('Nome do Esporte: ')

	for medalha in medalhas:
		if parte_nome.upper() in medalha['esporte'].upper():
			pais = obter_pais_por_id(medalha['pais_id'], paises)
			print '%s - %s - %s  - %s' % (medalha['atleta'], medalha['esporte'], medalha['medalha'], pais['nome'])


