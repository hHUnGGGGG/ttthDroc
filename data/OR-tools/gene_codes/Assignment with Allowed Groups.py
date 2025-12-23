
# Import the required module from OR-Tools
from ortools.linear_solver import pywraplp

# Define the function to solve the problem
def solve(cost: list, group1: list, group2: list, group3: list, num_workers: int, num_tasks: int):
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Create variables
    x = {}
    for worker in range(num_workers):
        for task in range(num_tasks):
            # Create a boolean variable for each worker-task pair
            x[worker, task] = solver.BoolVar(f'x[{worker},{task}]')
    
    # Create constraints
    for worker in range(num_workers):
        # Each worker can be assigned to at most one task
        solver.Add(solver.Sum([x[worker, task] for task in range(num_tasks)]) <= 1)
    for task in range(num_tasks):
        # Each task needs to be assigned to exactly one worker
        solver.Add(solver.Sum([x[worker, task] for worker in range(num_workers)]) == 1)
    
    # Create variables to represent whether a worker is working or not
    work = {}
    for worker in range(num_workers):
        work[worker] = solver.BoolVar(f'work[{worker}]')
    for worker in range(num_workers):
        # If a worker is assigned to a task, then the worker is working
        solver.Add(work[worker] == solver.Sum([x[worker, task] for task in range(num_tasks)]))
    
    # Create constraints for the groups
    for group in [group1, group2, group3]:
        constraint_group = solver.Constraint(1, 1)
        for index, _ in enumerate(group):
            constraint = solver.Constraint(0, 1)
            # If a worker in a group is working, then the group is working
            constraint.SetCoefficient(work[group[index][0]], 1)
            constraint.SetCoefficient(work[group[index][1]], 1)
            p = solver.BoolVar(f'g_p{index}')
            constraint.SetCoefficient(p, -2)
            constraint_group.SetCoefficient(p, 1)
    
    # Create the objective function
    objective_terms = []
    for worker in range(num_workers):
        for task in range(num_tasks):
            # The objective is to minimize the total cost
            objective_terms.append(cost[worker][task] * x[worker, task])
    solver.Minimize(solver.Sum(objective_terms))
    
    # Solve the problem
    status = solver.Solve()
    
    # Check the status of the solution
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        # If the problem has an optimal solution, return the objective value
        obj = solver.Objective().Value()
    else:
        # If the problem does not have an optimal solution, return -1
        obj = -1
    return obj
