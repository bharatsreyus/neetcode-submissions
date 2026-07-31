class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valIdxDict = {}
        numsL = len(nums)
        # for i in range(numsL):
        #     valIdxDict[nums[i]] = i

        for i in range(numsL):
            diff = target - nums[i]
            if nums[i] not in valIdxDict:
                valIdxDict[nums[i]] = i
            if diff in valIdxDict and i != valIdxDict[diff]:
                return [valIdxDict[diff], i]

            
