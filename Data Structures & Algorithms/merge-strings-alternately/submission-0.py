class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        curr = 0
        res = ''
        while curr < len(word1):
            res += word1[curr]
            if curr < len(word2):
                res += word2[curr]
            curr += 1
        
        while curr < len(word2):
            res += word2[curr]
            curr +=1
        
        return res