class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0 
        sell = 1 
        maxprofit = 0

        while sell < len(prices):

            if prices[buy] < prices[sell]:
                #calculate profit and update maxprofit along the way

                profit = prices[sell] - prices[buy]
                maxprofit = max(maxprofit, profit)
            
            else:
                # if the sell price is lower then update the buy to that position. Increment the sell price by one after these conditions.

                buy = sell 
            
            sell += 1
            
        return maxprofit