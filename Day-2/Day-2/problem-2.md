# Problem: Remove Duplicates from Sorted Array II

## My Approach
I used two pointers to allow only two occurrences of each element.

## Mistake
Initially, I tried counting duplicates manually, which was confusing.

## Final Logic
I compared the current element with the element at index (i-2).
If they are different, I placed the element.

## Pattern
Two Pointers (Controlled Duplicates)

## Learning
Instead of counting, we can use position-based comparison.
