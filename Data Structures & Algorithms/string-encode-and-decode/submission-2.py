class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
     

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0

        while i<len(s):
            j=i

            while s[j]!='#':
                j+=1
            
            # to find out length we will separate hash value
            length=int(s[i:j])       #here j is at # index and j as ending index would be exclusive so we will get only the length of the string
            word=s[j+1:j+1+length]
            res.append(word)

            # this will skip to the next word
            i=j+1+length
        return res

      