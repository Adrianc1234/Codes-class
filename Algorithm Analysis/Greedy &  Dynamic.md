## Greedy Algorithms and Dynamic Programming

### Greedy Algorithms

Greedy algorithms are a problem-solving strategy that follows the idea of choosing the locally optimal option at each step with the hope of finding the global optimum at the end. They do not guarantee optimal solutions in all cases, but they are efficient for certain problems.

These algorithms, also known as "myopic algorithms", are a methodology for solving problems that follows an iterative and myopic approach. At each step, the algorithm chooses the most promising or "best" available option without considering the future consequences of that choice. This "best" option is selected according to a local optimization criterion, with the hope that these local choices will lead to an optimal global solution for the entire problem.

**Characteristics of Greedy Algorithms:**

* **Greedy Choice:** At each step, the algorithm makes a choice that seems to be the best at that time, based on a local optimization criterion.
* **Local Optimization:** It does not review previously made decisions or consider future ones. It only focuses on maximizing or minimizing the immediate selection criterion.
* **No Backtracking:** Once a decision is made, the algorithm never backtracks to reconsider it, even if that decision does not turn out to be optimal.
* **Efficiency:** Greedy algorithms tend to be more efficient in terms of execution time compared to other approaches, although this may come at the cost of not always finding the global optimal solution.

**Applications of Greedy Algorithms:**

* Fractional knapsack problem
* Kruskal's algorithm for finding the minimum spanning tree
* Dijkstra's algorithm for finding the shortest path

**Example: The change problem:**

Given a set of coin denominations and a change value, the goal is to find the minimum number of coins needed to make that change.

Denominations: 1, 5, 10, 25
Change: 36 cents

**Greedy Solution:**

```python
def cambio_greedy(monedas, cambio):
    monedas.sort(reverse=True)  # Sort coins from highest to lowest
    total_monedas = 0
    for moneda in monedas:
        while cambio >= moneda:
            cambio -= moneda
            total_monedas += 1
    return total_monedas

# Example usage
monedas = [1, 5, 10, 25]
cambio = 36
print(f"Monedas necesarias: {cambio_greedy(monedas, cambio)}")
```

**Greedy Exercise:**

Given coin denominations [1, 3, 4] and a change value of 6, use the greedy approach to find the minimum number of coins required.


## Dynamic Programming

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems and storing the results of these so that they do not have to be recalculated, thus optimizing execution time. It is especially useful in optimization problems.

In short, it is a technique for solving optimization problems by breaking the problem into simpler subproblems, solving them once and storing their solutions (in what is called "memoization" or by using tabulation), so that when the same subproblem occurs again, the solution is already available and does not need to be recalculated.

**Characteristics of Dynamic Programming:**

* **Decomposition into Subproblems:** DP decomposes the main problem into smaller and more manageable subproblems.
* **Solution Storage:** Stores the solutions of the subproblems in a table (array or matrix), thus avoiding the redundant work of solving the same subproblem multiple times.
* **Bottom-Up or Top-Down Solution:** It can build solutions starting from the simplest subproblems and moving up to the complete problem (bottom-up) or by decomposing the main problem into subproblems recursively until reaching the base cases and then combining those solutions (top-down).
* **Optimization:** DP is especially useful in optimization problems, where the most efficient solution (maximum or minimum) is sought among all possible ones.

**Applications of Dynamic Programming:**

* 0-1 knapsack problem
* Fibonacci number calculation
* Bellman-Ford algorithm for finding the shortest path in graphs with negative weights

**Example: Fibonacci**

The Fibonacci sequence is a classic example where dynamic programming can significantly improve efficiency over a simple recursive implementation.

**Dynamic Programming Solution:**

```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Example usage
n = 10
print(f"Fibonacci de {n}: {fibonacci_dp(n)}")
```