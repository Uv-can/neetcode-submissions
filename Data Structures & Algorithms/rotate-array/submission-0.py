class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums) -1

        def reverse( arr, left, right ):
            while left < right:
                tmp = arr[left]
                arr[left] = arr[right]
                arr[right] = tmp
                left += 1
                right -= 1          
            

        reverse(nums, l, r)
        reverse(nums, l, k-1)
        reverse(nums, k, r)
                