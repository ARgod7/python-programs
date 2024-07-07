def numWaterBottles(numBottles: int, numExchange: int) -> int:
        count = 0
        empty = 0
        while True:
            count += numBottles
            empty += numBottles
            numBottles = 0
            numBottles = empty // numExchange
            empty = empty % numExchange
            if numBottles == 0:
                break
        return count
numWaterBottles(15,4)
