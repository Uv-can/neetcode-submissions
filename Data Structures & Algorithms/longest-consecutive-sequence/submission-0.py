class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        res = 0
        for i in nums:
            if (i - 1) not in seq:
                length = 1
                while (i + length) in seq:
                    length += 1
                res = max(res,length)
        return res