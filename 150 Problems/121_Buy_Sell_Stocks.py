# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 1: return 0
        max_profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - buy_price)

            if prices[i] < buy_price:
                buy_price = prices[i]
        return max_profit

sol = Solution()
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(sol.maxProfit(prices))