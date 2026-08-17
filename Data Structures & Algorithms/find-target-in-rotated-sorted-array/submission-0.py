class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            #left sorted portion
            if nums[l] <= nums[mid]:                        # L<=........M.........R
                if target > nums[mid] or target < nums[l]:  #  <L.....M>...Search here...R
                    l = mid + 1
                else:                                       # L>...Search here....<M........R
                    r = mid - 1
            # RIght sorted portion
            else:                                           # L.......M>........<R                            
                if target < nums[mid] or target > nums[r]:  #  L...Search here..<M......R>
                    r = mid - 1
                else:                                       # L......M>....search here....<R
                    l = mid + 1
        return -1