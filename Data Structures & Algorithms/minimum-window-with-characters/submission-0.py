class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""

        tCount = defaultdict(int)
        for ch in t:
            tCount[ch] += 1
        
        l = 0
        have, need = 0, len(tCount)
        window = defaultdict(int)
        res, resLen = [-1, -1], float('inf')
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have += 1

            while have == need:
                
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""