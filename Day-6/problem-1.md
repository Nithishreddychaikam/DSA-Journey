# Problem: H-Index

## My Approach
I sorted the array and checked from left to right.

## Mistake
Initially confused about how to calculate h.

## Final Logic
For each index, calculate h = n - i and check if citations[i] >= h.

## Pattern
Sorting + Greedy

## Learning
We need at least h elements with value >= h.
