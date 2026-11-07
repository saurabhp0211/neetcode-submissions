class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        l=0
        k=1
        for r in range(1,len(nums)):
            if nums[l]!=nums[r]:
                l+=1
                k+=1
                nums[l]=nums[r] 
            
        return k

      


        