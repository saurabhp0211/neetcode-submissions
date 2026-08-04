class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        k=len(prefix)
        
        for i in range(1,len(strs)):
            while not strs[i].startswith(prefix):
                k-=1
                prefix=prefix[:k]


                if not prefix:
                    return ""
        return prefix

            
               
                

        