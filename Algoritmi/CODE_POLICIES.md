# Code Policies - Algoritmi e Strutture Dati

> Standard, convenzioni e best practices per implementazione di algoritmi e strutture dati

## 📋 Indice
- [Naming Conventions](#naming-conventions)
- [Complexity Analysis](#complexity-analysis)
- [Code Organization](#code-organization)
- [Common Patterns](#common-patterns)
- [Testing](#testing)
- [Documentation](#documentation)
- [Implementation Guidelines](#implementation-guidelines)
- [Performance](#performance)

---

## Naming Conventions

### Functions and Variables
```python
# ✅ Descriptive names for algorithms
def binary_search(arr, target):
    """Binary search implementation."""
    pass

def merge_sort(arr):
    """Merge sort implementation."""
    pass

# ✅ Clear variable names
left_pointer = 0
right_pointer = len(arr) - 1
mid_point = (left + right) // 2

# ✅ Use standard naming for common concepts
n = len(array)          # Size of input
i, j, k = 0, 0, 0      # Loop indices
left, right = 0, n-1   # Pointers
result = []            # Output

# ❌ Avoid cryptic names
def bs(a, t):  # What is this?
    l = 0
    r = len(a) - 1
```

### Data Structures
```python
# ✅ Clear class names
class BinarySearchTree:
    pass

class LinkedListNode:
    pass

class MinHeap:
    pass

class Graph:
    pass

# ✅ Descriptive attribute names
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False
```

---

## Complexity Analysis

### Document Time and Space Complexity
```python
def binary_search(arr: list, target: int) -> int:
    """
    Binary search implementation.

    Time Complexity: O(log n)
    - We halve the search space each iteration

    Space Complexity: O(1)
    - Only using constant extra space

    Args:
        arr: Sorted array of integers
        target: Value to search for

    Returns:
        Index of target if found, -1 otherwise

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def merge_sort(arr: list) -> list:
    """
    Merge sort implementation.

    Time Complexity: O(n log n)
    - T(n) = 2T(n/2) + O(n)
    - Log n levels, each doing O(n) work

    Space Complexity: O(n)
    - Additional space for merge operation

    Args:
        arr: Array to sort

    Returns:
        Sorted array

    Examples:
        >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
```

### Common Complexities
```python
# Time Complexities (from best to worst)
# O(1)        - Constant
# O(log n)    - Logarithmic (binary search)
# O(n)        - Linear (single loop)
# O(n log n)  - Linearithmic (merge sort, quicksort)
# O(n²)       - Quadratic (nested loops)
# O(n³)       - Cubic (triple nested loops)
# O(2ⁿ)       - Exponential (fibonacci recursive)
# O(n!)       - Factorial (permutations)

# Examples:
def constant_time(arr):
    """O(1) - Accessing array element"""
    return arr[0]

def logarithmic_time(arr, target):
    """O(log n) - Binary search"""
    return binary_search(arr, target)

def linear_time(arr):
    """O(n) - Single pass through array"""
    total = 0
    for num in arr:
        total += num
    return total

def linearithmic_time(arr):
    """O(n log n) - Merge sort"""
    return merge_sort(arr)

def quadratic_time(arr):
    """O(n²) - Bubble sort"""
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def exponential_time(n):
    """O(2ⁿ) - Recursive fibonacci"""
    if n <= 1:
        return n
    return exponential_time(n-1) + exponential_time(n-2)
```

---

## Code Organization

### File Structure
```
algorithms/
├── sorting/
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── heap_sort.py
├── searching/
│   ├── __init__.py
│   ├── binary_search.py
│   ├── linear_search.py
│   └── depth_first_search.py
├── data_structures/
│   ├── __init__.py
│   ├── linked_list.py
│   ├── binary_tree.py
│   ├── graph.py
│   ├── heap.py
│   └── hash_table.py
├── dynamic_programming/
│   ├── __init__.py
│   ├── fibonacci.py
│   ├── longest_common_subsequence.py
│   └── knapsack.py
└── tests/
    ├── test_sorting.py
    ├── test_searching.py
    └── test_data_structures.py
```

### Module Template
```python
"""
Module: binary_search_tree.py
Description: Implementation of Binary Search Tree data structure

Author: Nome Autore
Date: 2025-01-16
Version: 1.0.0
"""

from typing import Optional, List


class TreeNode:
    """Node in a binary search tree."""

    def __init__(self, value: int):
        """
        Initialize a tree node.

        Args:
            value: The value to store in the node
        """
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    """
    Binary Search Tree implementation.

    A binary search tree is a tree where for each node:
    - All values in left subtree are less than node value
    - All values in right subtree are greater than node value

    Attributes:
        root: The root node of the tree

    Examples:
        >>> bst = BinarySearchTree()
        >>> bst.insert(5)
        >>> bst.insert(3)
        >>> bst.insert(7)
        >>> bst.search(3)
        True
        >>> bst.search(10)
        False
    """

    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        """
        Insert a value into the tree.

        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(log n) due to recursion

        Args:
            value: The value to insert
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Optional[TreeNode], value: int) -> TreeNode:
        """Helper method for recursive insertion."""
        if node is None:
            return TreeNode(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value: int) -> bool:
        """
        Search for a value in the tree.

        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(1)

        Args:
            value: The value to search for

        Returns:
            True if value exists, False otherwise
        """
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False


if __name__ == "__main__":
    # Example usage
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 9, 4, 6]

    for val in values:
        bst.insert(val)

    print(f"Search 4: {bst.search(4)}")  # True
    print(f"Search 10: {bst.search(10)}")  # False
```

---

## Common Patterns

### Two Pointers
```python
def two_sum_sorted(arr: list, target: int) -> tuple:
    """
    Find two numbers that sum to target in sorted array.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return (-1, -1)


def remove_duplicates(arr: list) -> int:
    """
    Remove duplicates from sorted array in-place.

    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0

    write_ptr = 1

    for read_ptr in range(1, len(arr)):
        if arr[read_ptr] != arr[read_ptr - 1]:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1

    return write_ptr
```

### Sliding Window
```python
def max_sum_subarray(arr: list, k: int) -> int:
    """
    Find maximum sum of subarray of size k.

    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return -1

    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find longest substring with at most k distinct characters.

    Time: O(n), Space: O(k)
    """
    char_count = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Shrink window if needed
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

### Recursion
```python
def factorial(n: int) -> int:
    """
    Calculate factorial recursively.

    Time: O(n), Space: O(n) due to call stack
    """
    # Base case
    if n <= 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


def fibonacci(n: int, memo: dict = None) -> int:
    """
    Calculate fibonacci number with memoization.

    Time: O(n), Space: O(n)
    """
    if memo is None:
        memo = {}

    # Base cases
    if n <= 1:
        return n

    # Check memo
    if n in memo:
        return memo[n]

    # Calculate and memoize
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
```

### Dynamic Programming
```python
def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find length of longest common subsequence.

    Time: O(m * n), Space: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def coin_change(coins: list, amount: int) -> int:
    """
    Find minimum number of coins to make amount.

    Time: O(amount * len(coins)), Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

---

## Testing

### Test Template
```python
import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    """Test cases for binary search implementation."""

    def test_element_found(self):
        """Test when element exists in array."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 5), 4)

    def test_element_not_found(self):
        """Test when element doesn't exist."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 10), -1)

    def test_empty_array(self):
        """Test with empty array."""
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_found(self):
        """Test with single element that matches."""
        self.assertEqual(binary_search([5], 5), 0)

    def test_single_element_not_found(self):
        """Test with single element that doesn't match."""
        self.assertEqual(binary_search([5], 3), -1)

    def test_first_element(self):
        """Test finding first element."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 1), 0)

    def test_last_element(self):
        """Test finding last element."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 5), 4)


if __name__ == '__main__':
    unittest.main()
```

### Edge Cases to Test
```python
# Always test:
# - Empty input
# - Single element
# - Two elements
# - All elements same
# - Already sorted (for sorting)
# - Reverse sorted (for sorting)
# - Duplicates
# - Very large input
# - Negative numbers (if applicable)
# - Maximum/minimum values
```

---

## Documentation

### Algorithm Documentation Template
```python
"""
Algorithm: Dijkstra's Shortest Path

Description:
    Finds the shortest path from a source vertex to all other vertices
    in a weighted graph with non-negative edge weights.

Approach:
    1. Initialize distances to all vertices as infinite, except source (0)
    2. Use a min-heap to always process the closest unvisited vertex
    3. For each vertex, update distances to its neighbors
    4. Repeat until all vertices are visited

Time Complexity: O((V + E) log V) with binary heap
    - V: number of vertices
    - E: number of edges
    - Each vertex is extracted once: O(V log V)
    - Each edge is relaxed once: O(E log V)

Space Complexity: O(V)
    - Distance array: O(V)
    - Priority queue: O(V)
    - Visited set: O(V)

Optimizations:
    - Use Fibonacci heap: O(E + V log V)
    - Early termination if only finding path to single destination

Limitations:
    - Doesn't work with negative edge weights
    - For negative edges, use Bellman-Ford algorithm

Alternative Algorithms:
    - Bellman-Ford: Works with negative edges, O(VE)
    - A*: Faster with heuristic, O((V + E) log V)
    - Floyd-Warshall: All pairs shortest path, O(V³)

References:
    - Dijkstra, E. W. (1959). "A note on two problems in connexion
      with graphs". Numerische Mathematik. 1: 269–271.

Examples:
    >>> graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
    >>> dijkstra(graph, 0)
    {0: 0, 1: 3, 2: 1, 3: 4}
"""
```

---

## Implementation Guidelines

### General Guidelines
```python
# ✅ Use meaningful variable names
def find_maximum(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

# ✅ Add input validation
def binary_search(arr, target):
    if not arr:
        raise ValueError("Array cannot be empty")
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Array must be sorted")
    # ... implementation

# ✅ Handle edge cases explicitly
def reverse_linked_list(head):
    # Edge case: empty list
    if head is None:
        return None

    # Edge case: single node
    if head.next is None:
        return head

    # General case
    # ... implementation

# ✅ Use helper functions for clarity
def quick_sort(arr):
    """Main quick sort function."""
    if len(arr) <= 1:
        return arr
    return _quick_sort_helper(arr, 0, len(arr) - 1)

def _quick_sort_helper(arr, low, high):
    """Recursive helper for quick sort."""
    # ... implementation

def _partition(arr, low, high):
    """Partition helper for quick sort."""
    # ... implementation
```

---

## Performance

### Optimization Techniques
```python
# ✅ Use appropriate data structures
# Hash table for O(1) lookup
seen = set()  # Instead of list for membership test

# ✅ Avoid unnecessary work
# Early return when possible
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True  # Early return
        seen.add(num)
    return False

# ✅ Use built-in functions (usually optimized in C)
# Slow
result = 0
for num in numbers:
    result += num

# Fast
result = sum(numbers)

# ✅ Cache expensive computations
def fibonacci_memoized(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    return cache[n]
```

---

## Note Aggiuntive

### Resources
- **Books**: Introduction to Algorithms (CLRS), Algorithm Design Manual
- **Online**: LeetCode, HackerRank, CodeSignal
- **Visualizations**: VisuAlgo, Algorithm Visualizer
- **Complexity**: Big-O Cheat Sheet

### Common Mistakes
- Not considering edge cases
- Incorrect time/space complexity analysis
- Off-by-one errors in loops
- Not handling null/empty inputs
- Modifying input when not expected

---

**Ultima revisione**: 2025-11-16
**Versione**: 1.0.0
