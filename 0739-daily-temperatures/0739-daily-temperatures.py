class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = []

        for day, tmp in enumerate(temperatures):
            while mono_stack and temperatures[mono_stack[-1]] < tmp:
                j = mono_stack.pop()
                res[j] = day - j
            mono_stack.append(day)
        return res
