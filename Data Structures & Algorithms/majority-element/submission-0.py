class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        j=len(nums)
        seen={}
        for n in nums:
            seen[n]=seen.get(n,0)+1
            if seen[n]>(j/2):
                return n

            
        

            
        