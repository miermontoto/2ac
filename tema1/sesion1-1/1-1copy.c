#include <stdio.h>
#include <string.h>
#include <assert.h>

void copy(char *source, char *destination, unsigned int lengthDestination) {
	for(int i = 0; source[i] != '\0' ; i++) {
		destination[i] = source[i];
	}

	assert(i + 1 == lengthDestination);
	destination[i+1] = '\0';
}

int main() {
	unsigned int destinationLength = 6;
	char b[destinationLength];
	char *a = "prueba";

	copy(&a, &b, destinationLength);
	printf("%s %s", a, b);
}
