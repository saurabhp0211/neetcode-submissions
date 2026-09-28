class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        seen={}
        k=n//2
        for i in range(len(nums)):
            j=nums[i]
            seen[j]=seen.get(j,0)+1
        
        for num, count in seen.items():
            if count>k:
                return num
            

     