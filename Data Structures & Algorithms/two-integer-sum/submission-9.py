class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valIdxDict = {}
        for i,v in enumerate(nums):
            valIdxDict[v] = i
        for i,v in enumerate(nums):
            diff = target -v
            if diff in valIdxDict and i != valIdxDict[diff]:
                return [i, valIdxDict[diff]]

            
