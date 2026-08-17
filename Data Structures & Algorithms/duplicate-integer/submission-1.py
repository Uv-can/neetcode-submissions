class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        varm = set()
        for i in nums:
            if i in varm:
                return True
            varm.add(i)
        return False