class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2=None, None
        count1=0
        count2=0

        for num in nums:
            if candidate1==num:
                count1+=1
            elif candidate2==num:
                count2+=1
            elif count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1
            else:
                count1-=1
                count2-=1

        res=[]
        k=len(nums)//3

        if nums.count(candidate1)>k:
            res.append(candidate1)
        if nums.count(candidate2)>k:
            res.append(candidate2)

        return res




