# Bug reports for homework.py

Line: 6
Problem: Incorrect arithmetic operator; discount should be calculated as a percentage of price, not subtracted directly.  
Example: calculate_discount(100, 20) returns 80 instead of 80 (correct in this case, but logically flawed — discount_percent should be applied as price * (1 - discount_percent/100))  
Fix: Change to `return price - (price * discount_percent / 100)`

Line: 11
Problem: Incorrect boolean condition; age should be at least 18 (inclusive), but condition uses `> 18` which excludes 18.  
Example: is_valid_age(18) returns False when it should return True  
Fix: Change to `return age >= 18`

Line: 16
Problem: Division by zero when scores list is empty; `len(scores)` is 0, causing division by zero.  
Example: average_scores([]) raises ZeroDivisionError  
Fix: Change to `if not scores: return 0` before the division

Line: 22
Problem: SQL injection vulnerability — untrusted input is directly inserted into SQL query without escaping.  
Example: username = "'; DROP TABLE users; --" leads to SQL injection and potential data loss  
Fix: Use parameterized query, e.g., `db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()`

Line: 28
Problem: Path traversal vulnerability — `Path(base_dir) / filename` allows traversal if `filename` contains path traversal sequences like `../`.  
Example: filename = "../etc/passwd" when base_dir is "/home" may read files outside base_dir  
Fix: Validate that filename does not contain path traversal sequences (e.g., `..`), or use `Path(base_dir).joinpath(filename).resolve()` with strict path checking and relative path restriction.
