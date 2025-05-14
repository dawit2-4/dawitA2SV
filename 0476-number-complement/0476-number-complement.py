class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        x = list(x)
    
        for i in range(len(x)):
            if x[i] == '1':
                x[i] = '0'
            else:
                x[i] = '1'
        
        x = ''.join(x)
        
        return int(x,2)
        
