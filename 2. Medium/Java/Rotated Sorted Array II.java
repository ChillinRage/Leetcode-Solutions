class Solution {
    public boolean search(int[] nums, int target) {
        // not in array's range
        if ((target < nums[0]) && (target > nums[nums.length - 1])) {
            return false;
        }
        
        // check left portion of array
        if (target >= nums[0]) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] < nums[0]) { break; }      // end of left portion
                else if (nums[i] > target)  { break; } // not in left portion
                else if (nums[i] == target) { return true; }  
            }
            
        // check right portion of array
        } else {
            for (int i = nums.length - 1; i >= 0; i--) {
                if (nums[i] > nums[nums.length - 1]) { break; } // end of right portion
                else if (nums[i] < target)  { break; }          // not in right portion
                else if (nums[i] == target) { return true; }  
            }
        }
        
        return false;
    }
}