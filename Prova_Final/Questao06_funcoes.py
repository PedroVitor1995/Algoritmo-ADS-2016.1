def inicializar_alunos():
	alunos = []
	alunos_importacao = open('tabela_alunos.csv', 'r')
	for linha in alunos_importacao:
		dados = linha.strip().split(';')
		if dados[1] == 'A':
			media = float(((float(dados[2])+float(dados[3]))/2)+0.5)
			if media >= 7.0:
				aluno = {
						'nome': dados[0], 
		                'situacao': 'APROVADO',
		                'nota1': float(dados[2]),
		                'nota2': float(dados[3]),
		                'media': media
		                }
			elif media >= 4.0 and media < 7.0:
				aluno = {
						'nome': dados[0], 
		                'situacao': 'PROVA FINAL',
		                'nota1': float(dados[2]),
		                'nota2': float(dados[3]),
		                'media': media
		                }
			else:
				aluno = {
						'nome': dados[0], 
		                'situacao': 'REPROVADO',
		                'nota1': float(dados[2]),
		                'nota2': float(dados[3]),
		                'media': media
		                }
		else:
			media = (float(dados[2])+float(dados[3]))/2
			aluno = {
					'nome': dados[0], 
		            'situacao': 'EVADIDO',
		            'nota1': float(dados[2]),
		            'nota2': float(dados[3]),
		            'media': media
		            }
		alunos.append(aluno)
	alunos_importacao.close()
	return alunos
def listar_notas_media_situacao(lista_de_alunos):
	for aluno in range(len(lista_de_alunos)):
		print('	Notas: %f e %f'%(lista_de_alunos[aluno]['nota1'],\
		lista_de_alunos[aluno]['nota2']))
		print('	Media calculada: %f'%(lista_de_alunos[aluno]['media']))
		print('	Situacao: {}'.format(lista_de_alunos[aluno]['situacao']))
def listar_contagem_e_percentual_por_situação(lista_de_alunos):
	qtd_total = 0
	qtd_aprovados = 0
	qtd_prova_final = 0
	qtd_reprovados = 0
	qtd_evadidos = 0
	for aluno in range(len(lista_de_alunos)):
		if lista_de_alunos[aluno]['situacao'] == 'APROVADO':
			qtd_aprovados += 1
		elif lista_de_alunos[aluno]['situacao'] == 'REPROVADO':
			qtd_reprovados += 1
		elif lista_de_alunos[aluno]['situacao'] == 'PROVA FINAL':
			qtd_prova_final += 1
		elif lista_de_alunos[aluno]['situacao'] == 'EVADIDO':
			qtd_evadidos += 1
		qtd_total += 1
	percentual_aprovados = (qtd_aprovados * 100) / qtd_total 
	percentual_prova_final = (qtd_prova_final * 100) / qtd_total 
	percentual_reprovados = (qtd_reprovados * 100) / qtd_total
	percentual_evadidos =  (qtd_evadidos * 100) / qtd_total
	print('Alunos aprovados')
	print('Quantidade dos alunos: %d '% qtd_aprovados)
	print('Percentual dos alunos: %.2f %%\n'%percentual_aprovados)
	print('Alunos de prova final')
	print('Quantidade dos alunos: %d '% qtd_prova_final)
	print('Percentual dos alunos: %.2f %%\n'%percentual_prova_final)
	print('Alunos reprovados')
	print('Quantidade dos alunos: %d '% qtd_reprovados)
	print('Percentual dos alunos: %.2f %%\n'%percentual_reprovados)
	print('Alunos evadidos')
	print('Quantidade dos alunos: %d '% qtd_evadidos)
	print('Percentual dos alunos: %.2f %%'%percentual_evadidos)
def listar_tabela_ordenada_por_nota_decrescente_todos(lista_de_alunos):
	for i in range(len(lista_de_alunos)):
		aux = i
		for j in range(len(lista_de_alunos)-1):
			if lista_de_alunos[j]['media'] <= lista_de_alunos[aux]['media']:
				aux = j
			lista_de_alunos[aux], lista_de_alunos[i] = lista_de_alunos[i], lista_de_alunos[aux]
	for aluno in range(len(lista_de_alunos)):
		nome_completo = lista_de_alunos[aluno]['nome'].split(' ')
		nome_sobrenome = nome_completo[0] + ' ' + nome_completo[-1]
		print('Nome: {}'.format(nome_sobrenome ))
		print('Media: %f'%lista_de_alunos[aluno]['media'])
def listar_tabela_ordenada_por_nota_decrescente_quantidade_desejadas(lista_de_alunos,quantidade_desejadas):
	for i in range(len(lista_de_alunos)):
		aux = i
		for j in range(len(lista_de_alunos)-1):
			if lista_de_alunos[j]['media'] <= lista_de_alunos[aux]['media']:
				aux = j
			lista_de_alunos[aux], lista_de_alunos[i] = lista_de_alunos[i], lista_de_alunos[aux]
	for aluno in range(quantidade_desejadas):
		nome_completo = lista_de_alunos[aluno]['nome'].split(' ')
		nome_sobrenome = nome_completo[0] + ' ' + nome_completo[-1]
		print('Nome: {}'.format(nome_sobrenome))
		print('Media: %f'%lista_de_alunos[aluno]['media'])
def buscar_alunos_por_parte_nome(lista_de_alunos,parte_nome):
	for aluno in range(len(lista_de_alunos)):
		if parte_nome.upper() in lista_de_alunos[aluno]['nome'].upper():
			print('Aluno: {}'.format(lista_de_alunos[aluno]['nome']))
			print('Media: %f'%(lista_de_alunos[aluno]['media']))
def buscar_alunos_por_faixa_nota(lista_de_alunos,faixa_nota):
	contador = 0
	for aluno in range(len(lista_de_alunos)):
		if lista_de_alunos[aluno]['media'] >= int(faixa_nota) \
		and lista_de_alunos[aluno]['media'] <= (int(faixa_nota) + 1):
			print('	Aluno:  {}'.format(lista_de_alunos[aluno]['nome']))
			print('	Media:	%f'%(lista_de_alunos[aluno]['media']))
			contador += 1
	if contador == 0:
		print('Nao tem alunos nessa faixa de notas')
def buscar_alunos_A_por_media_(lista_de_alunos,faixa_nota_a):
	contador = 0
	for aluno in range(len(lista_de_alunos)):
		if lista_de_alunos[aluno]['situacao'] != 'EVADIDO':
			if lista_de_alunos[aluno]['media'] >= int(faixa_nota_a) \
			and lista_de_alunos[aluno]['media'] <= (int(faixa_nota_a) + 1):
				print('	Aluno:  {}'.format(lista_de_alunos[aluno]['nome']))
				print('	Media:	%f'%(lista_de_alunos[aluno]['media']))
				contador += 1
	if contador == 0:
		print('Nao tem alunos ativos com essa faixa de media')
def salvar_alunos(alunos):
	arquivo_alunos = open('bd_alunos.txt', 'w')
	for aluno in alunos:
		arquivo_alunos.write(str(aluno) + '\n')
	arquivo_alunos.close()