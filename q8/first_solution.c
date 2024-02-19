#include <limits.h>

int myAtoi(char* s) {

    int i = -1; 
    int num = 0; 
    int sign = 1; 

    // removing leading whitespace
    while (s[++i] == ' ');

    // determine sign of integer
    if (s[i] == '-') {
        sign *= -1; 
        i++;
    } else if (s[i] == '+') i++;

    // reading in digits
    while ('0' <= s[i] && s[i] <= '9') {
        if (sign == 1 && (num > INT_MAX / 10 || (num == INT_MAX / 10 && s[i] >= '7'))) return INT_MAX;
        if (sign == -1 && (-1*num < INT_MIN / 10 || (-1*num == INT_MIN / 10 && s[i] >= '8'))) return INT_MIN;
        
        num = num*10 + (s[i++] - '0');
    }

    return num * sign; 
}