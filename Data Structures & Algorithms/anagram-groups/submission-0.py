from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        anagram = [0]*26

        for word in strs:
            for w in word:
                anagram[ord('a') - ord(w)] +=1
            mapper[tuple(anagram)].append(word)
            anagram = [0]*26
        return mapper.values()
