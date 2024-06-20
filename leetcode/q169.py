# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(self, nums: list[int]) -> int:

        nums.sort()
        return nums[len(nums)//2]

        # MAP
        
        # count = Counter(nums)
        # n = (len(nums)//2) + 1
        # for i in count:
        #     if count[i] >= n:
        #         num = i
        # return num

# f = open("user.out", 'w')
# for line in stdin:
#     l = sorted(map(int, line.rstrip()[1:-1].split(',')))
#     print(l[len(l) // 2], file=f)