# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 1: return 0
        max_profit = 0
        for i, val in enumerate(prices):
            profit = 0
            for j in range(i+1, len(prices)):
                res = prices[j] - prices[i]
                if res > profit:
                    profit = res
            if profit > max_profit:
                max_profit = profit
        return max_profit

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))