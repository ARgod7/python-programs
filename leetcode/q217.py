from typing import Counter


def containsDuplicate(nums: list[int]) -> bool:
        count = Counter(nums)
        for i in count.values():
            if i>1:
                return True
            
        return False

print(containsDuplicate([1,2,3,4]))