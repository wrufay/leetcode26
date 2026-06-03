# First solved June 3 2026

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float('inf') # so that it will be updates with anything lower
        max_profit = 0 # this is the max profit

        # need to check each time if the current price is less than the minimum. if so, then update the minumum - this is a better time to buy.
        
        # then you also need to calculate the profit and keep track of it

        for price in prices:
            if price < cur_min:
                cur_min = price

            # ^^ same as cur_min = min(price, cur_min)
            max_profit = max(max_profit, price - cur_min)
            # price - min_price is calculating the new profit if you sold on the current day. so we want to check if this is larger or if the existing max_profit is larger

        return max_profit

        



        