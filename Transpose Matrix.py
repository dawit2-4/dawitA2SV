class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix[0])):
            result.append([])
        for arr in matrix:
            for i in range(len(arr)):
                result[i].append(arr[i])
        return result
