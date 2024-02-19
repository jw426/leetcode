public class Solution {
    public int MyAtoi(string s) {
        
        int i = 0; 
        int num = 0; 
        int sign = 1; 

        s = s.Trim();
        if (s.Length == 0) return num;

        // determine sign of integer
        if (s[i] == '-') {
            sign *= -1; 
            i++;
        } else if (s[i] == '+') i++;

        for (i = i; i < s.Length; i++) {
            if (s[i] < '0' || s[i] > '9') break;

            if (sign == 1 && (num > Int32.MaxValue / 10 || (num == Int32.MaxValue / 10 && s[i] >= '7'))) return Int32.MaxValue;
            if (sign == -1 && (-1*num < Int32.MinValue / 10 || (-1*num == Int32.MinValue / 10 && s[i] >= '8'))) return Int32.MinValue;
            
            num = num*10 + s[i] - '0';
        }

        return num * sign; 
    }
}