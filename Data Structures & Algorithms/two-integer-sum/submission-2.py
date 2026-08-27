class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            curr_num=nums[i]
            rem= target-curr_num
            if rem in seen:
                return [seen[rem],i]
            seen[curr_num]=i
        return []
