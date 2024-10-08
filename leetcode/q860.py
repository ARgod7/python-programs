def lemonadeChange(self, bills: list[int]) -> bool:
        five , ten = 0 , 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                five -= 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
        return True
            