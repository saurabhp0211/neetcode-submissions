class Solution:
    def atmost(self, nums, k):
        l=0
        odd=0
        count=0
        for r in range(len(nums)):
            if nums[r]%2:
                odd+=1
            while odd>k:
                if nums[l]%2:
                    odd-=1
                l+=1
            count+=r-l+1
        
        return count
        

    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atmost(nums,k)-self.atmost(nums, k-1)
    