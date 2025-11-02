class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for i in range(1,n+1):
            queue.append(i)
        
    
        while len(queue) > 1:
            for _ in range(k-1):
                x = queue.popleft()
                queue.append(x)
            queue.popleft()
        return queue[0]