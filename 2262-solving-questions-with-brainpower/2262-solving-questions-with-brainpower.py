class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        store = {}
        def dp (i):
            if i >= len(questions):
                return 0
            if i in store:
                return store[i]

            take = questions[i][0] + dp(i + questions[i][1] + 1)
            notTake = dp(i+1)

            store[i] = max(take, notTake)
            return store[i]
        return dp(0)

