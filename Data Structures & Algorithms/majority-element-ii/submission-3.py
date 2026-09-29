class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        k=n//3
        candidate1, candidate2=None, None
        count1, count2=0,0

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
            
        if nums.count(candidate1)>k:
            result.append(candidate1)
        if nums.count(candidate2)>k:
            result.append(candidate2)
        
        return result
           