def registros_medalhas():
	arquivo = open('medalhas.txt','r') 
	linhas = arquivo.readlines() 
	registros = [] 
	for linha in linhas: 
		registros.append(eval(linha)) 
	arquivo.close()
	arquivo = open('medalhas.txt', 'w')
	return registros
def acrecentar_medalhas(nome_recebido,esporte_recebido, modalidade_recebido, medalha_racebida, pais_recebido):
	medalha = {
		'nome': nome_recebido,
		'esporte': esporte_recebido,
		'modalidade': modalidade_recebido,
		'medalha': medalha_recebida,
		'pais': pais_recebido,
	}

	return medalha