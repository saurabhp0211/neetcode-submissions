class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(string, left, right):
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
                skipL=checkPalindrome(s,l+1,r)
                skipR=checkPalindrome(s,l,r-1)

                return skipL or skipR
            l+=1
            r-=1
        return True

