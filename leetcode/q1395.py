def numTeams(rating: list[int]) -> int:
        res = 0
        for idx, j in enumerate(rating):
            small_left = small_right = big_left = big_right = 0
            for i in rating[:idx]:
                if i < j:
                    small_left += 1
                else:
                    big_left += 1
            for k in rating[idx+1:]:
                if j < k:
                    big_right += 1
                else:
                    small_right += 1
            res += small_left * big_right + big_left * small_right
        return res