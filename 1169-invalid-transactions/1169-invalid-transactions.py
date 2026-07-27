class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        store = defaultdict(list)
        invalid = []
        transaction = []
        for i in range(len(transactions)):
            transaction.append(transactions[i].split(","))
            transaction[i].append(i)
           
            
        for t in transaction:
            _, _, amount, _, idx = t
            if int(amount) > 1000:
                invalid.append(idx)
        

        for t in transaction:
            name, time, amount, city, idx = t
            store[name].append((int(time), amount, city, idx))
        
        for key, val in store.items():
            name = key
            val.sort()

            if len(val) > 1:
                for i in range(len(val)):
                    for j in range(i+1, len(val)):
                        if val[i][2] != val[j][2] and val[j][0] - val[i][0] <= 60:
                            idx1 = val[i][3]
                            idx2 = val[j][3]
                            invalid.append(idx1)
                            invalid.append(idx2)
        

                            
        invalid = set(invalid)
        ans = []
        for i in invalid:
            ans.append(transactions[i])
        return ans