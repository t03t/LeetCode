class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # price[i] = price of ith item
        # ith item discount = price[j] (minimum index such that j > i? and price[j] < price[i]
        # so basically the first cheap item after price[i]
        for i in range(len(prices)):
            price = prices[i]
            remaining = prices[i+1:]
            for discount in remaining:
                if discount <= price:
                    prices[i] = price - discount
                    break
        return prices
                