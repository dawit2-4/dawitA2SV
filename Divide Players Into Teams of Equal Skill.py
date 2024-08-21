class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        s, e= 0, n - 1
        target = skill[s] + skill[e]
        sum = 0
        while s < e:
            curr = skill[s] + skill[e]
            if curr != target:
                return -1
            else:
                sum += skill[s] * skill[e]
                s += 1
                e -= 1
        return sum
            
