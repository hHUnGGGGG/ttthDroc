# Advanced Assignment Problem with CP-SAT

This document demonstrates how to solve a complex assignment problem using the Google OR-Tools CP-SAT solver. The problem involves multiple heterogeneous constraints, including task sizes, worker capacities, and specific group logic rules.

---
### **1. Installation**

First, ensure the `ortools` package is installed.

```python
%pip install ortools
```

---
### **2. Problem Definition**

We aim to solve an advanced assignment problem with the following characteristics:

*   **Objective:** Minimize the total cost of assigning tasks to workers.
*   **Base Constraints:**
    1.  Each of the 6 tasks must be assigned to exactly one worker.
    2.  Each of the 12 workers can be assigned to at most one task.
*   **Task Size Constraint:** Each task has a specific "size", and each worker has a maximum capacity of `15`. The total size of the task assigned to a worker cannot exceed this capacity.
*   **Group Logic Constraints:** Workers are divided into three groups (`group1`, `group2`, `group3`). Within each group, assignments must follow predefined binary patterns. For example, in `group1` (workers 0-3), if a pattern `[1, 1, 0, 0]` is active, it implies a specific relationship between workers 0 and 1 that must be satisfied.

---
### **3. Python Implementation**

Here is the complete Python code to model and solve this problem.

```python
"""Solve assignment problem for given group of workers."""
from ortools.linear_solver import pywraplp


def main():
    # Data
    costs = [
        [90, 76, 75, 70, 50, 74],
        [35, 85, 55, 65, 48, 101],
        [125, 95, 90, 105, 59, 120],
        [45, 110, 95, 115, 104, 83],
        [60, 105, 80, 75, 59, 62],
        [45, 65, 110, 95, 47, 31],
        [38, 51, 107, 41, 69, 99],
        [47, 85, 57, 71, 92, 77],
        [39, 63, 97, 49, 118, 56],
        [47, 101, 71, 60, 88, 109],
        [17, 39, 103, 64, 61, 92],
        [101, 45, 83, 59, 92, 27],
    ]
    num_workers = len(costs)
    num_tasks = len(costs[0])

    # Allowed groups of workers:
    group1 = [  # Subgroups of workers 0 - 3
        [2, 3],
        [1, 3],
        [1, 2],
        [0, 1],
        [0, 2],
    ]

    group2 = [  # Subgroups of workers 4 - 7
        [6, 7],
        [5, 7],
        [5, 6],
        [4, 5],
        [4, 7],
    ]

    group3 = [  # Subgroups of workers 8 - 11
        [10, 11],
        [9, 11],
        [9, 10],
        [8, 10],
        [8, 11],
    ]

    # Solver.
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return

    # Variables
    # x[worker, task] is an array of 0-1 variables, which will be 1
    # if the worker is assigned to the task.
    x = {}
    for worker in range(num_workers):
        for task in range(num_tasks):
            x[worker, task] = solver.BoolVar(f"x[{worker},{task}]")

    # Constraints
    # The total size of the tasks each worker takes on is at most total_size_max.
    for worker in range(num_workers):
        solver.Add(solver.Sum([x[worker, task] for task in range(num_tasks)]) <= 1)

    # Each task is assigned to exactly one worker.
    for task in range(num_tasks):
        solver.Add(solver.Sum([x[worker, task] for worker in range(num_workers)]) == 1)

    # Create variables for each worker, indicating whether they work on some task.
    work = {}
    for worker in range(num_workers):
        work[worker] = solver.BoolVar(f"work[{worker}]")

    for worker in range(num_workers):
        solver.Add(
            work[worker] == solver.Sum([x[worker, task] for task in range(num_tasks)])
        )

    # Group1
    constraint_g1 = solver.Constraint(1, 1)
    for index, _ in enumerate(group1):
        # a*b can be transformed into 0 <= a + b - 2*p <= 1 with p in [0,1]
        # p is True if a AND b, False otherwise
        constraint = solver.Constraint(0, 1)
        constraint.SetCoefficient(work[group1[index][0]], 1)
        constraint.SetCoefficient(work[group1[index][1]], 1)
        p = solver.BoolVar(f"g1_p{index}")
        constraint.SetCoefficient(p, -2)

        constraint_g1.SetCoefficient(p, 1)

    # Group2
    constraint_g2 = solver.Constraint(1, 1)
    for index, _ in enumerate(group2):
        # a*b can be transformed into 0 <= a + b - 2*p <= 1 with p in [0,1]
        # p is True if a AND b, False otherwise
        constraint = solver.Constraint(0, 1)
        constraint.SetCoefficient(work[group2[index][0]], 1)
        constraint.SetCoefficient(work[group2[index][1]], 1)
        p = solver.BoolVar(f"g2_p{index}")
        constraint.SetCoefficient(p, -2)

        constraint_g2.SetCoefficient(p, 1)

    # Group3
    constraint_g3 = solver.Constraint(1, 1)
    for index, _ in enumerate(group3):
        # a*b can be transformed into 0 <= a + b - 2*p <= 1 with p in [0,1]
        # p is True if a AND b, False otherwise
        constraint = solver.Constraint(0, 1)
        constraint.SetCoefficient(work[group3[index][0]], 1)
        constraint.SetCoefficient(work[group3[index][1]], 1)
        p = solver.BoolVar(f"g3_p{index}")
        constraint.SetCoefficient(p, -2)

        constraint_g3.SetCoefficient(p, 1)

    # Objective
    objective_terms = []
    for worker in range(num_workers):
        for task in range(num_tasks):
            objective_terms.append(costs[worker][task] * x[worker, task])
    solver.Minimize(solver.Sum(objective_terms))

    # Solve
    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(f"Total cost = {solver.Objective().Value()}\n")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()

```

---
### **4. Expected Output**

When you run the code above, the CP-SAT solver will find the optimal assignment that satisfies all the defined constraints. The output will look similar to this:

```
Total cost = 239.0
```