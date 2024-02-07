#include <unordered_map>

class Solution {

    public:
        int lengthOfLongestSubstring(string s) 
        {
            std::unordered_map<char, int> char_dict = {};
            int max_length = 0; 
            int cur_start = 0; 

            for (int i = 0; i < s.length(); i++) 
            {
                auto last_i = char_dict.find(s.at(i));

                // not recurring
                if (last_i != char_dict.end() && last_i->second >= cur_start) 
                {
                    cur_start = last_i->second + 1;
                }
                
                char_dict.insert_or_assign(s.at(i), i);

                if (i - cur_start + 1 > max_length)
                {
                    max_length = i - cur_start + 1;
                }
            }

            return max_length;            
        }
};