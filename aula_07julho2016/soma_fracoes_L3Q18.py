"""
	Somar Fracoes S = 1/N + 2/N-1 ... + N/1
	Pythonic Way: sum([Fraction(i, N-i+1) for i in range(1, N+1)])
"""
from soma_fracoes_L3Q17 import calcular_mmc_sequencia


def main():
    numero = input('N: ')
    soma_fracoes(numero)


def soma_fracoes(numero):
    mmc = calcular_mmc_sequencia(numero)
    print 'MMC = %d' % mmc
    numerador_resultante = 0
    for i in range(1, numero + 1):
        numerador = i
        denominador = numero + 1 - i
        print '%d/%d + ' % (numerador, denominador),
        numerador_resultante += mmc / denominador * numerador

    print 'Resultado = %d/%d == %.2f' % (numerador_resultante, mmc, (numerador_resultante/float(mmc)))


if __name__ == '__main__':
    main()
