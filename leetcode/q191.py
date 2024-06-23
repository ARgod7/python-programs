from collections import Counter


def hammingWeight(n: int) -> int:
        n = bin(n)[2:]
        count = Counter(n)
        a = count['1']
        return count[1]

print(hammingWeight(11))