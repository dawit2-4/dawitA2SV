class Solution:
    def romanToInt(self, s: str) -> int:
        store = {
            'I'      :       1,
            'V'      :       5,
            'X'      :       10,
            'L'      :       50,
            'C'      :       100,
            'D'      :       500,
            'M'      :       1000
        }

        ans = store[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if store[s[i+1]] > store[s[i]]:
                ans -= store[s[i]]
            else:
                ans += store[s[i]]
        return ans
                