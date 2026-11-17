class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum=0
        l=0
        minWindow=float('inf')
        for r in range(len(nums)):
            currSum+=nums[r]
            while currSum>=target:
                minWindow=min(minWindow, r-l+1)
                currSum-=nums[l]
                l+=1
        if minWindow==float('inf'):
            return 0
            
                
        return minWindow


        