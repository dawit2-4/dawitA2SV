class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        if n <= k:
            return max(energy)
        
        prefix = energy[:]
        for i in range(n-k-1, -1, -1):
            prefix[i] += prefix[i+k]
        
        return max(prefix)