# Problem 1: Merge Sorted Array

## My Approach
I compared elements from the end of both arrays and placed the larger one at the last position.

## Mistake
Initially, I used the wrong loop condition (j <= 0 instead of j >= 0).

## Final Logic
Use three pointers (i, j, k) and fill nums1 from the back.

## Pattern
Two Pointers (Backward)

## Learning
Starting from the end avoids overwriting elements.
