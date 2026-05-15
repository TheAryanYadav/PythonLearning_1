class Solution(object):
    def stock(self,prices):
        if  not prices:
            return 0
        max_profit=0
        start=prices[0]

        for price in prices:
            if (price<start):
                start=price
            current_profit= price- start

            if current_profit> max_profit:
                max_profit=current_profit
        return max_profit
    
solve=Solution()
print(solve.stock([1,2,3,8,3,9]))