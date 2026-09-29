class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen={0:1}
        currSum=0
        count=0

        for n in nums:
            currSum+=n
            diff= currSum-k
            if diff in seen:
                count+=seen[diff]
            seen[currSum]=seen.get(currSum,0)+1
            
        return count