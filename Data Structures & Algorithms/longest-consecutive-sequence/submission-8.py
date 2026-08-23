class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        if len(nums) == 0:
            return 0
        longestSeqLen = 1
        for n in store:
            # start of the sequence
            if n-1 not in store:
                currentSeqLen = 1
                search = n+1
                while search in store:
                    currentSeqLen += 1
                    search+=1
                longestSeqLen = max(currentSeqLen, longestSeqLen)
        return longestSeqLen

        
            

        
        


            
