#include <math.h>

int divide(int dividend, int divisor) {

    // edge cases 
    if (divisor == 1) return dividend;
    if (divisor == -1) {
        if (dividend == -2147483648) return 2147483647;
        else return 0-dividend;
    }

    int quotient = 0;
    int positive = dividend < 0 == divisor < 0;  // flag for sign of quotient 

    unsigned int ndividend = abs(dividend);
    unsigned int ndivisor = abs(divisor);
    while (ndividend >= ndivisor) {
        ndividend -= ndivisor;
        quotient++;
    }

    if (positive) return quotient;
    return 0 - quotient;
}