class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visited = defaultdict(int)

        def winner(left, right, turn):
            if left > right:
                return 0
            if (left, right, turn) in visited:
                return visited[(left, right, turn)]
            
            res = 0
            
            if turn == 1:
                res = max(nums[right] + winner(left, right-1, 2), nums[left] + winner(left +  1, right, 2))
            else:
                res = min(winner(left, right - 1, 1), winner(left + 1, right, 1))
            visited[(left, right, turn)] = res

            return res
        p1_score = winner(0, len(nums) - 1, 1)          
        p2_score = winner(0, len(nums) - 1, 2)
        return p1_score >= p2_score
                    
