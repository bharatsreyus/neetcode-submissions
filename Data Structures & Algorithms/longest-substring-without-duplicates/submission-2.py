class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIdx = dict()
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in charIdx:
                l = max(charIdx[s[r]] + 1, l)
            charIdx[s[r]] = r
            res = max(res, r - l + 1)
        return res