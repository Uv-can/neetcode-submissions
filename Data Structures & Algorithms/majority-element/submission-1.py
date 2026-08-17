class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''count = {}
        res = 0
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        return max(count, key = count.get)'''

        res, maxCount = 0, 0
        for i in nums:
            if maxCount == 0:
                res = i
            maxCount = maxCount + 1 if i == res else maxCount - 1
        return res