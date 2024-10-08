def is_prime(func):
    def wrapper(*args):
        result_f = func(*args)
        print(result_f)
        for i in range(2, result_f):
            if (result_f % i) == 0:
                return 'Составное'
        return 'Простое'
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(2, 3, 6)
print(result)
