class Solution {

    public String convert(String s, int numRows) {
        
        if (numRows <= 1) return s; 

        String pattern = new String("");
        
        int jump_const = (numRows - 1) * 2;
        int jump = jump_const;  
        int cur_jump; 
        boolean inc = true; 

        for (int idx = 0; idx < numRows; idx++) {
        
            int i = idx;
            int prev = -1; 
            inc = true; 

            while (i < s.length()) {
                if (prev != i) pattern += s.charAt(i);
                prev = i;
                i += inc ? jump : jump_const - jump;
                inc = !inc; 
            }

            jump -= 2;  
        }

        return pattern;

    }
}