class Solution {
    TreeNode root;
    
    public int kthSmallest(TreeNode root, int k) {
        this.root = root; // Main root of BST
        int k_smallest = 0;
        
        // remove smallest number in current tree k times
        for (int i = 0; i < k; i++) {
            k_smallest = DeleteSmallest(null, this.root);
        }
        
        return k_smallest;
    }
    
    public int DeleteSmallest(TreeNode parent, TreeNode root) {
        // empty tree
        if (root == null) { return -1; }
        
        else if (root.left != null) { // go left subtree
            return DeleteSmallest(root, root.left);
        }
        
        // current node is smallest
        if (parent == null) { // root is the smallest
            this.root = root.right;
            return root.val;
        } else {
            if (parent.val > root.val) { // parent's left child
                parent.left = root.right;
            } else {
                parent.right = root.right;
            }
            
            return root.val;
        }
        
    }
}