class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      res=[]
      seen={}
      for i in range(len(nums)):
        n=nums[i]
        rem=target-n
        if rem in seen:
            res.append(seen[rem])
            res.append(i)
        
        seen[n]=i
        
      return res