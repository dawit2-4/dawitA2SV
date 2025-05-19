class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest = []
        for r in range(len(mat)):
            count = 0
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    count += 1
            weakest.append((count,r))
        weakest.sort()
        ans = [w[1] for w in weakest]
        return ans[:k]
        