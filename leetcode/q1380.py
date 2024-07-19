# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

def luckyNumbers (matrix: list[list[int]]) -> list[int]:
        row , col = len(matrix) , len(matrix[0])
        res = []
        row_min = set()
        for r in range(row):
            row_min.add(min(matrix[r]))
        col_max = set()
        for c in range(col):
            cur = matrix[0][c]
            for r in range(row):
                cur = max(cur, matrix[r][c])
            col_max.add(cur)
        for n in row_min:
            if n in col_max:
                res.append(n)
        return res


        