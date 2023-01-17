class Solution {
    public String intToRoman(int num) {
        String[] letters = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String roman = "";
        int quotient = 0;
        
        for (int i = 0; i < values.length; i++) {
            if (num >= values[i]) {
                quotient = num / values[i];
                num %= values[i];
                
                roman += letters[i].repeat(quotient);
            }
            
        }
        
        return roman;
    }
}