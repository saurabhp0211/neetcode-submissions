class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        if k<=1:
            return 0
        l=0
        prod=1
        
        for r in range(len(nums)):
            prod*=nums[r]
            while prod>=k:
                prod=prod//nums[l]
                l+=1

            count+=(r-l+1)
                
        return count
                

        
        
        