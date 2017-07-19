import os
def limpar():
	os.system('cls')

def inicializar_veiculos(): 
	arquivo = open('veiculos.txt','r') 
	linhas = arquivo.readlines() 
	veiculos = [] 
	for linha in linhas: 
		veiculos.append(eval(linha)) 
	arquivo.close()
	
	return  veiculos

def inicializar_montadoras(): 
	arquivo = open('montadoras.txt','r') 
	linhas = arquivo.readlines() 
	montadoras = [] 
	for linha in linhas: 
		montadoras.append(eval(linha)) 
	arquivo.close()
	arquivo = open('veiculos.txt', 'w')

	return  montadoras

#veiculos
def acrecentar_veiculo(nome_recebido, ano_recebido, montadora_recebida, preco_recebido, motor_recebido):
	veiculo = {
		'nome': nome_recebido,
		'ano': ano_recebido,
		'montadora': montadora_recebida,
		'preco': preco_recebido,
		'motor': motor_recebido
	}

	return veiculo

def listar_veiculos(lista_de_veiculos, montadora = ''):
	print('Numero de veiculos cadastrados: %d'%len(lista_de_veiculos) )
	if not(montadora):#porisso que gosto de python
		for veiculo in range( len(lista_de_veiculos) ):
			print('----------------------------\n')
			print('	id:		{}'.format(veiculo) )
			print('	Nome:		{}'.format(lista_de_veiculos[veiculo]['nome']) )
			print('	Ano:		{}'.format(lista_de_veiculos[veiculo]['ano']) )
			print('	Montadora:	{}'.format(lista_de_veiculos[veiculo]['montadora']) )
			print('	Faixa de preco:	%.2f'%lista_de_veiculos[veiculo]['preco'])
			print('	Motor:		%.2f\n'%lista_de_veiculos[veiculo]['motor'])

	else:
		for veiculo in range(len(lista_de_veiculos)):
			if montadora == lista_de_veiculos[veiculo]['montadora']:
				print('----------------------------\n')
				print('		id:		{}'.format(veiculo) )
				print('		Nome:		{}'.format(lista_de_veiculos[veiculo]['nome']) )
				print('		Ano:		{}'.format(lista_de_veiculos[veiculo]['ano']) )
				print('		Montadora:	{}'.format(lista_de_veiculos[veiculo]['montadora']) )
				print('		Faixa de preco:	%.2f'%lista_de_veiculos[veiculo]['preco'])
				print('		Motor:		%.2f\n'%lista_de_veiculos[veiculo]['motor'])

def remover_veiculo(lista_de_veiculos, lista_de_montadoras, id_recebida):
	for veiculo in range( len(lista_de_veiculos) ):
		if(id_recebida == veiculo):
			decrementador_de_veiculos(lista_de_montadoras, lista_de_veiculos, lista_de_veiculos[id_recebida]['montadora'])
			lista_de_veiculos.pop(veiculo)
			return True
	return False

def editar_veiculo(lista_de_veiculos, id_recebida, chave, alteracao):
	lista_de_veiculos[id_recebida][chave] = alteracao

def listar_por_montadora(lista_de_montadoras, lista_de_veiculos, nome_montadora):
	for veiculo in range( len(lista_de_veiculos) ):
		if nome_montadora == lista_de_veiculos[veiculo]['montadora']:
			print('----------------------------\n')
			print('	id:		{}'.format(veiculo) )
			print('	Nome:		{}'.format(lista_de_veiculos[veiculo]['nome']) )
			print('	Ano:		{}'.format(lista_de_veiculos[veiculo]['ano']) )
			print('	Montadora:	{}'.format(lista_de_veiculos[veiculo]['montadora']) )
			print('	Faixa de preco:	%.2f'%lista_de_veiculos[veiculo]['preco'])
			print('	Motor:		%.2f\n'%lista_de_veiculos[veiculo]['motor'])

def listar_por_ano(lista_de_veiculos, ano_recebido):
	for veiculo in range( len(lista_de_veiculos) ):
		if ano_recebido == lista_de_veiculos[veiculo]['ano']:
			print('----------------------------\n')
			print('	id:		{}'.format(veiculo) )
			print('	Nome:		{}'.format(lista_de_veiculos[veiculo]['nome']) )
			print('	Ano:		{}'.format(lista_de_veiculos[veiculo]['ano']) )
			print('	Montadora:	{}'.format(lista_de_veiculos[veiculo]['montadora']) )
			print('	Faixa de preco:	%.2f'%lista_de_veiculos[veiculo]['preco'])
			print('	Motor:		%.2f\n'%lista_de_veiculos[veiculo]['motor'])

