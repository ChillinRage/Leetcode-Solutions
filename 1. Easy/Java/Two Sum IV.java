// NOTE: MIGHT NOT WORK WITH BST WITH DUPLICATES
class Solution {
    TreeNode main_root;
    
    public boolean findTarget(TreeNode root, int k) {
        main_root = root;
        return recurse_findTarget(root, k);
    }
    
    public boolean recurse_findTarget(TreeNode root, int k) {
        if (root == null) { return false; }
        
        // traverse left and right subtrees
        if (recurse_findTarget(root.left,  k)) { return true; }
        if (recurse_findTarget(root.right, k)) { return true; }
        
        // handle using same element
        if ((root.val + root.val) == k) {
            return false;
        } else {
            return search(main_root, k - root.val);
        }
    }
    
    public static boolean search(TreeNode root, int target) {
        if (root == null) { return false;}
        
        if (root.val == target) { return true; }
        
        else if (root.val > target) { // search left subtree
            return search(root.left, target);
        } else { // search right subtree
            return search(root.right, target);
        }
    }
}