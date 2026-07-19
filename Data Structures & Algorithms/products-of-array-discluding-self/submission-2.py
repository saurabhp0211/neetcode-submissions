class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n

        prefix=1     #this is for left side product of elements
        for i in range(n):
            result[i]*=prefix
            prefix*=nums[i]

        suffix=1 # this is for right side product of elements
        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]
        
        return result