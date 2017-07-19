"""
>>> soma(2,2)
4
>>> soma(3,2)
5
>>> subtracao(10,2)
8
>>> subtracao(8,5)
3
"""

def main():
	print 'Main is running...'
	print soma(1,1)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

if __name__ == '__main__':
	main()

