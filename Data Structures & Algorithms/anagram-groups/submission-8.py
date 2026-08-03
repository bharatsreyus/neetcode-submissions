class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:                    
        outputD = defaultdict(list)

        for word in strs:
            alphabetCode = [0] * 26
            for ch in word:
                alphabetCode[ord(ch) - ord("a")] += 1
            outputD[tuple(alphabetCode)].append(word) 

        return list(outputD.values())