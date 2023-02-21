class Solution {
    int max_sum; // global variable to keep track of max possible sum
    
    public int maxPathSum(TreeNode root) {
        max_sum = Integer.MIN_VALUE;
        searchall(root);
        return max_sum;
    }
    
    public int searchall(TreeNode root) {
        if (root == null) { return 0; }
        
        int left_path  = searchall(root.left);
        int right_path = searchall(root.right);
        int best_path  = max(left_path, right_path);
        
        max_sum = max( // all possible paths given current root
            root.val,
            root.val + left_path + right_path,
            root.val + best_path,
            max_sum
        );
        
        // pick one path to connect with parent nodes
        return max(root.val, root.val + best_path);
    }
    
    public static int max(int...nums) {
        int maxm = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (maxm < nums[i]) {
                maxm = nums[i];
            }
        }
        
        return maxm;
    }
}