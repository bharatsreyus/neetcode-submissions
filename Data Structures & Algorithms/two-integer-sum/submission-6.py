class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputL = [0,1]
        for i in range(len(nums)):
            try:
                # print(nums[i:])
                idx = nums[i+1:].index(target-nums[i])
                outputL[0] = i
                outputL[1] = idx + i + 1
                return outputL
            except:
                pass
            
