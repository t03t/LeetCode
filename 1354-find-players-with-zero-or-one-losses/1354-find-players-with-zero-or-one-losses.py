class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        losses = Counter()
        for match in matches:
            winner, loser = match[0], match[1]
            losses[loser] += 1
            if not winner in losses:
                losses[winner] = 0
        for loser in sorted(losses.keys()):
            if losses[loser] == 0:
                res[0].append(loser)
            elif losses[loser] == 1:
                res[1].append(loser)
        return res