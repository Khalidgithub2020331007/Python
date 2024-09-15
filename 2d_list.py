class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array (list of lists) with dimensions m * n
        a = [[0] * n for _ in range(m)]
        
        # Initialize the first column to 1
        for i in range(m):
            a[i][0] = 1
        
        # Initialize the first row to 1
        for i in range(n):
            a[0][i] = 1
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                a[i][j] = a[i-1][j] + a[i][j-1]
        
        return a[m-1][n-1]
