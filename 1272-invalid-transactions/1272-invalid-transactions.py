class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []

        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))
        
        ans = set()

        for i in range(len(parsed)):
            name, time, amount, city = parsed[i]
            if amount > 1000:
                ans.add(i)
        for i in range(len(parsed)):
            for j in range(i+1, len(parsed)):
                name1, time1, amount1, city1 = parsed[i]
                name2, time2, amount2, city2= parsed[j]
                if name1 == name2 and city1 != city2 and abs(time1 - time2) <= 60:
                    ans.add(i)
                    ans.add(j)
        result = []
        for i in range(len(transactions)):
            if i in ans:
                result.append(transactions[i])
        return result