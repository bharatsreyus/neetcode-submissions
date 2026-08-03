class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        fixedI = []
        outputL = []
        for i in range(len(strs)):
            groupL = []
            word1 = strs[i]
            ## word1 should not be in any of groupL in outpuL ##
            if word1 in [w for g in outputL for w in g]:
                continue
            dict1 = {}
            for idx in range(len(word1)):
                dict1[word1[idx]] = 1 + dict1.get(word1[idx], 0)
            if word1 == "":
                dict1[""] = 1

            groupL.append(word1)

            for j in range(len(strs)):
                if i != j:
                    word2 = strs[j]
                    dict2 = {}
                    for idx in range(len(word2)):
                        dict2[word2[idx]] = 1 + dict2.get(word2[idx], 0)
                    if word2 == "":
                        dict2[""] = 1
                    ## check if both dictionaries have same values ##
                    isAnagram = True
                    if len(dict1) != len(dict2):
                        isAnagram = False
                    else:
                        for ch,freq in dict1.items():
                            if ch in dict2 and dict2[ch] == dict1[ch]:
                                continue
                            else:
                                isAnagram = False
                                break

                    if isAnagram:
                        groupL.append(word2)
                        # print(dict1, dict2, sep="\n")

            outputL.append(groupL)

        return outputL
                    



            
