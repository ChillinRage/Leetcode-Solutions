class Solution {
    
    List<List<Integer>> levels;
    
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        
        // initialise List of Lists
        levels = new ArrayList<>();
        
        // get height of tree and initialise corresponding number of lists
        int tree_height = get_depth(root, 1);
        for (int i = 0; i < tree_height; i++) {
            levels.add( new ArrayList<>() );
        }
        
        // traverse all nodes
        traverse(root, tree_height - 1);
        
        return levels;
    }
    
    public void traverse(TreeNode root, int height) {
        if (root == null) { return; }
        
        // add value to current level
        levels.get(height).add(root.val);
        
        // traverse left and right subtrees
        traverse(root.left,  height - 1);
        traverse(root.right, height - 1);
    }
    
    public int get_depth(TreeNode root, int height) {
        if (root == null) { return height - 1; }
        
        return Math.max(
            get_depth(root.left,  height + 1), 
            get_depth(root.right, height + 1)
        );
    }
}