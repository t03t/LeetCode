class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        pot_holes = []
        potHole = 'x' if road[0] == 'x' else ''
        for r in road[1:]:
            if r != 'x':
                if potHole != '.' and potHole != '':
                    pot_holes.append(len(potHole))
                potHole = ''
            else:
                potHole += r
        if potHole != '.' and potHole != '':
            pot_holes.append(len(potHole))
        res = 0
        for potHole in reversed(sorted(pot_holes)):
            if budget - (potHole + 1) >= 0:
                budget -= potHole + 1
                res += potHole
            elif budget - 1 >= 0:
                res += budget - 1
                budget = 0
        return res