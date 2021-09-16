#include <stdio.h>
# include "1-1circle.h"

int main() {
	double radius = 3.0;
	double area = circleArea(radius);
	printf("Circle of radius %f has an area of %f\n", radius, area);
	return 0;
}
