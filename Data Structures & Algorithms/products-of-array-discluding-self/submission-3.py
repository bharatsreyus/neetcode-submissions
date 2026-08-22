class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
        
        # numsOutput = []
        # n = len(nums)
        # pre = [1] * n
        # post = [1] * n
        # preProd = 1
        # # for i in range(1, n):
        # #     preProd *= nums[i-1]
        # #     pre[i] = preProd
        # postProd = 1

        # # for i in range(n-2, -1, -1):
        # #     postProd *= nums[i+1]
        # #     post[i] = postProd

        # # for i in range(n):
        # #     numsOutput.append(pre[i] * post[i])

        # k = 0

        # while k<n:

        #     if k == 0:
        #         pre[k] = 1
        #     else:
        #         preProd *= nums[k-1]
        #         pre[k] = preProd
            
        #     l = n - k - 1

        #     if l == n-1:
        #         post[l] = 1
        #     else:
        #         postProd *= nums[l+1]
        #         post[l] = postProd

        #     k+=1

        # for i in range(n):
        #     numsOutput.append(pre[i] * post[i])
        
        # return numsOutput

