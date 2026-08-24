class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputL = []
        size = len(nums)
        nums.sort()
        # if nums[0] >= 0:
        #     return []
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            idx1, idx2 = i+1, size-1
            target = nums[i]
            while idx1 < idx2:
                # print(idx1, idx2)
                if nums[idx1] + nums[idx2] > -target:
                    idx2-=1
                elif nums[idx1] + nums[idx2] < -target:
                    idx1+=1
                else:
                    outputL.append([nums[i], nums[idx1], nums[idx2]])
                    idx1 += 1
                    idx2 -= 1
                    while nums[idx1] == nums[idx1-1] and idx1 < idx2:
                        idx1+=1

        return outputL
        