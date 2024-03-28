#include <math.h>
#include <stdlib.h>

int divide(int dividend, int divisor) {

    // edge cases 
    if (divisor == dividend) return 1;
    if (divisor == 1) return dividend;
    if (divisor == -1) {
        if (dividend == INT_MIN) return INT_MAX;
        else return 0-dividend;
    }

    unsigned int quotient = 0;
    int positive = dividend < 0 == divisor < 0;  // flag for sign of quotient 

    unsigned int ndividend = dividend == INT_MIN ? INT_MAX + 1 : abs(dividend);
    unsigned int ndivisor = divisor == INT_MIN ? INT_MAX + 1 : abs(divisor);

    while (ndividend >= ndivisor) {
        short bt = 0;
        while (ndividend > (ndivisor << (bt+1))) bt++;
        quotient += (1 << bt);
        ndividend -= ndivisor << bt;
    }

    if (quotient == INT_MAX && positive) return INT_MAX;
    return positive ? quotient : 0 - quotient;
}