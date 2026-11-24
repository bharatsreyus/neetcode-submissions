class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap sortedchars vs list of words
        groupmap = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))
            groupmap[key].append(word)
            
        outputl = []
        for key in groupmap.keys():
            outputl.append(groupmap[key])

        return outputl
