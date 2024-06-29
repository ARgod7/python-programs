def permute(nums: list[int]) -> list[list[int]]:
        # perms = [[]]

        # for n in nums:
        #     new_perms = []
        #     for p in perms:
        #         for i in range(len(p) + 1):
        #             p_copy = p.copy()
        #             p_copy.insert(i,n)
        #             new_perms.append(p_copy)
        #     perms = new_perms
        # return perms
        res = []
        
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack(curr)
                    curr.pop()
                    
                
        backtrack([])
        return res
        