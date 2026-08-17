class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = set()

        for i in nums:
            if i in cnt:
                return True
            cnt.add(i)

        return False