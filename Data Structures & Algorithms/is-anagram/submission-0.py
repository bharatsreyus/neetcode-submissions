class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = dict()
        dictT = dict()
        for ch in s:
            dictS[ch] = dictS.get(ch, 0) + 1
        for ch in t:
            dictT[ch] = dictT.get(ch, 0) + 1
        
        if dictS.keys() != dictT.keys():
            return False
        
        for k in dictS.keys():
            if dictS[k] != dictT[k]:
                return False
        return True
        
        