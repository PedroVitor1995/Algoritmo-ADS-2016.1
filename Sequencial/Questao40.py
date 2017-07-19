"""40. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o numero de anos que ele
fuma, o numero de cigarros fumados por dia e o preco de uma carteira (1 carteira tem 20 cigarros)."""

anos = input ('Digite o numero de anos que ele fuma: ')
numero_dia = input ('\nDigite o numero de cigarros fumados por dia: ')
preco_carteira = input ('\nDigite o o preco de uma carteira: ')

dias = anos * 365
total_cigarros = numero_dia * dias
preco_cigarro = float(preco_carteira) / 20
total_gasto = total_cigarros * preco_cigarro

print ('\nO total a pagar pelo fumante em %d anos e %.2f reais ') % (anos,total_gasto)