class Solution {
    public int reverse(int x) {

        String int_str = Integer.toString(x);
        int reversed = 0;
        int digit = 0;
        
        for (int i = int_str.length() - 1; i >= 0; i--) {
            if (int_str.charAt(i) == '-') {
                reversed *= -1; 
                break; 
            }

            digit = int_str.charAt(i) - '0';
            if (reversed > Integer.MAX_VALUE / 10 || reversed == Integer.MAX_VALUE / 10 && digit > 7) return 0;
            if (reversed < Integer.MIN_VALUE / 10 || reversed == Integer.MIN_VALUE / 10 && digit > 8) return 0;

            reversed = reversed * 10 + digit;  
        }
        return reversed; 
    }
}