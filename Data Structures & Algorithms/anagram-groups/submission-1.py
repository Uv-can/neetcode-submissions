from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=collections.defaultdict(list)
        for word in strs:
            mapper = [0] * 26
            for char in word:
                mapper[ord("a")-ord(char)] += 1
            res[tuple(mapper)].append(word)

        return  list(res.values())