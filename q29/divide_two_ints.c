#include <math.h>

int divide(int dividend, int divisor) {

    // edge cases 
    if (divisor == 1) return dividend;
    if (divisor == -1) {
        if (dividend == -2147483648) return 2147483647;
        else return 0-dividend;
    }

    int quotient = 0;
    int negative = 0;  // flag for sign of quotient 
    if ((dividend < 0 && divisor > 0) || dividend > 0 && divisor < 0) negative = 1;

    int ndividend = dividend == -2147483648 ? 2147483647 : abs(dividend);
    int ndivisor = abs(divisor);
    while (ndividend >= ndivisor) {
        ndividend -= ndivisor;
        quotient++;
    }

    if (negative) return 0-quotient;
    return quotient;
}