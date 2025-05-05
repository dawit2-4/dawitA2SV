class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict(str)
        name_parent = {}
        def find(node):
            if parent[node] == "":
                parent[node] = node
                
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)

            parent[root2] = root1

        for account in accounts:
            name = account[0]
            rep = account[1]
            if parent[rep] == "":
                parent[rep] = rep

            for i in range(2,len(account)):
                union(rep, account[i])

            actual_parent = find(rep)
            name_parent[actual_parent] = name
        ans = defaultdict(list)

        # print(parent)

        for key, value in parent.items():
            ans[find(value)].append(key)
        for key in ans:
            ans[key].sort()
            ans[key].insert(0,name_parent[key])
        return list(ans.values())
        