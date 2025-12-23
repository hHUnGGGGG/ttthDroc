# Data
# cost[source][target] đại diện cho chi phí để gán source cho target
cost = [
    [90, 76, 75, 80],
    [35, 85, 55, 65],
    [125, 95, 90, 105],
    [45, 110, 95, 115]
]

num_sources = 4
num_targets = 4

params_dict = {
    'num_sources': num_sources,
    'num_targets': num_targets,
    'cost_matrix': cost
}

input = {
    "problem": "Linear Sum Assignment",
    "objective": "Minimize the total cost of assigning each source to exactly one target",
    "method": "SimpleLinearSumAssignment (Minimum Cost Perfect Matching in Bipartite Graph)",
    "code_example": '''def solve(num_sources, num_targets, costs):
    """
    Args:
        num_sources: Number of workers/sources.
        num_targets: Number of tasks/targets.
        costs: 2D matrix of assignment costs.

    Logic:
        1. Initialize SimpleLinearSumAssignment.
        2. Add arcs between all sources and targets with their respective costs.
        3. Solve the assignment problem.
        4. Retrieve the optimal assignment for each source.
    """
    from ortools.graph.python import linear_sum_assignment
    
    assignment = linear_sum_assignment.SimpleLinearSumAssignment()
    for s in range(num_sources):
        for t in range(num_targets):
            assignment.add_arc_with_cost(s, t, costs[s][t])

    status = assignment.solve()

    if status == assignment.OPTIMAL:
        results = []
        for i in range(assignment.number_of_nodes()):
            results.append((i, assignment.right_mate(i), assignment.assignment_cost(i)))
        return results, assignment.optimal_cost()
    return None, -1
''',
    'solver': 'OR-Tools Graph Library'
}

# Theo dữ liệu: cost[0][3] + cost[1][2] + cost[2][1] + cost[3][0]
# 80 + 55 + 95 + 45 = 275
optimal = 275