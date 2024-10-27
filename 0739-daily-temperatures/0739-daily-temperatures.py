class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = []
        for i, temp in enumerate(temperatures):
            while mono_stack and temperatures[mono_stack[-1]] < temperatures[i]:
                j = mono_stack.pop()
                res[j] = i - j
            mono_stack.append(i)
        return res
