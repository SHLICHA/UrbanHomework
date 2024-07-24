def calculate(data):
    sum_ = 0
    print(data)
    if isinstance(data, dict):
        for key, value in data.items():
            sum_ += calculate(key)
            sum_ += calculate(value)
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            sum_ += calculate(i)
    elif isinstance(data, (int, float)):
        sum_ += data
    elif isinstance(data, str):
        sum_ += len(data)
    return sum_

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate(data_structure)
print(result)