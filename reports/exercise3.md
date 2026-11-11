# Bug reports for exercise3.py

Line: 3
Problem: The docstring states that an empty list has an average of 0, but the function divides by len(numbers), which causes a ZeroDivisionError when the input list is empty.
Example: average([]) raises ZeroDivisionError, expected to return 0.
Fix: Add a check for an empty list and return 0 in that case. Change the function to: return sum(numbers) / len(numbers) if numbers else 0.

Line: 8
Problem: The function returns the first word using split()[0], but if the text is empty or contains only whitespace, split() returns an empty list, and accessing [0] raises an IndexError.
Example: first_word("   ") returns IndexError, expected to return "".
Fix: Use split() and check if the result is empty before accessing [0]. Change the function to: return text.split()[0] if text.strip() else ""

Line: 12
Problem: The docstring states that if total is 0, the result is 0. However, the current implementation divides by total, which causes a ZeroDivisionError when total is 0.
Example: percent(5, 0) raises ZeroDivisionError, expected to return 0.
Fix: Add a check for total == 0 and return 0 in that case. Change the function to: return part / total * 100 if total != 0 else 0
