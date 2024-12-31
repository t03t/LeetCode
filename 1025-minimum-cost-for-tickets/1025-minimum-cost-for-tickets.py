class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[len(days) - 1]
        dp = [0 for _ in range(last + 1)]

        i = 0
        for day in range(last + 1):
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                i += 1
                dp[day] = min(
                    dp[day-1] + costs[0],
                    min(dp[max(0, day-7)] + costs[1], dp[max(0, day - 30)] + costs[2])
                )
        return dp[last]

        