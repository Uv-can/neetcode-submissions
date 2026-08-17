class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            count = 0
            while num in nums:
                count += 1
                num = num + 1
            res = max(res, count)
        return res