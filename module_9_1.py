def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        res_func = func(int_list)
        results.update({func.__name__: res_func})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
