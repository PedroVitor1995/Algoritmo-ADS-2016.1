def inicializar_partidos():
	coligacoes = []
	arquivo1 = open('partidos_coligacoes_the_2012.csv', 'r')
	for linha in arquivo1:
		dados = linha.strip()
		coligacao = {
					'coligacao':dados,
					'total_votos':0,
					'qtd_vargas': 0,
					'votos_sobra_total':0
					}
		coligacoes.append(coligacao)
	arquivo1.close()
	return coligacoes
def inicializar_candidatos():
	candidatos = []
	arquivo2 = open('candidatos_e_votos_vereador_THE_2012.csv', 'r')
	for linha in arquivo2:
		dados = linha.strip().split(';')
		candidato = {
					'nome':dados[0],
					'numero':dados[1],
					'partido': dados[2],
					'coligacao':dados[3],
					'total_votos':int(dados[4])
					}
		candidatos.append(candidato)
	arquivo2.close()
	return candidatos
def votos_validos(lista_de_candidatos):
	quantidade_votos = 0
	for candidato in range(len(lista_de_candidatos)):
		quantidade_votos += lista_de_candidatos[candidato]['total_votos']
	print('Quantidade de votos validos: {}'.format(quantidade_votos))
def quociente_eleitoral(lista_de_candidatos):
	quantidade_votos = 0
	for candidato in range(len(lista_de_candidatos)):
		quantidade_votos += lista_de_candidatos[candidato]['total_votos']
	quociente_eleitoral = quantidade_votos // 29
	print('O quociente eleitoral de 2012 foi: {}'.format(quociente_eleitoral))
def votos_por_coligacao(lista_de_coligacoes,lista_de_candidatos):
	for coligacao in range(len(lista_de_coligacoes)):
		qtd_votos = 0
		for candidato in range(len(lista_de_candidatos)):
			if lista_de_coligacoes[coligacao]['coligacao'] == lista_de_candidatos[candidato]['coligacao']:
				qtd_votos += lista_de_candidatos[candidato]['total_votos']
		lista_de_coligacoes[coligacao]['total_votos'] = qtd_votos
	for coligacao in range(len(lista_de_coligacoes)):
		print('Coligacao {} '.format(lista_de_coligacoes[coligacao]['coligacao']))
		print('Total de votos {} \n'.format(lista_de_coligacoes[coligacao]['total_votos']))
def vagas_quociente_partidario(lista_de_coligacoes,lista_de_candidatos):
	quantidade_votos = 0
	for candidato in range(len(lista_de_candidatos)):
		quantidade_votos += lista_de_candidatos[candidato]['total_votos']
	quociente_eleitoral = quantidade_votos // 29
	for coligacao in range(len(lista_de_coligacoes)):
		qtd_votos = 0
		for candidato in range(len(lista_de_candidatos)):
			if lista_de_coligacoes[coligacao]['coligacao'] == lista_de_candidatos[candidato]['coligacao']:
				qtd_votos += lista_de_candidatos[candidato]['total_votos']
		lista_de_coligacoes[coligacao]['total_votos'] = qtd_votos
	for coligacao in range(len(lista_de_coligacoes)):
		qtd_vargas = lista_de_coligacoes[coligacao]['total_votos'] // quociente_eleitoral
		resto_votos = lista_de_coligacoes[coligacao]['total_votos'] % quociente_eleitoral
		lista_de_coligacoes[coligacao]['qtd_vargas'] = qtd_vargas
		lista_de_coligacoes[coligacao]['votos_sobra_total'] = resto_votos
	qtd_vargas_total = 0
	for coligacao in range(len(lista_de_coligacoes)):
		qtd_vargas_total += lista_de_coligacoes[coligacao]['qtd_vargas']
	qtd_vargas_sobra = 29 - qtd_vargas_total
	for coligacao in range(len(lista_de_coligacoes)):
		print('Coligacao {} '.format(lista_de_coligacoes[coligacao]['coligacao']))
		print('Quantidade de vargas {} \n'.format(lista_de_coligacoes[coligacao]['qtd_vargas']))
	print('Faltam {} vargas para ser ocupadas '.format(qtd_vargas_sobra))
def vargas_sobra(lista_de_coligacoes,lista_de_candidatos):
	quantidade_votos = 0
	for candidato in range(len(lista_de_candidatos)):
		quantidade_votos += lista_de_candidatos[candidato]['total_votos']
	quociente_eleitoral = quantidade_votos // 29
	for coligacao in range(len(lista_de_coligacoes)):
		qtd_votos = 0
		for candidato in range(len(lista_de_candidatos)):
			if lista_de_coligacoes[coligacao]['coligacao'] == lista_de_candidatos[candidato]['coligacao']:
				qtd_votos += lista_de_candidatos[candidato]['total_votos']
		lista_de_coligacoes[coligacao]['total_votos'] = qtd_votos
	for coligacao in range(len(lista_de_coligacoes)):
		qtd_vargas = lista_de_coligacoes[coligacao]['total_votos'] // quociente_eleitoral
		resto_votos = lista_de_coligacoes[coligacao]['total_votos'] % quociente_eleitoral
		lista_de_coligacoes[coligacao]['qtd_vargas'] = qtd_vargas
		lista_de_coligacoes[coligacao]['votos_sobra_total'] = resto_votos
	qtd_vargas_total = 0
	for coligacao in range(len(lista_de_coligacoes)):
		qtd_vargas_total += lista_de_coligacoes[coligacao]['qtd_vargas']
	qtd_vargas_sobra = 29 - qtd_vargas_total
	for i in range(len(lista_de_candidatos)):
		aux = i
		for j in range(len(lista_de_candidatos)-1):
			if lista_de_candidatos[j]['total_votos'] <= lista_de_candidatos[aux]['total_votos']:
				aux = j
			lista_de_candidatos[aux], lista_de_candidatos[i] = lista_de_candidatos[i], lista_de_candidatos[aux]
	for candidato in range(len(lista_de_candidatos)):
		print(lista_de_candidatos[candidato])