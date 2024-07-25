numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    if num != 1:
        is_prime = True
        for j in range(2, num):
            if num % j == 0:
                is_prime = False
                break
        if not is_prime:
            not_primes.append(num)
        else:
            primes.append(num)
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')

