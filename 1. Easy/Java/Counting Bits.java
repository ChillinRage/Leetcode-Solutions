class Solution {
    public int[] countBits(int n) {
        int[] output = new int[n + 1];
        int power;
        int closest;
        
        output[0] = 0;      //initialise num 0 with 0 bit.
        if (n > 0) {
            output[1] = 1;  //initialise num 1 with 1 bit.
        }
        
        for (int i = 2; i <= n; i++) {
            power = log2(i);
            closest = (int)(Math.pow(2, power));
            
            if (closest == i) {
                output[i] = 1;
                
            } else {
                output[i] = 1 + output[i - closest];
            }
        }
        
        return output;
    }
    
    public int log2(int n) { return (int)(Math.log(n) / Math.log(2)); }
}