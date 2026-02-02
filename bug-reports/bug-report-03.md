# Bug Report 03 — format_name

## Summary
format_name raises a TypeError because last.upper is missing parentheses.

## Steps to Reproduce
Call format_name("laura", "smith")

## Expected Behavior
Should return "laura SMITH".

## Actual Behavior
Raises TypeError: can only concatenate str (not "builtin_function_or_method") to str

## Error Output
TypeError at buggy_script.py line 11

## Root Cause
The code uses `last.upper` instead of `last.upper()`.

## Suggested Fix
Add parentheses: `last.upper()`.

