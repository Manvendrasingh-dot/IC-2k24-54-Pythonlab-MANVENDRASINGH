# Lab 2 — Python Practice Programs

## 1. armstrong_number.py

**Aim:** Check if a number is an Armstrong number, and list all Armstrong numbers in a given range.

**Logic:** Split the number into digits, raise each digit to the power of the total digit count, and check if the sum equals the original number. For the range, run this check on every number in the range and collect the ones that pass.

**Sample Input / Output:**
```
Enter a number to check: 153
153 is an Armstrong number.
Enter the lower limit of the range: 1
Enter the upper limit of the range: 1000
Armstrong numbers between 1 and 1000: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
```

## 2. prime_number.py

**Aim:** Check if a number is prime, and list all primes up to a given limit.

**Logic:** A number is prime if no integer from 2 up to its square root divides it evenly. Even numbers greater than 2 are ruled out immediately. For the limit version, this check runs on every number from 2 to the limit.

**Sample Input / Output:**
```
Enter a number to check: 29
29 is a prime number.
Enter the upper limit: 50
Prime numbers up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

## 3. perfect_number.py

**Aim:** Check if a number is a perfect number, and list all perfect numbers up to a given limit.

**Logic:** A number is perfect if the sum of its proper divisors (divisors smaller than itself) equals the number. This sum is computed by testing every number from 1 up to num - 1.

**Sample Input / Output:**
```
Enter a number to check: 28
28 is a perfect number.
Enter the upper limit: 1000
Perfect numbers up to 1000: [6, 28, 496]
```

## 4. palindrome.py

**Aim:** Check if a number is a palindrome using only arithmetic operations, and separately check if a user-entered string is a palindrome.

**Logic:** For the number version, the digits are reversed one at a time using `% 10` and `// 10` to build a reversed number, which is then compared to the original — no `str()` involved. For the string version, the string is lowercased, spaces removed, and compared to its own reverse using slicing.

**Sample Input / Output:**
```
Enter a number to check: 121
121 is a palindrome.
Enter a word or phrase to check: madam
"madam" is a palindrome.
```

## 5. fibonacci_series.py

**Aim:** Print the first n Fibonacci terms using a loop, then using recursion, and compare how much work each does.

**Logic:** The loop version keeps two running variables and updates them n times. The recursive version calls itself twice per non-base case, so a call counter (passed as a mutable list) tracks every call made while building the full series.

**Sample Input / Output:**
```
Enter the number of Fibonacci terms: 10
Loop version: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] (loop steps: 10)
Recursive version total calls to build the series: 276
```

## 6. pattern_printing.py

**Aim:** Print a star triangle, a number pattern, and a centered pyramid for n rows.

**Logic:** Each pattern uses a nested loop — the outer loop controls the row, the inner loop (or string repetition) builds that row's content. The pyramid additionally pads each row with leading spaces so it appears centered.

**Sample Input / Output:**
```
Enter the number of rows: 4

*
**
***
****

1
12
123
1234

   *
  ***
 *****
*******
```

## 7. menu_driven_app.py

**Aim:** Combine programs 1–6 into one menu-driven application that loops until the user exits.

**Logic:** All checks and pattern functions from programs 1–6 are redefined in this single file so it runs standalone. A dictionary maps menu numbers to (label, function) pairs; the main loop prints the menu, reads a choice, runs the matching function, and repeats until "7. Exit" is chosen. Any choice not in the dictionary prints an "Invalid choice" message instead of crashing.

**Sample Input / Output:**
```
===== MENU =====
1. Armstrong Number
2. Prime Number
3. Perfect Number
4. Palindrome
5. Fibonacci Series
6. Pattern Printing
7. Exit
Enter your choice: 1

-- Armstrong Number --
Enter a number to check: 153
153 is an Armstrong number.
Enter the lower limit of the range: 1
Enter the upper limit of the range: 1000
Armstrong numbers between 1 and 1000: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

===== MENU =====
...
Enter your choice: 9
Invalid choice, please try again.
...
Enter your choice: 7
Exiting. Goodbye!
```

## 8. number_guessing_game.py

**Aim:** Let the user guess a randomly picked number (1–100) within a maximum of 7 attempts, with too high / too low / correct feedback.

**Logic:** `random.randint` picks the target once at the start. Each guess is validated to be a whole number inside the allowed range before it's compared to the target. The loop runs until the user guesses correctly or uses up all 7 attempts, printing the attempt count on success or the target number on failure.

**Sample Input / Output:**
```
I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it.
Attempt 1/7 - your guess: 50
Too low.
Attempt 2/7 - your guess: 75
Too high.
Attempt 3/7 - your guess: 63
Correct! You guessed it in 3 attempt(s).
```

---

## Analysis

**1. for vs while loop:**
`for` was the better fit for programs 1, 2, 3, and 6, since I always knew the exact range or row count to iterate over in advance (a range of numbers, digits, or rows). `while` was better for input validation loops (asking again on bad input) and the guessing game, where the number of iterations depends on runtime conditions (a correct guess or bad input) rather than a fixed count.

**2. Fibonacci — loop vs recursion:**
The recursive version repeats far more work as n grows. Each recursive call to `fibonacci(n)` branches into `fibonacci(n-1)` and `fibonacci(n-2)`, and those two calls both end up recomputing many of the same smaller Fibonacci values independently, with no memory of earlier results. This causes the call count to grow roughly exponentially with n (276 calls for n=10 versus 10 loop steps), while the loop only ever computes each value once.

**3. Prime check — largest divisor to test:**
Only divisors up to the square root of n need to be tested, not all the way to n - 1. This works because divisors always come in pairs that multiply to n (e.g., for n = 36, 4 × 9 = 36); if n had a divisor larger than its square root, it would have to be paired with a divisor smaller than the square root, which would already have been found. So checking beyond the square root can never turn up a new factor.

**4. Number guessing game — optimal strategy:**
The best strategy is **binary search**: always guess the midpoint of the remaining possible range, then narrow the range in half based on the too-high/too-low feedback. This guarantees finding any number in a range of size N within about log2(N) guesses — for example, at most 7 guesses for a 1–100 range, which matches the attempt limit used here.
