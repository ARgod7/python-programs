def restoreMatrix(rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        rows = len(rowSum)
        cols = len(colSum)

        res = [[0] * cols for _ in range(rows)]
        i, j = 0, 0

        while i < rows and j < cols:
            res[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return res
        # row , col = len(rowSum) , len(colSum)
        # res = [[0]*col for _ in range(row)]
        # for r in range(row):
        #     res[r][0] = rowSum[r]
        # for c in range(col):
        #     curSum = 0
        #     for r in range(row):
        #         curSum += res[r][c]
        #     r = 0
        #     while curSum > colSum[c]:
        #         diff = curSum - colSum[c]
        #         shift = min(res[r][c],diff)
        #         res[r][c] -= shift
        #         res[r][c+1] += shift
        #         curSum -= shift
        #         r += 1
        # return res