def listar_faixa_preco(lista_de_veiculos, preco_recebido):
	for veiculo in range( len(lista_de_veiculos) ):
		if (lista_de_veiculos[veiculo]['preco'] >= preco_recebido-10000)and(lista_de_veiculos[veiculo]['preco'] <= preco_recebido+10000):
			print('----------------------------\n')
			print('	id:		{}'.format(veiculo) )
			print('	Nome:		{}'.format(lista_de_veiculos[veiculo]['nome']) )
			print('	Ano:		{}'.format(lista_de_veiculos[veiculo]['ano']) )
			print('	Montadora:	{}'.format(lista_de_veiculos[veiculo]['montadora']) )
			print('	Faixa de preco:	%.2f'%lista_de_veiculos[veiculo]['preco'])
			print('	Motor:		%.2f\n'%lista_de_veiculos[veiculo]['motor'])

def listar_por_motor(lista_de_veiculos, motor_recebido):
	for veiculo in range( len(lista_de_veiculos) ):
		if lista_de_veiculos[veiculo]['motor'] == motor_recebido:
			print('----------------------------\n')
			print('	id:		{}'.format(veiculo) )
			print('	Nome:		{}'.format(lista_de_veiculos[veiculo]['nome']) )
			print('	Ano:		{}'.format(lista_de_veiculos[veiculo]['ano']) )
			print('	Montadora:	{}'.format(lista_de_veiculos[veiculo]['montadora']) )
			print('	Faixa de preco:	%.2f'%lista_de_veiculos[veiculo]['preco'])
			print('	Motor:		%.2f\n'%lista_de_veiculos[veiculo]['motor'])
			
#montadoras
def acrecentar_montadora(nome_montadora, nome_pais, qtd_carros=0):
	montadora = {
		'nome': nome_montadora,
		'pais': nome_pais,
		'carros': qtd_carros
	}

	return montadora

def listar_montadoras(lista_de_montadoras):

	print('Numero de montadoras cadastradas: %d'%len(lista_de_montadoras) )

	for montadora in range( len(lista_de_montadoras) ):
		print('----------------------------------------\n')
		print('	Id:			{}'.format(montadora) )
		print('	Nome:			{}'.format(lista_de_montadoras[montadora]['nome']) )
		print('	pais:			{}'.format(lista_de_montadoras[montadora]['pais']) )
		print('	carros:			{}\n'.format(lista_de_montadoras[montadora]['carros']) )

def pesquisar_nome_montadora(lista , nome_recebido):
	for montadora in range( len(lista) ):
		if nome_recebido in lista[montadora]['nome']:
			print('----------------------------------------\n')
			print('	Id:		{}'.format(montadora) )
			print('	Nome:		{}'.format(lista[montadora]['nome']) )
			print('	pais:		{}'.format(lista[montadora]['pais']) )
			print('	carros:		{}\n'.format(lista[montadora]['carros']) )

def remover_montadora(lista_de_veiculos, lista_de_montadoras, id_recebida):
	for montadora in range( len(lista_de_montadoras) ):
		if(id_recebida == montadora):
			if (lista_de_montadoras[id_recebida]['carros']==0):
				atualizar_veiculos(lista_de_veiculos, lista_de_montadoras[montadora]['nome'])
				lista_de_montadoras.pop(montadora)
				return True
	return False

def atualizar_veiculos(lista_de_veiculos, nome_montadora, alteracao):
	for veiculo in range( len(lista_de_veiculos) ):
		if lista_de_veiculos[veiculo]['montadora'] == nome_montadora:
			lista_de_veiculos[veiculo]['montadora'] = alteracao

def verifica_montadora(lista_de_montadoras, nome_montadora):
	for i in range( len(lista_de_montadoras) ):
		if nome_montadora == lista_de_montadoras[i]['nome']:
			return False
	return True

def pesquisa_valida(lista, nome_recebido):
	bol = False
	for montadora in range( len(lista) ):
		if nome_recebido in lista[montadora]['nome']:
			bol = True

	return bol

def editar_montadora(lista_de_montadoras, lista_de_veiculos, id_recebida, chave, alteracao):
	lista_de_montadoras[id_recebida][chave] = alteracao
	atualizar_veiculos(lista_de_veiculos, lista_de_veiculos[id_recebida]['montadora'], alteracao)

def incrementador_de_veiculos(bd_montadoras, nome_montadora):
	for montadora in range( len(bd_montadoras) ):
		if nome_montadora == bd_montadoras[montadora]['nome']:
			bd_montadoras[montadora]['carros'] += 1
	return bd_montadoras

def decrementador_de_veiculos(lista_de_montadoras, lista_de_veiculos, nome_montadora):
	for montadora in range( len(lista_de_montadoras) ):
		if nome_montadora == lista_de_montadoras[montadora]['nome']:
			lista_de_montadoras[montadora]['carros'] -= 1
	return lista_de_montadoras

def salvar_veiculos(lista_de_veiculos):
	arquivo = open('veiculos.txt', 'w')

	for veiculo in lista_de_veiculos:
		arquivo.writelines( str(veiculo) + '\n' )
	arquivo.close()

def salvar_montadoras(lista_de_montadoras):
	arquivo = open('montadoras.txt', 'w')

	for montadora in lista_de_montadoras:
		arquivo.writelines( str(montadora) + '\n' )
	arquivo.close()