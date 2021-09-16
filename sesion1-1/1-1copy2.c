// no tengo fuerzas para hacerlo, está copiado de stackoverflow.
#include <stdio.h>
#include <assert.h>

int copy(char * source, char * destination, unsigned int lengthDestination);

int copy(char * source, char * destination, unsigned int lengthDestination)
{
    int i;
    for(i = 0; source[i] != '\0'; i++) {
        destination[i] = source[i];
    }
    assert(i+1 == lengthDestination);
    destination[i+1] = '\0';
    return 0;
}

int main() {
    char * source = "Test number 17"; //Length is 15 counting the null character
    unsigned int destinationLength = 15;
    char destination[destinationLength];
    copy(source, destination, destinationLength);
    printf("The String source is: %s\n", source);
    printf("The String destination is: %s\n", destination);
    return 0;
}
