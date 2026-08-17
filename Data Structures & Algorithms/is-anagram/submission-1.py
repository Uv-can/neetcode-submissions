class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0]*26
        countT = [0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            varS = ord("a") - ord(s[i])
            varT = ord("a") - ord(t[i])
            countS[varS] += 1
            countT[varT] += 1

        return countS == countT
