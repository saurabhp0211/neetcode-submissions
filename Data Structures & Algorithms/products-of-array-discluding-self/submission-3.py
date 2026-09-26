class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n

        # for left side of products
        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        
        # for right side of products now merging it with left side
        postfix=1
        for i in range(n-1, -1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res

    