class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        winLen = len(s1)
        countS1 = [0]*26
        for ch in s1:
            countS1[ord(ch) - ord('a')] += 1
        l = 0
        for r in range(winLen-1, len(s2)):
            countS2 = [0]*26
            for ch in s2[l:r+1]:
                countS2[ord(ch) - ord('a')] += 1
            if countS1 == countS2:
                return True
            l += 1
        return False