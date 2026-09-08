class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqDict = dict()
        L, R = 0, 0
        res = 0
        maxf = 0
        while R < len(s):
            freqDict[s[R]] = freqDict.get(s[R], 0) + 1
            maxf = max(maxf, freqDict[s[R]])

            windowSize = R - L + 1
            if windowSize - maxf <= k:
                res = max(windowSize, res)
                R += 1
            else:
                if windowSize - maxf > k:
                    freqDict[s[L]] -= 1
                    L += 1
                R += 1
        return res


                

