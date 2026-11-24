class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        
        for i, num in enumerate(nums):
            lookingfor = target - num
            if lookingfor in d:
                j = d[lookingfor]
                if i != j:
                    return [i, j]