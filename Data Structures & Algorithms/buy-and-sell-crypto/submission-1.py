class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=[]
        if prices==[] or len(prices)==1:
            return 0
        
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    res.append(0)
                    
                else:
                    diff=prices[j]-prices[i]
                    res.append(diff)
        return max(res)

        