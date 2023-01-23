class Solution {
    
    private int row_length;
    private int col_length;
    private int[][] dupe_matrix;
    
    public void setZeroes(int[][] matrix) {
        row_length = matrix.length;
        col_length = matrix[0].length;
        dupe_matrix = new int[row_length][col_length];
        
        for (int r = 0; r < row_length; r++) {
            for (int c = 0; c < col_length; c++) {
                if (matrix[r][c] == 0) {
                    setRow(dupe_matrix, r);
                    setCol(dupe_matrix, c);
                }
            }
        }
        
        for (int r = 0; r < row_length; r++) {
            for (int c = 0; c< col_length; c++) {
                if (dupe_matrix[r][c] == 1) {
                    matrix[r][c] = 0;
                }
            }
        }
    }
    
    private void setRow(int[][] matrix, int row) {
        for (int i = 0; i < col_length; i++) {
            matrix[row][i] = 1;
        }
    }
    
    private void setCol(int[][] matrix, int col) {
        for (int i = 0; i < row_length; i++) {
            matrix[i][col] = 1;
        }
    }
}