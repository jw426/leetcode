#include <stdio.h>
#include <ctype.h>

void q1(int n);
int main(int argc, char** argv) {

    q1(3);
    q1(5);

    return 0;
}

void q1(int n) {

    printf("QUESTION with %d\n", n);

    for (int i = n-1; i >= 0; i--) {

        for (int k = 0; k < (n-1-i); k++) {
            putchar(' ');
        }
        putchar('v');
        for (int j = 0; j < space_num(n-1-i); j++) {
            putchar(' ');
        }
        putchar('v');putchar('\n');
    } putchar('v'); putchar('\n'); 
}

int space_num(int n ) {

    if (n==0 || n==1) {
        return n;
    } else {
        return 3+2*(n-2);
    }
}