"""22. Leia a hora do inicio de um jogo e a hora de fim do jogo cada hora e composta por 2 variaveis inteiras
hora e minuto. Calcule e escreva a duracao do jogo horas e minutos sabendo se que o tempo
maximo de duracao do jogo e de 24 horas e que ele pode iniciar se em um dia e terminar no dia
seguinte."""

print('Digite a hora do inicio do jogo ')
hora_inicio,minuto_inicio = input('\nHora: '),input('\nMinutos: ')
print('\nDigite a hora do fim do jogo ')
hora_fim,minuto_fim = input('\nHora: '),input('\nMinutos: ')

if hora_inicio < hora_fim:
	duracao_hora = hora_fim - hora_inicio
else:
	duracao_hora = hora_inicio - hora_fim

if minuto_inicio < minuto_fim:
	duracao_minuto = minuto_fim - minuto_inicio
else:
	duracao_minuto = minuto_inicio - minuto_fim

print('\nO jogo deve duracao de %d horas e %d minutos ') % (duracao_hora,duracao_minuto)

