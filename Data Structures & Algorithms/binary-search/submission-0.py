class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            middle = (r + l)//2
            
            if nums[middle] < target:
                l += 1
            elif nums[middle] > target:
                r -= 1
            else:
                return middle
        return -1 