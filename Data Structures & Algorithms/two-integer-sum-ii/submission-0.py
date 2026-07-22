class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        soln=0
        while l<r:
            soln=numbers[l]+numbers[r]
            if soln==target:
                return [l+1, r+1]
                
            elif soln<target:
                l+=1
            else:
                r-=1
      
            



        