# Data
costs = [
    [90, 76, 75, 70],
    [35, 85, 55, 65],
    [125, 95, 90, 105],
    [45, 110, 95, 115],
    [60, 105, 80, 75],
    [45, 65, 110, 95],
]

num_workers = len(costs)
num_tasks = len(costs[0])

team1 = [0, 2, 4]
team2 = [1, 3, 5]
team_max = 2  # Maximum total tasks for any team

params_dict = {
    'costs': costs,
    'num_workers': num_workers,
    'num_tasks': num_tasks,
    'team1': team1,
    'team2': team2,
    'team_max': team_max
}

input = {
    "problem": "Assignment Problem with Team Capacity Constraints",
    "code_example": '''def solve(costs: list, num_workers: int, num_tasks: int, team1: list, team2: list, team_max: int):\n    """\n    Args:\n        costs: matrix where costs[i][j] is the cost of assigning worker i to task j\n        num_workers: total number of workers\n        num_tasks: total number of tasks to be assigned\n        team1: list of worker indices belonging to team 1\n        team2: list of worker indices belonging to team 2\n        team_max: maximum number of tasks that can be assigned to all workers in a single team combined\n\n    Returns:\n        obj: the minimum total cost of assigning all tasks while respecting team capacities\n    """\n    obj = -1\n    return obj\n''',
    'solver': 'OR-tools'
}

optimal = -1 # Placeholder cho giá trị tối ưu