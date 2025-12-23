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
    [0, 0, 1, 1],  # Workers 2, 3
    [0, 1, 0, 1],  # Workers 1, 3
    [0, 1, 1, 0],  # Workers 1, 2
    [1, 1, 0, 0],  # Workers 0, 1
    [1, 0, 1, 0],  # Workers 0, 2
]

group2 = [
    [0, 0, 1, 1],  # Workers 6, 7
    [0, 1, 0, 1],  # Workers 5, 7
    [0, 1, 1, 0],  # Workers 5, 6
    [1, 1, 0, 0],  # Workers 4, 5
    [1, 0, 0, 1],  # Workers 4, 7
]

group3 = [
    [0, 0, 1, 1],  # Workers 10, 11
    [0, 1, 0, 1],  # Workers 9, 11
    [0, 1, 1, 0],  # Workers 9, 10
    [1, 0, 1, 0],  # Workers 8, 10
    [1, 0, 0, 1],  # Workers 8, 11
]

sizes = [10, 7, 3, 12, 15, 4] # Đã điều chỉnh size tương ứng với 6 tasks trong cost
total_size_max = 15
num_workers = len(cost)
num_tasks = len(cost[0])

params_dict = {
    'cost': cost,
    'group1': group1,
    'group2': group2,
    'group3': group3,
    'sizes': sizes,
    'total_size_max': total_size_max,
    'num_workers': num_workers,
    'num_tasks': num_tasks
}

input = {
    "problem": "Assignment Problem with Group Logic Constraints and Task Sizes",
    "code_example": '''def solve(cost: list, group1: list, group2: list, group3: list, sizes: list, total_size_max: int, num_workers: int, num_tasks: int):\n    """\n    Args:\n        cost: matrix of assignment costs\n        group1, group2, group3: lists of allowed assignment combinations (boolean/indicator) for specific worker subsets\n        sizes: the size/weight of each task\n        total_size_max: maximum capacity for each worker\n        num_workers: total number of workers\n        num_tasks: total number of tasks\n\n    Returns:\n        obj: the minimum total cost of assigning all tasks\n    """\n    obj = -1\n    return obj\n''',
    'solver': 'OR-tools'
}

optimal = -1 # Placeholder