#include <string>
using std::string;

class Solution {

public:
    string convert(string s, int numRows) {
        
        if (numRows <= 1) return s; 

        string pattern("");

        int jump_const = (numRows - 1) * 2; 
        int jump = jump_const; 
        int cur_jump;
        bool inc = true; 

        for (int idx = 0; idx < numRows; idx++) {

            int i = idx; 
            int prev = -1; 
            inc = true; 

            while (i < s.length()) {
                
                if (prev != i) pattern += s[i];
                prev = i; 
                i += inc ? jump : jump_const - jump;
                inc = !inc; 
            }

            jump -= 2; 
        }

        return pattern; 

    }
};