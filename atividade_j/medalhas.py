def nova_medalha(paises):

	tipos_medalhas = ['Ouro', 'Prata', 'Bronze'] 
	modalidades = ['Masculino', 'Feminino', 'Misto']

	atleta = raw_input('Atleta: ')
	esporte = raw_input('Esporte: ')

	modalidade = raw_input('Masculino - Feminino - Misto: ')
	while modalidade not in modalidades:
		modalidade = raw_input('Masculino - Feminino - Misto: ')

	medalha = raw_input('Ouro - Prata - Bronze: ')
	while medalha != 'Ouro' and medalha != 'Prata' and medalha != 'Bronze':
	#while medalha not in tipos_medalhas:
		medalha = raw_input('Ouro - Prata - Bronze: ')
	
	listar_paises(paises)
	pais_id = input('ID do Pais: ')
	while not pais_id_valido(pais_id, paises):
		pais_id = input('ID do Pais: ')

	medalha = {'atleta': atleta, 'esporte': esporte, 'modalidade': modalidade, 'medalha': medalha, 'pais_id': pais_id}

	return medalha

def pais_id_valido(pais_id, paises):
	for pais in paises:
		if pais['id'] == pais_id:
			return True

	return False

def listar_paises(paises):
	for pais in paises:
		print "%d - %s" % (pais['id'], pais['nome'])

def remover_medalha(medalhas, paises):
	lista_todas_medalhas(medalhas, paises)
	medalha_id = input('ID da medalha a remover: ')
	medalhas.pop(medalha_id)

def lista_todas_medalhas(medalhas, paises):
	ordem = 0
	for medalha in medalhas:
		pais = obter_pais_por_id(medalha['pais_id'], paises)
		print "%d - %s - %s - %s - %s" % (ordem, medalha['atleta'], medalha['esporte'], medalha['medalha'], pais['nome'])
		ordem += 1

def obter_pais_por_id(pais_id, paises):
	for pais in paises:
		if pais['id'] == pais_id:
			return pais



