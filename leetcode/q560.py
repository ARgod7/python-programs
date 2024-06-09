# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

def subarraySum(nums: list[int], k: int) -> int:
        res, curSum, n = 0, 0, len(nums)
        d = {0: 1}
        for n in nums:
            curSum += n
            if curSum - k in d:
                res += d[curSum-k]
            d[curSum] = d.get(curSum, 0) + 1
        return res