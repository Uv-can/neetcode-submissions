from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)
        mapper = [[] for i in range(len(nums)+1)]
        for key, value in counter.items():
            mapper[value].append(key)

        res = []
        for i in range(len(mapper)-1, 0, -1):
            for num in mapper[i]:
                res.append(num)
                if len(res) == k:
                    return res