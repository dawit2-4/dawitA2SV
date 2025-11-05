class Solution:
    def numberOfBeams(self, banks: List[str]) -> int:
        counts = []
        answer= 0
        for bank in banks:
            count = 0
            for i in range(len(bank)):
                if bank[i] == '1':
                    count += 1
            if count > 0:
                counts.append(count)
        # print(counts)
        for i in range(len(counts) - 1):
            answer += counts[i] * counts[i+1]
        
        return answer