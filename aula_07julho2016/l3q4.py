"""
    Progressao Geometrica
"""
def main():
    inicio = input('Inicio: ')
    limite = input("Limite: ")
    razao = input("Razao: ")
    atual = 1
    print atual,
    ultimo = atual
    for i in range(inicio, limite + 1):
        atual = ultimo * razao
        if atual <= limite:
            print atual,
            ultimo = atual
        else:
            break


if __name__ == '__main__':
    main()
