# Data
costs = [
    [90, 76, 75, 70, 50, 74, 12, 68],
    [35, 85, 55, 65, 48, 101, 70, 83],
    [125, 95, 90, 105, 59, 120, 36, 73],
    [45, 110, 95, 115, 104, 83, 37, 71],
    [60, 105, 80, 75, 59, 62, 93, 88],
    [45, 65, 110, 95, 47, 31, 81, 34],
    [38, 51, 107, 41, 69, 99, 115, 48],
    [47, 85, 57, 71, 92, 77, 109, 36],
    [39, 63, 97, 49, 118, 56, 92, 61],
    [47, 101, 71, 60, 88, 109, 52, 90],
]

task_sizes = [10, 7, 3, 12, 15, 4, 11, 5]
total_size_max = 15
num_workers = len(costs)
num_tasks = len(costs[0])

params_dict = {
    'costs': costs,
    'task_sizes': task_sizes,
    'total_size_max': total_size_max,
    'num_workers': num_workers,
    'num_tasks': num_tasks
}

input = {
    "problem": "Generalized Assignment Problem with Task Sizes (GAP)",
    "code_example": '''def solve(costs: list, task_sizes: list, total_size_max: int, num_workers: int, num_tasks: int):\n    """\n    Args:\n        costs: matrix where costs[i][j] is the cost of assigning worker i to task j\n        task_sizes: list where task_sizes[j] is the size of task j\n        total_size_max: maximum total size of tasks that can be assigned to any single worker\n        num_workers: total number of available workers\n        num_tasks: total number of tasks to be assigned\n\n    Returns:\n        obj: the minimum total cost of assigning all tasks\n    """\n    obj = -1\n    return obj\n''',
    'solver': 'OR-tools'
}

optimal = 326