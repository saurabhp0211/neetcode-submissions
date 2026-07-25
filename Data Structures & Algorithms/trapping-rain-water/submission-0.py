class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        # Initialize our max boundaries to the starting blocks
        max_left = height[l]
        max_right = height[r]
        
        stored_water = 0
        
        while l < r:
            # We process whichever side is the smaller bottleneck
            if max_left < max_right:
                l += 1 # Move the pointer first
                
                if height[l] > max_left:
                    # New tallest wall found! Update max_left.
                    max_left = height[l]
                else:
                    # Current block is shorter than max_left, so water is trapped!
                    stored_water += max_left - height[l]
            else:
                r -= 1 # Move the pointer first
                
                if height[r] > max_right:
                    # New tallest wall found! Update max_right.
                    max_right = height[r]
                else:
                    # Current block is shorter than max_right, so water is trapped!
                    stored_water += max_right - height[r]
                    
        return stored_water
        
        