"""
	Somar Fracoes S = 1/1 + 1/2 ... + 1/N
	Pythonic Way: sum([Fraction(1, i) for i in range(1, input('N: ')+1)])
"""


def main():
    numero = input("Quantas Fracoes? ")
    soma_fracoes(numero)


def soma_fracoes(numero):
    mmc = calcular_mmc_sequencia(numero)
    print 'MMC = %d' % mmc
    numerador_geral = 0
    for i in range(1, numero + 1):
        print '%d/%d + ' % (1, i),
        numerador_geral = numerador_geral + ((mmc / i) * 1)

    print 'Resultado = %d/%d == %.2f' % (numerador_geral, mmc, (numerador_geral/float(mmc)))


def calcular_mmc_sequencia(limite):
    # Calcular MMC
    mmc = 1
    while True:
        encontrou = True
        for i in range(1, limite + 1):
            if mmc % i != 0:
                encontrou = False
                break

        if encontrou == True:
            break
        mmc = mmc + 1
    return mmc


if __name__ == '__main__':
    main()
