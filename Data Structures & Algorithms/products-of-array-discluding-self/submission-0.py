class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsOutput = []
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        preProd = 1
        for i in range(1, n):
            preProd *= nums[i-1]
            pre[i] = preProd
        postProd = 1

        for i in range(n-2, -1, -1):
            postProd *= nums[i+1]
            post[i] = postProd
        for i in range(n):
            numsOutput.append(pre[i] * post[i])
        return numsOutput

