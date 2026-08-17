class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = [0]*26
        tCount = [0]*26

        for i in range(len(s)):
            sCount[ord('a')-ord(s[i])] += 1
            tCount[ord('a')-ord(t[i])] += 1
        
        return sCount == tCount