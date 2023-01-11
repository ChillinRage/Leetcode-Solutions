def maxProfit(prices):
    max_profit = 0
    min_cost   = prices[0]
        
    for price in prices[1:]:
        if price > min_cost:
            max_profit = max(price - min_cost, max_profit)
        else:
            min_cost = price

    return max_profit
