#include <stdio.h>

int main() {
	int x = 1;
	const char *p = (const char*) &x;
	if (*p) printf("Little-endian\n");
	else printf("Big-endian\n");

	return 0;
}
