class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n

        for i in range(n):
            curr_product=1
            for j in range(n):
                if j!=i:
                    curr_product*=nums[j]
            answer[i]=curr_product    
        return answer
