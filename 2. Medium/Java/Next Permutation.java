class Solution {
    public void nextPermutation(int[] nums) {
        //start from index i = second last index
        
        //if (i:n-1) is reverse sorted,
        //then decrease i by 1
        
        //if (i:n-1) is NOT reverse sorted,
        //then reverse (i+1:n-1) to sorted,
        //swap next larger num in (i+1:n-1) with i
        
        if (nums.length == 1) { // one number only
            return;
        }
        
        int i = nums.length - 2;
        int next_num_index;
        
        while (i >= 0) {
            if (nums[i] < nums[i+1]) { // num after i is bigger
                reverse(nums, i + 1, nums.length - 1);
                next_num_index = next_larger(nums, nums[i], i+1, nums.length - 1);
                swap(nums, i, next_num_index);
                return;
                
            } else {
                i--;
            }
        }
        
        // whole array is in descending
        if (i == -1) {
            reverse(nums, 0, nums.length- 1); // return smallest order
        }
    }
    
    // in-place reversal of array from index [start, end]
    static void reverse(int[] nums, int start, int end) {
        while (start <= end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
    
    // in-place swapping of elements in index i and j
    static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    // find index of next larger number in sorted array[start:end]
    // that is bigger than floor
    static int next_larger(int[] nums, int floor, int start, int end) {
        while (start <= end) {
            if (nums[start] > floor) {
                return start;
            } else {
                start++;
            }
        }
        
        return floor; // cannot find any
    }
}