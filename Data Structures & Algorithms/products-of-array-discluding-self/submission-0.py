class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1 for i in range(len(nums))]
        for index, num in enumerate(nums):
            res[index] = prefix
            prefix *= num
     
        postfix = 1
       
        for i in range(len(res)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]
        
        return res
        
        