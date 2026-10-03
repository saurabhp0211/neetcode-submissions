class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset=set(nums)
        target=1
        while target in numset:
            target+=1
        else:
            return target