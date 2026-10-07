class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palin(string, left, right):
            while left<right:
                if string[left]!=string[right]:
                    return False
                left+=1
                right-=1
            return True
        
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skip_l= check_palin(s, l+1, r)
                skip_r=check_palin(s,l, r-1)
            
                return skip_l or skip_r
            l+=1
            r-=1
        return True


        


    


            


        