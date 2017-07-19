# -*- coding: utf-8 -*-
def main():
	numeros = input().split(' ')
	A = int(numeros[0])
	B = int(numeros[1])
	C = int(numeros[2])
	D = int(numeros[3])
	qtd = 0
	if (B - C) < A and A < (B + C) and (A - C) < B and B < (A + C) and \
	(A - B) < C and C < (A + B):
		qtd += 1
	elif (C - D) < A and A < (C + D) and (A - D) < C and C < (A + D) and \
	(A - C) < D and D < (A + C):
		qtd += 1
	elif (C - D) < B and B < (C + D) and (B - D) < C and C < (B + D) and \
	(B - C) < D and D < (B + C):
		qtd += 1
	elif (B - D) < A and A < ( B + D) and (A - D) < B and B < (A + D) and \
	(A - B) < D and D < (A + B):
		qtd += 1
		
	if qtd > 0:
		print('S')
	else:
		print('N')
if __name__ == '__main__':
	main()