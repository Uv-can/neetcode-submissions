class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefSum = {0:1}
        curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefSum.get(diff, 0)
            prefSum[curSum] = 1 + prefSum.get(curSum, 0)

        return res
            
                 