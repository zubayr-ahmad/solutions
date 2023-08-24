# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if i == j:
                continue
            diff = prices[j] - prices[i]
            if j > i and 0 < diff > profit:
                profit = diff
    return profit

if __name__ == '__main__':
    ...