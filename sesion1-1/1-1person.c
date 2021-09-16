#include <stdio.h>
#include <string.h>

struct _Person {
	char name[30];
	int heightcm;
	double weightkg;
};

typedef struct _Person Person;

int main(int argc, char* argv[]) {
	Person Peter;
	strcpy(Peter.name, "Peter");
	Peter.heightcm = 175;
	Peter.weightkg = 175;

	printf("%s weighs %f kg and is %d cm tall.\n",
		 Peter.name, Peter.weightkg, Peter.heightcm);
}
