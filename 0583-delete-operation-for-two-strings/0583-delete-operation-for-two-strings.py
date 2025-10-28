class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dist = [[float('inf')] * (len(word1) +1) for _ in range(len(word2)+1)]
        for i in range(len(word2) + 1):
            dist[i][len(word1)] = len(word2) - i
        for j in range(len(word1) + 1):
            dist[len(word2)][j] = len(word1) - j
        
        for i in range(len(word2)-1,-1,-1):
            for j in range(len(word1)-1,-1,-1):
                if word2[i] == word1[j]:
                    dist[i][j] = dist[i+1][j+1]
                else:
                    dist[i][j] = min(dist[i+1][j], dist[i][j+1]) + 1
        return dist[0][0]