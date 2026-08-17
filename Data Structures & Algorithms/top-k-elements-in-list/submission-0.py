from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dual_list = [[] for i in range(len(nums) + 1)]
        map_dict = defaultdict(list)
        for num in nums:
            map_dict[num] = 1 + map_dict.get(num, 0)
        
        for num, count in map_dict.items():
            dual_list[count].append(num)
        res = []
        for i in range(len(dual_list)-1, 0, -1):
            for j in dual_list[i]:
                res.append(j)
                if len(res) == k:
                    return res
