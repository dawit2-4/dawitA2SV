class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        for i in range(len(edges)):
            in_degree[edges[i][1]] += 1
        champ = []
        for i in range(n):
            if in_degree[i] == 0:
                champ.append(i)
        if len(champ) == 1:
            return champ[0]
        return -1