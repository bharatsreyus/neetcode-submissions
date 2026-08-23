class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxContSeq = 0
        store = set(nums)
        for num in nums:
            search = num
            cont = 0
            if search-1 not in store:
                while search in store: 
                    search+=1
                    cont+=1
                maxContSeq = max(cont, maxContSeq)

        return maxContSeq

        
            

        
        


            
