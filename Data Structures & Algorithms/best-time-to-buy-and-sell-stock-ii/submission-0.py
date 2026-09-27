class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        j=0
        for i in range(1,len(prices)):
          if prices[j]<prices[i] and j<len(prices):
            maxP+=prices[i]-prices[j]
            j+=1
          else:
            j+=1
        return maxP




        
        
