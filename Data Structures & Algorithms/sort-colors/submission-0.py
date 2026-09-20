class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0=0
        count1=0
        count2=0

        for i in range(len(nums)):
            if nums[i]==0:
                count0+=1
            elif nums[i]==1:
                count1+=1
            else:
                count2+=1
        idx=0
        while count0>0:
            nums[idx]=0
            idx+=1
            count0-=1
        
        while count1>0:
            nums[idx]=1
            idx+=1
            count1-=1
        while count2>0:
            nums[idx]=2
            idx+=1
            count2-=1
