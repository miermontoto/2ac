#include <stdio.h>
#include <string.h>

struct _Person {
	char name[30];
	int heightcm;
	double weightkg;
};

typedef struct _Person Person;
typedef Person* PPerson;

int main(int argc, char* argv[]) {
	Person Javier;
	PPerson pJavier;

	pJavier = &Javier;
	Javier.heightcm = 180;
	Javier.weightkg = 84.0;
	pJavier -> weightkg = 83.2;
	return 0;
}
