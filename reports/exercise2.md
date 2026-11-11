# Bug reports for exercise2.py

Line: 3  
Problem: The function `is_passing` returns `True` only when the grade is *greater than* 5, but the docstring states "True if the grade is 5 or more", which means 5 should be included.  
Example: is_passing(5) returns False, expected True.  
Fix: Change `grade > 5` to `grade >= 5`.

Line: 8  
Problem: The function `is_valid_password` checks for length greater than 8 (`len(password) > 8`), but the docstring requires "at least 8 characters", which means 8 is acceptable. The condition should be inclusive.  
Example: is_valid_password("password123") returns False (length 10 is valid, but the example is not illustrative), but consider "pass123" (length 8): it returns False because `len(password) > 8` fails.  
Correct example: is_valid_password("pass123") returns False, expected True.  
Fix: Change `len(password) > 8` to `len(password) >= 8`.

Line: 12  
Problem: The `clamp` function incorrectly computes the lower bound. It uses `max(low, min(x, low))`, which simplifies to `low` regardless of x. This is logically incorrect.  
Example: clamp(3, 1, 5) returns 1, which is correct. But clamp(10, 1, 5) returns max(1, min(10, 1)) = max(1,1) = 1, which is correct. However, clamp(2, 5, 10) returns max(5, min(2,5)) = max(5,2) = 5 — correct. But the logic is flawed: `min(x, low)` is wrong — it should be `min(x, high)`, and then `max(low, result)`.  
The actual bug: it uses `min(x, low)` instead of `min(x, high)`.  
Example: clamp(10, 1, 5) returns 5, which is correct. But clamp(0, 1, 5) returns max(1, min(0,1)) = max(1,0) = 1 — correct. But the logic is wrong because `min(x, low)` will always be ≤ low, and then `max(low, min(x, low))` will always be `low`.  
This means the function always returns `low`, regardless of `x` and `high`.  
Example: clamp(10, 1, 10) returns 1, expected 10.  
Fix: Change `return max(low, min(x, low))` to `return max(low, min(x, high))`.
