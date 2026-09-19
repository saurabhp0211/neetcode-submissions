class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums

        # Dividing array into two halves
        mid=len(nums)//2

        left_half=self.sortArray(nums[:mid])
        right_half=self.sortArray(nums[mid:])

        # conquer-- merge both the arrays
        return self.merge(left_half, right_half)

    def merge(self, arr1:List[int], arr2:List[int])->List[int]:
        merged=[]
        i=0
        j=0

        while i<len(arr1) and j<len(arr2):
            if arr1[i]<=arr2[j]:
                merged.append(arr1[i])
                i+=1
            else:
                merged.append(arr2[j])
                j+=1

        # for leftovers -- i.e., when while loop breaks there will be leftovers in one or both the arrays so we need to add them here using .extend method

        merged.extend(arr1[i:])
        merged.extend(arr2[j:])

        return merged









       