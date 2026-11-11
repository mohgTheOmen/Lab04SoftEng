# Bug reports for exercise1.py

Line: 3
Problem: The function is_even checks if n % 2 == 1, which is true for odd numbers, not even numbers. It should check for even numbers, which means n % 2 == 0.
Example: is_even(4) returns False, expected True; is_even(3) returns True, expected False.
Fix: Change the condition to n % 2 == 0.

Line: 8
Problem: The rectangle_area function returns the sum of width and height, but it should return the product (width * height) to compute the area correctly.
Example: rectangle_area(4, 5) returns 9, expected 20.
Fix: Change the return statement to return width * height.

Line: 12
Problem: The double function adds 2 to n, but it should return twice the number, i.e., n * 2.
Example: double(3) returns 5, expected 6.
Fix: Change the return statement to return n * 2.
