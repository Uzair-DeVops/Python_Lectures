Let's use `17` as an example to illustrate how checking up to the square root works:

### Steps to Determine if 17 is Prime

1. **Calculate the Square Root:**
   - The square root of 17 is approximately \( \sqrt{17} \approx 4.12 \).
   - Therefore, we need to check for factors up to \( \text{int}(4.12) + 1 = 5 \).

2. **Check Divisibility:**
   - We’ll check if 17 is divisible by any integer from 2 up to 4 (the integer part of the square root).

   **Checking each divisor:**
   - **2:** \( 17 \div 2 = 8.5 \) (17 is not divisible by 2, as it does not result in an integer)
   - **3:** \( 17 \div 3 \approx 5.67 \) (17 is not divisible by 3)
   - **4:** \( 17 \div 4 = 4.25 \) (17 is not divisible by 4)

3. **Conclusion:**
   - Since 17 is not divisible by any number up to its square root (which is 4), it has no divisors other than 1 and itself.

### Summary:
- For `n = 17`, the square root is approximately 4.12.
- We check for divisors up to 4.
- 17 is not divisible by 2, 3, or 4.
- Therefore, 17 is a prime number.

**Why This Works:**
- If 17 had any divisors, one of them would have to be less than or equal to the square root of 17. 
- Since there are no such divisors (less than or equal to 4) that divide 17 evenly, 17 must be prime.

Let's use `78` to determine if it's a prime number by checking up to its square root.

### Steps to Determine if 78 is Prime

1. **Calculate the Square Root:**
   - The square root of 78 is approximately \( \sqrt{78} \approx 8.83 \).
   - Therefore, we need to check for factors up to \( \text{int}(8.83) + 1 = 9 \).

2. **Check Divisibility:**
   - We’ll check if 78 is divisible by any integer from 2 up to 8 (the integer part of the square root).

   **Checking each divisor:**
   - **2:** \( 78 \div 2 = 39 \) (78 is divisible by 2, and the result is an integer, 39)
   - Since 78 is divisible by 2, it is not a prime number. 

   However, for completeness, let’s check the remaining potential divisors:

   - **3:** \( 78 \div 3 = 26 \) (78 is divisible by 3)
   - **4:** \( 78 \div 4 = 19.5 \) (78 is not divisible by 4)
   - **5:** \( 78 \div 5 = 15.6 \) (78 is not divisible by 5)
   - **6:** \( 78 \div 6 = 13 \) (78 is divisible by 6)
   - **7:** \( 78 \div 7 \approx 11.14 \) (78 is not divisible by 7)
   - **8:** \( 78 \div 8 = 9.75 \) (78 is not divisible by 8)

3. **Conclusion:**
   - Since 78 is divisible by 2 (and other numbers like 3 and 6), it is not a prime number.

### Summary:
- For `n = 78`, the square root is approximately 8.83.
- We check divisibility up to 8.
- 78 is divisible by 2, 3, and 6, among others.
- Therefore, 78 is not a prime number.

**Explanation of Why This Works:**
- If a number `n` has any divisors, one of them must be less than or equal to the square root of `n`. 
- Since we found that 78 is divisible by 2 (and 3, and 6), we confirmed that 78 is not a prime number.