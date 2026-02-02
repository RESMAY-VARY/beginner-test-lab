# Bug Report 02 — get_first_item

## Summary
get_first_item returns the wrong element from the list.

## Steps to Reproduce
Call get_first_item([10, 20, 30])

## Expected Behavior
Should return 10 (the first item).

## Actual Behavior
Returns 20 (the second item).

## Error Output
AssertionError: assert 20 == 10

## Root Cause
The function uses index 1 instead of index 0.

## Suggested Fix
Change `items[1]` to `items[0]`.

