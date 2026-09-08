class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        winLen = len(s1)
        countS1 = [0]*26
        for ch in s1:
            countS1[ord(ch) - ord('a')] += 1
        l = 0
        countS2 = [0]*26
        for i in range(winLen):
            countS2[ord(s2[i]) - ord('a')] += 1
        for r in range(winLen, len(s2)+1):
            
            if countS1 == countS2:
                return True
            if r < len(s2):
                outgoingCh = s2[l]
                countS2[ord(outgoingCh) - ord('a')] -= 1
                incomingCh = s2[r]
                countS2[ord(incomingCh) - ord('a')] += 1
                l += 1
        return False