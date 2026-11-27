class Solution:
    def subsKdiff(self, nums, k):
        l=0
        freq={}
        count=0

        for r in range(len(nums)):
            n=nums[r]
            freq[n]=freq.get(n,0)+1

            while len(freq)>k:
                freq[nums[l]]-=1

                if not freq[nums[l]]:
                    del freq[nums[l]]
                l+=1
            
            count+=r-l+1
        
        return count




    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subsKdiff(nums,k) - self.subsKdiff(nums, k-1)



        

        