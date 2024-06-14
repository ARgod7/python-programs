def minFallingPathSum(matrix: list[list[int]]) -> int:
        n = len(matrix)

        for r in range(1,n):
            for c in range(n):
                m = matrix[r-1][c]
                l = matrix[r-1][c-1] if c > 0 else float("inf")
                ri = matrix[r-1][c+1] if c < n - 1 else float("inf")
                matrix[r][c] = matrix[r][c] + min(m , l , ri)
        return min(matrix[-1])

minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])