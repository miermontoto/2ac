#include <stdio.h>

#define NUM_ELEMENTS 7

int add(int x[], int l) {
	int a = 0;
	for(int i = 0; i < l; i++) a = a + x[i];
	return a;
}

int main() {
	int vector[NUM_ELEMENTS] = {2, 5, -2, 9, 12, -4, 3};
	int result;

	result = add(vector, NUM_ELEMENTS);
	printf("The addition of the contents of the vector is: %d\n", result);
	return 0;
}

