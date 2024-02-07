import java.util.HashMap;

class Solution {

    public int lengthOfLongestSubstring(String s) {

        HashMap<Character, Integer> char_dict = new HashMap<>();
        int max_length = 0;
        int cur_start = 0;

        for (int i = 0; i < s.length(); i++) {

            if (char_dict.getOrDefault(s.charAt(i), -1) >= cur_start) {
                cur_start = char_dict.get(s.charAt(i)) + 1;
                char_dict.put(s.charAt(i), i);
            } else {
                char_dict.put(s.charAt(i), i);
            }

            if (i - cur_start + 1 > max_length) {
                max_length = i - cur_start + 1;
            }
        }

        return max_length;
        
    }
}