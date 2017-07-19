def main():
	N = input('N: ')
	mmc = mmc_sequencia(N)
	print 'MMC: ', mmc
	numerador_geral = 0
	for i in range(1, N+1):
		print '1/%d +' % i, 
		numerador_geral += (mmc / i) * 1
	print '== {}/{} == {}'.format(numerador_geral, mmc, numerador_geral/float(mmc))

def mmc_sequencia(numero):
	mmc = 1
	while True:
		eh_mmc = True
		for i in range(1,numero+1):
			if mmc % i != 0:
				eh_mmc = False
				break
		if eh_mmc == True:
			return mmc
		mmc = mmc + 1

if __name__ == '__main__':
	main()