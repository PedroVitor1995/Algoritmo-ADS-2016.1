def main():

	quantidade = input()

	for z in range(quantidade):
		sobr_dieta = ''
		cont = 0
		cont2 = 0
		cont3 = 0
		flag = 0
		dieta = raw_input()
		cafe_manha = raw_input()
		almoco = raw_input()

		for i in dieta:

			for y in cafe_manha:
				cont2 = 0
				cont3 = 0
				if y not in dieta:
					cont += 1
				for w in cafe_manha:
					if y == w:
						cont2 +=1
				for z in almoco:
					if y == z:
						cont3 +=1
				if cont2> 1 or cont3>=1:
					flag = 1

			for y in almoco:
				cont2 = 0
				cont3 = 0
				if y not in dieta:
					cont += 1
				for w in almoco:
					if y == w:
						cont2 +=1
				for z in cafe_manha:			
					if y == z:
						cont3 +=1
				if cont2 > 1 or cont3>=1:		
					flag = 2
					
			if i not in cafe_manha and i not in almoco :
				sobr_dieta += i

		sobr_dieta =''.join(sorted(sobr_dieta))	

		if (cont > 0 or flag > 0 or len(dieta)< 1) and (len(almoco) > 0 or len(cafe_manha) > 0):
			print 'CHEATER'
		if cont == 0 and flag == 0:	
			print sobr_dieta

if __name__ == '__main__':
	main()