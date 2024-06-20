# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1


def singleNumber(nums: list[int]) -> int:
        # hmap = set()
        # for n in nums:
        #     if n in hmap:
        #         hmap.discard(n)
        #     else:
        #         hmap.add(n)
        # return list(hmap)[0]
        res = 0
        for n in nums:
            res = n ^ res
        return res
        