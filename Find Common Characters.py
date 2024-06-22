class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count_first = {}
        result = []
        for char in words[0]:
            if char in count_first:
                count_first[char] += 1
            else:
                count_first[char] = 1
        
        for word in words[1:]:
            count_second = {}
            for char in word:
                if char in count_second:
                    count_second[char] += 1
                else:
                    count_second[char] = 1
            for char in count_first.keys():
                if char in count_second:
                    count_first[char] = min(count_first[char], count_second[char])
                else:
                    count_first[char] = 0
        for char, count in count_first.items() :
            result.extend([char] * count)

        return result
