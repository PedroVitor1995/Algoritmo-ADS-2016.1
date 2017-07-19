#__*__  encoding:utf8 __*__
"""10. Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave
pode levantar vôo ou não. Considere os seguintes critérios:
· O peso de decolagem da aeronave é sempre igual a 500.000 kg;
· O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos
passageiros;
· O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
· A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
· O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
· O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso
estimado de 10kg.
O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
mensagem indicando a liberação da decolagem ou não."""
def main():
	quantidade_passageiros = 0
	quantidade_volumes = 0
	volume_bagagens = 0
	peso_total_passageiros = 0
	peso_decolagem = 0
	peso_total_carga = 0
	peso_dos_passageiros = 0

	peso_combustivel = 10000 * 1.5

	numero_containers = input('Digite o numero de de containers: ')
	for i in range(1,numero_containers+1):
		peso_containers = input('Digite o peso do containers:')
		peso_total_carga = peso_total_carga + peso_containers

	while True:
		numero_bilhete = input('Digite o numero do bilhete do passageiro: ')
		if numero_bilhete <= 0:
			break
		else:
			quantidade_passageiros = quantidade_passageiros + 1
			quantidade_bagagens = input('Digite a quantidade de bagagens: ')
			peso_passageiro = input('Digite o peso do passageiro: ')
			quantidade_volumes = quantidade_volumes + 1
			quantidade_passageiros = quantidade_passageiros + 1
			peso_total_passageiros = peso_total_passageiros + peso_passageiro
			volume_bagagens = volume_bagagens + (quantidade_bagagens * 10)
			peso_dos_passageiros = peso_total_passageiros + volume_bagagens

	peso_decolagem = peso_combustivel + peso_total_carga + peso_dos_passageiros
	if peso_decolagem >= 500000:
		print('liberado a decolagem')
	else:
		print('negado a decolagem')



if __name__ == '__main__':
	main()