class Solution:
    arr = {}
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        if n in self.arr:
            return self.arr[n]
        
        fibon = self.fib(n-1) + self.fib(n-2)
        self.arr[n] = fibon
        return fibon
        