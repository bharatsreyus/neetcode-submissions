class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxWindow = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            if (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            maxWindow = max(maxWindow, r-l+1)
        return maxWindow
