class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        cycle = 2 * numRows - 2
        cycles = (len(s) + cycle - 1) // cycle

        cols = cycles * (numRows - 1)
        rows = numRows

        array = [["" for _ in range(cols)] for _ in range(rows)]

        row = 0
        col = 0
        down = True

        for s in s:
            array[row][col] = s
            if down == True:
                if row == rows - 1:
                    down = False
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:
                if row == 0:
                    down = True
                    row += 1
            
                else:
                    row -= 1
                    col += 1
        
        result = ''
        for row in array:
            for char in row:
                if char != "":
                    result += char
        return result
                    