#include <string>
#include <limits.h>
#include <iostream>

class Solution {
public:
    int reverse(int x) {

        std::string int_str = std::to_string(x);
        int reversed = 0, digit = 0;

        for (int i = int_str.length() - 1; i >= 0; i--) {

            if (int_str[i] == '-') {
                reversed *= -1; 
                break;
            }

            digit = int(int_str[i]) - 48;
            if(reversed>(INT_MAX/10)||reversed<(INT_MIN/10)) return 0;
            reversed = reversed * 10 + digit; 
        }
        return reversed;
    }
};