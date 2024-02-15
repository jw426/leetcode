class Solution {
    public String longestPalindrome(String s) {

        if (s.length() == 0) return s; 

        float max_len = 1f, mid_idx = 0f;
        for (float i = 0; i < s.length(); i+=0.5) {
            int new_exp = expand(s, i);
            System.out.println(new_exp);

            if (max_len < new_exp) {
                max_len = new_exp;
                mid_idx = i;
            }
        }
        
        int lower_idx = (int)Math.ceil(mid_idx - max_len/2);
        System.out.println(max_len);
        return s.substring(lower_idx, lower_idx + (int)max_len);

    }

    public int expand(String s, float i) {

        int l, r;
        if (i % 1 == 0) {
            l = r = (int)i;
        } else {
            l = (int)(i - 0.5f);
            r = (int)(i + 0.5f);
        }

        while (l >= 0 && r < s.length()) {

            if (s.charAt(l) == s.charAt(r)) {
                l--; r++;
            } else break;
        }

        return r-l-1;
    }
}