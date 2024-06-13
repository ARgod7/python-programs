import random


class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res
        

    def getRandom(self) -> int:
        if self.numList:
            return random.choice(self.numList)
        else: return -1

obj = RandomizedSet()
a1 = obj.insert(3)
a2 = obj.insert(1)
a3 = obj.remove(2)