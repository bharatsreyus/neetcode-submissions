class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for ch in s:
            d1[ch] += 1
        for ch in t:
            d2[ch] += 1
        ## Check if both dicts are equal
        if len(d1.keys()) != len(d2.keys()): return False
        for k in d1.keys():
            if k not in d2:
                return False
            else:
                if d1[k] != d2[k]:
                    return False
        return True