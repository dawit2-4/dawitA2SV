class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = defaultdict(int)           
        for num in arr:
            calc = num%k
            remainder[calc] += 1
        
        for i in range(k):
            if i == 0:
                if remainder[i] % 2 != 0:
                    return False
            else:
                if remainder[i] != remainder[k-i]:
                    return False
                
        
        return True
 