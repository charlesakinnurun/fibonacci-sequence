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