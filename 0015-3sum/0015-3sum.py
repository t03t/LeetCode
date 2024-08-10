class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target: int):
            l = 0
            r = len(nums) - 1
            pairs = []
            while r > l:
                total = nums[l] + nums[r]
                if total == target:
                    pairs.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate elements
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
            return pairs

        if len(nums) < 3:
            return []

        nums.sort()  # Sort the input list
        result = []

        for i in range(len(nums)):
            # Avoid duplicate solutions for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            cur = nums[i]
            remaining = nums[i + 1:]
            pairs = twoSum(remaining, -cur)

            for pair in pairs:
                result.append([cur] + pair)

        return result
