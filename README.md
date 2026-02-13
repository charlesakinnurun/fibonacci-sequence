## Fibonacci Sequence
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

### 📁 Python Implementation
```python
"""
Fibonacci Sequence Implementation in Python

This script provides multiple ways to calculate Fibonacci numbers:
1. Iterative Approach (Most efficient for basic use)
2. Recursive Approach (With Memoization for performance)
3. Generator Approach (Best for memory efficiency)
"""

def fibonacci_iterative(n):
    '''
    Generate Fibonacci sequence up to n terms using a loop
    Time Complexity: O(n)
    Space Complexity: O(n) to store the list
    '''
    if n<= 0:
        return []
    elif n == 1:
        return[0]
    
    sequence = [0,1]
    while len(sequence) < n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)

    return sequence

def fibonacci_generator(n):
    """
    A generator that yields Fibonacci numbers one by one
    This is memory efficient because it doesn't store the whole list
    """
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a + b

# Using a dictionary for "memoization" to speed up recursion
memo = {
    0:0,
    1:1
}

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion and memoization
    Without memoization, this would be O(2^n), but with it, it's O(n).
    """
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_recursive(n-1) - fibonacci_recursive(n-2)
    return memo[n]


def main():
    # Numbers of terms to generate
    num_terms = 20

    print(f"----- Fibonacci Sequence (First {num_terms} terms) -----")

    # 1. Iterative Result
    iter_res = fibonacci_iterative(num_terms)
    print(f"Iterative: {iter_res}")

    # 2. Generator Result
    gen_res = list(fibonacci_generator(num_terms))
    print(f"Generator: {gen_res}")

    # 3. Recursive Result (getting the 10th number specifically)
    nth = 10
    val = fibonacci_recursive(nth)
    print(f"The {nth}th Fibonacci number (recursive): {val}")


if __name__ == "__main__":
    main()
```

### Where You’ll See It in Nature
<p>The Fibonacci sequence isn't just a classroom exercise; it appears in the physical world in fascinating ways:</p>

- Flower Petals: Most flowers have a petal count that is a Fibonacci number (e.g., lilies have 3, buttercups have 5, delphiniums have 8).

- Pinecones and Sunflowers: The seeds grow in opposing spirals. If you count the clockwise and counter-clockwise spirals, they are almost always consecutive Fibonacci numbers.

- Shells: The "Golden Spiral" (based on Fibonacci squares) is famously seen in the shell of the chambered nautilus.

- Galaxies: The spiral arms of the Milky Way and other galaxies often follow the path of the Golden Spiral.
