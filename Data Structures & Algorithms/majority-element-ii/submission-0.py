class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        k=n//3
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
       

        for num, count in seen.items():
            if count>k:
                res.append(num)

        return res