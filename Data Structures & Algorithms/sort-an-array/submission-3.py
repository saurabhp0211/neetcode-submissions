class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # base case
        if len(nums)<=1:
            return nums

        mid=len(nums)//2
        l_half=self.sortArray(nums[:mid])
        r_half=self.sortArray(nums[mid:])
        return self.merge(l_half, r_half)
    
    def merge(self, arr1:List[int], arr2:List[int])->List[int]:
        i, j=0,0
        merged=[]

        while i<len(arr1) and j<len(arr2):

            if arr1[i]<=arr2[j]:
                merged.append(arr1[i])
                i+=1
            else:
                merged.append(arr2[j])
                j+=1
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])

        return merged