import copy


def rotate(matrix: list[list[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        y = copy.deepcopy(matrix)
        
        for r in range(n):
            for c in range(n):
                matrix[r][c] = y[n-1-c][r]
        print(matrix)
rotate([[1,2,3],[4,5,6],[7,8,9]])

        