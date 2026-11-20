class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req={}
        for r in range(len(t)):
            ch=t[r]
            req[ch]=req.get(ch,0)+1
        
        have=0
        need=len(req)
        l=0
        window={}
        best_start=0
        best_len=float('inf')
        for r in range(len(s)):
            ch_r=s[r]
            window[ch_r]=window.get(ch_r,0)+1

            if ch_r in req and window[ch_r]==req[ch_r]:
                have+=1
            while have==need:
                if (r-l+1)<best_len:
                    best_len=r-l+1
                    best_start=l
            
                ch_l=s[l]
                window[ch_l]-=1
                if ch_l in req and window[ch_l]<req[ch_l]:
                    have-=1
                l+=1
        
        if best_len!=float('inf'):
            return s[best_start:best_start+best_len]
        else:
            return ""





        

        