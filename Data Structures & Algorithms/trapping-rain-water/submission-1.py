class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1

        stored_water=0
        max_left=height[l]
        max_right=height[r]
        
        while l<r:
            if max_left<max_right:
                l+=1
                
                if height[l]>max_left:
                    max_left=height[l]
                else:
                    stored_water+=max_left-height[l]
            else:
                r-=1

                if max_right<height[r]:
                    max_right=height[r]
                else:
                    stored_water+=max_right-height[r]
        return stored_water
            
        