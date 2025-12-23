# Data
cost = [
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

group1 = [
    [2, 3],
    [1, 3],
    [1, 2],
    [0, 1],
    [0, 2],
]

group2 = [
    [6, 7],
    [5, 7],
    [5, 6],
    [4, 5],
    [4, 7],
]

group3 = [
    [10, 11],
    [9, 11],
    [9, 10],
    [8, 10],
    [8, 11],
]

num_workers = len(cost)
num_tasks = len(cost[0])

params_dict = {
    'cost': cost,
    'group1': group1,
    'group2': group2,
    'group3': group3,
    'num_workers': num_workers,
    'num_tasks': num_tasks
}

input = {
    "problem": "Assignment with Allowed Groups",
    "code_example": '''def solve(cost: list, group1: list, group2: list, group3: list, num_workers: int, num_tasks: int):\n    """\n    Args:\n        cost: matrix of assignment costs\n        group1: list of allowed worker pairs for group 1 (workers 0-3)\n        group2: list of allowed worker pairs for group 2 (workers 4-7)\n        group3: list of allowed worker pairs for group 3 (workers 8-11)\n        num_workers: total number of workers\n        num_tasks: total number of tasks\n\n    Returns:\n        obj: the minimum total cost of assigning all tasks\n    """\n    obj = -1\n    return obj\n''',
    'solver': 'OR-tools'
}

optimal = 239