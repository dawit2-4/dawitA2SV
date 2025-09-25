class Solution:
    def canCross(self, stones: List[int]) -> bool:
        store = {}

        def dp(end, val):
            if end == len(stones) - 1:
                return True
            # if end >= len(stones):
            #     return False
            state = (end, val)
            if state in store:
                return store[state]
            
            
            temp = False
            for i in range(end+1, len(stones)):
                if stones[i] == stones[end] + val:
                    temp = temp or dp(i, val)
                if stones[i] == stones[end] + val + 1:
                    temp = temp or dp(i, val + 1)
                if stones[i] == stones[end] + val - 1:
                    temp = temp or dp(i, val - 1)
            store[state] = temp
            return temp
        return dp(0, 0)