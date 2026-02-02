# Bug Report 01 — add_numbers

## Summary
add_numbers returns incorrect results because it adds an extra +1.

## Steps to Reproduce
Call add_numbers(2, 3)

## Expected Behavior
Function should return 5

## Actual Behavior
Function returns 6

## Error Output
6 == 5 (AssertionError)

## Root Cause
The function adds an unnecessary +1.

## Suggested Fix
Change `return a + b + 1` to `return a + b`

