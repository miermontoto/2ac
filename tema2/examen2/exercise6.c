#include <stdio.h>
#include <string.h>

int main()
{
	int  value = 5;
	int *varData = NULL;
	*varData = 5;
	memcpy(varData, &value, sizeof(int) );
	printf("P: %ld\n", (long) varData);
}

