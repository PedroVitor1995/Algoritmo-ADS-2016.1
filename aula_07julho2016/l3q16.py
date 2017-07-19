"""
Gerar Fibonacci com qtd de Elementos.
"""


def main():
    qtd = input('Qtd: ')
    item1 = 0
    item2 = 1
    print item1, item2,
    for i in range(qtd - 2):
        atual = item1 + item2
        item1 = item2
        item2 = atual
        print atual,


if __name__ == '__main__':
    main()
