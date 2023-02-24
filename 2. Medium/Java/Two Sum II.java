class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left  = 0;
        int right = numbers.length - 1;
        
        while (left < right) {
            
            // found target
            if ( target == (numbers[left] + numbers[right]) ) {
                return new int[] {left + 1, right + 1};
            }
            
            // find bigger number (left pointer forward once)
            else if ( target > (numbers[left] + numbers[right]) ) {
                left++;
            // find smaller number (right pointer back once)
            } else {
                right--;
            }
        }
        
        // no pair found
        return null;
    }
}