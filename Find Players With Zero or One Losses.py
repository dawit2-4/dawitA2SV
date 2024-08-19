class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        loser = {}
        ans1 = []
        ans2 = []
        for i in range(len(matches)):
            if matches[i][0] in winner:
                winner[matches[i][0]] += 1
            else:
                winner[matches[i][0]] = 1
            if matches[i][1] in loser:
                loser[matches[i][1] ]+= 1
            else:
                loser[matches[i][1]] = 1
        for player in winner:
            if player not in loser:
                ans1.append(player)
        for player, loss_count in loser.items():
            if loss_count == 1:
                ans2.append(player)
        ans1.sort()
        ans2.sort()
        return ans1, ans2
