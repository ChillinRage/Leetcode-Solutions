class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        
        while (low <= high) {
            if (nums[(low + high) / 2] == target) {
                return (low + high) / 2;
            } else if (nums[(low + high) / 2] > target) {
                high = ((low + high) / 2) - 1;
            } else {
                low = ((low + high) / 2) + 1;
            }
        }
        
        return -1;
    }
}