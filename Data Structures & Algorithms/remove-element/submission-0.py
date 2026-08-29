class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        # 'i' is our Reader pointer. It looks at every single number in the array.
        for i in range(len(nums)):
            
            # If the current number is NOT the target value, it's a "good" number!
            if nums[i] != val:
                # 1. The Writer puts the good number at its current position
                nums[k] = nums[i]
                
                # 2. The Writer takes one step forward to prepare for the next good number
                k += 1
                
        # By the end, 'k' will equal the exact length of the new array
        return k