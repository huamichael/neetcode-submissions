class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in prices:
            #two pointers
            #l is the buying price
            #r is the selling price
            #move r
            #if r<l, set l=r
            #if r>l, calculate r-l for profit
            l = 0
            r = 0
            max = 0
            for i in prices:
                if prices[r] < prices[l]:
                    l = r    
                elif prices[l] < prices[r]:
                    if max < prices[r] - prices[l]:
                        max = prices[r] - prices[l]
                r += 1
            return max