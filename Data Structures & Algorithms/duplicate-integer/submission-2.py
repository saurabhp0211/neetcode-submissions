class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for n in nums:
            if n in seen:
                return True
            seen[n]=seen.get(n,0)+1
        return False
      