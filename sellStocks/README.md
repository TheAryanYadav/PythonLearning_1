# Best Time to Buy and Sell Stock

## Description
Given an array 'prices' where 'prices[i]' is the price of a given stock on the `ith` day.
You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

**Goal:** Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

##  My Logic (One-time Approach)
Instead of comparing every single day with every other day (which is too slow), I used a greedy strategy:

1.  **Track the Minimum:** I keep a variable 'start' to track the lowest price I've seen so far.
2.  **Calculate Profit:** For every new price, I calculate what the profit would be if I sold *today* ('price - start').
3.  **Update Maximum:** If today's profit is higher than any profit I've seen before, I update `max_profit`.



## Efficiency
* **Time Complexity:** $O(n)$ — I only loop through the list of prices once.
* **Space Complexity:** $O(1)$ — I only use two variables (`start` and `max_profit`) regardless of how big the input list is.

## 🛠️ How to Run
To run this solution locally:
```bash
python sellStocks.py
