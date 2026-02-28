<!-- ## Fibonacci Sequence
<p>The Fibonacci Sequence is one of the most famous formulas in mathematics. It’s a simple series of numbers where each number is the sum of the two preceding ones.<p>
<p>The sequence usually starts like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...<p>

### The Formula
<p>In mathematical terms, the sequence is defined by the recurrence relation:<p>
$$F_n = F_{n-1} + F_{n-2}$$

With the seed values:
- $F_0 = 0$
- $F_1 = 1$

### The Golden Ratio ($\phi$)
<p>As the numbers in the Fibonacci sequence get higher, the ratio between two consecutive numbers approaches the Golden Ratio, which is approximately 1.618.</p>

<p>This ratio is found throughout nature, art, and architecture because it is visually pleasing and allows for efficient growth patterns.</p>

### Where You’ll See It in Nature
<p>The Fibonacci sequence isn't just a classroom exercise; it appears in the physical world in fascinating ways:</p>

- Flower Petals: Most flowers have a petal count that is a Fibonacci number (e.g., lilies have 3, buttercups have 5, delphiniums have 8).

- Pinecones and Sunflowers: The seeds grow in opposing spirals. If you count the clockwise and counter-clockwise spirals, they are almost always consecutive Fibonacci numbers.

- Shells: The "Golden Spiral" (based on Fibonacci squares) is famously seen in the shell of the chambered nautilus.

- Galaxies: The spiral arms of the Milky Way and other galaxies often follow the path of the Golden Spiral.

-->









<!-- # 📘 Fibonacci Sequence – README -->

<h1 align="center">Fibonacci Sequence</h1>

## Overview

The **Fibonacci Sequence** is a series of numbers in which each number is the sum of the two preceding numbers.

It starts with:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```
<!--
Mathematically, it is defined as:

[
F(0) = 0, \quad F(1) = 1, \quad F(n) = F(n-1) + F(n-2) \text{ for } n \ge 2
]
-->
The Fibonacci sequence appears in nature, computer science, mathematics, and art, such as in plant patterns, algorithms, and the Golden Ratio.

---

## ⚙️ How Fibonacci Sequence Works

1. Start with `0` and `1`.
2. Add the last two numbers to get the next number.
3. Repeat until the desired number of terms is reached.

Example for first 10 numbers:

```
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
5 + 8 = 13
8 + 13 = 21
13 + 21 = 34
```

Resulting sequence:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

---

## 🧠 Python Examples

### Example 1 — Recursive Approach

```python
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci_recursive(i), end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34
```

* Time complexity: O(2ⁿ)
* Simple but inefficient for large `n`.

---

### Example 2 — Iterative Approach

```python
def fibonacci_iterative(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[:n]

print(fibonacci_iterative(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

* Time complexity: O(n)
* Space complexity: O(n)
* Efficient and easy to implement.

---

### Example 3 — Space-Optimized Iterative

```python
def fibonacci_optimized(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci_optimized(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

* Time complexity: O(n)
* Space complexity: O(1)
* Uses minimal memory.

---

## ⏱️ Time Complexity Comparison

| Method              | Time Complexity | Space Complexity     |
| ------------------- | --------------- | -------------------- |
| Recursive           | O(2ⁿ)           | O(n) recursion stack |
| Iterative           | O(n)            | O(n)                 |
| Optimized Iterative | O(n)            | O(1)                 |

---

## 📌 When to Use Fibonacci Sequence

* Mathematical modeling and algorithm design
* Recursion practice in programming
* Modeling natural growth patterns (plants, shells, etc.)
* Dynamic programming examples and exercises

---

## 🏁 Summary

The Fibonacci Sequence is a fundamental mathematical series.
For small inputs, recursion works, but for larger inputs, iterative or space-optimized methods are more efficient and practical.

