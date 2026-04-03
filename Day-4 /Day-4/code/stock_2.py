# Problem: Best Time to Buy and Sell Stock II

## My Approach
I observed that I can make multiple transactions (buy and sell many times).
So instead of finding one maximum profit, I added all increasing profits.

## Mistake
Initially, I tried to find one buy and one sell like the previous problem.

## Final Logic
If today's price is greater than yesterday's price, add the difference to profit.

## Pattern
Greedy

## Learning
Instead of tracking one minimum, we accumulate every small profit.
