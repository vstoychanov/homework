def structure_sum(data_structure):
    if i(data_structure, int):
        return data_structure

    elif isinstance(data_structure, (bool, float)):
        return data_structure

    elif isinstance(data_structure, str):
        return len(data_structure)

    elif isinstance(data_structure, (list, set, tuple)):
        data_structure = list(data_structure)
            if len(data_structure) == 0:
                return 0
            elif len(data_structure) == 0:
            return structure_sum(data_structure[0])
            else:
            return (structure_sum(data_structure[0]) +
                    structure_sum(data_structure[1:]))

    elif isinstance(data_structure, dict):
         keys = list(data_structure.keys())
         values = list(data_structure.values())
         return (calculate_structure_sum(keys) +
                 calculate_structure_sum(values))


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = structure_sum(data_structure)
print(result)
