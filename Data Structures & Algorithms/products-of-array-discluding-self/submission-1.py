class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n

        for i in range(n):
            curr_prod=1
            for j in range(n):
                if j!=i:
                    curr_prod*=nums[j]
            answer[i]=curr_prod
        return answer
      
