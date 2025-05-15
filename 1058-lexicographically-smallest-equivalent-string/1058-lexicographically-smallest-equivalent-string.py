class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {
  'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
  'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
  'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
  'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
  'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y',
  'z': 'z'
}
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                return 
            if r1 < r2:
                parent[r2] = r1
            else:
                parent[r1] = r2
           
        
 

 
        for x, y in zip(s1, s2):
            union(x, y)
        ans = []
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))
        return "".join(ans)