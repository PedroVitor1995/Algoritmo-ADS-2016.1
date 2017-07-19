#include "stdio.h"

void desc(int numero){
	printf("begin %d\n", numero);
	if (numero == 0){
		printf("FIM\n");
	}else{   
	    printf("%d\n", numero);
	    desc(numero - 1);
	}
	printf("end %d\n", numero);
}

int main(){
	int numero;

	printf("Digite Numero: ");
	scanf("%d", &numero);
	
	desc(numero);
	return 0;
}