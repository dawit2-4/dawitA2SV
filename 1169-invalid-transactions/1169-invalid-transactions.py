# import csv

# def extract_transactions(f_name):
#     with open(f_name) as f:
#         reader = csv.DictReader(f)
#         transactions = list(reader)
#     return transactions


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        store_transaction = defaultdict(list)
        fraud = []
        invalid = [False] * len(transactions)
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            if int(amount) > 1000:
                invalid[i] = True
            store_transaction[name].append((time, amount,city, i))
    
        for name in store_transaction:
            store_transaction[name].sort()
            txs = store_transaction[name]
            for i in range(len(txs)):
                for j in range(1, len(txs)):
                    time1, amount1, city1, idx1 = txs[i]
                    time2, amount2, city2, idx2 = txs[j]

                    if city1 != city2 and abs(int(time1)  - int(time2)) <= 60:
                        invalid[idx1] = True
                        invalid[idx2] = True
        for i in range(len(transactions)):
            if invalid[i]:
                fraud.append(transactions[i])

        return fraud
                    
                    