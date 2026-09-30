class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
      seen={}
      for i in range(len(nums)):
        n=nums[i]
        rem=target-n
        if rem in seen:
            return [seen[rem],i]
            
        seen[n]=i
        
      return res