class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, maxR = 0, 0
        l, r = 0, len(height)-1
        capacity = 0
        while l<r:
            if height[l] > maxL:
                maxL = height[l]
            if height[r] > maxR:
                maxR = height[r]
            if maxL <= maxR:
                capacity +=  maxL - height[l]
                l += 1
            else:
                capacity += maxR - height[r]
                r -= 1
        return capacity
                