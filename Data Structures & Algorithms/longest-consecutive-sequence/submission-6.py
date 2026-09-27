class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set(nums)
        longest=0
        currL=0

        for num in numset:
            if num-1 not in numset:
                currL=1
                while (num+currL) in numset:
                    currL+=1
            longest=max(longest, currL)
        
        return longest

       