pair_ = 0
rem = 0
result = []
random_num = int(input("Введите число от 3 до 20: "))
if random_num < 3:
    print("Число должно быть больше 3 и меньше 20")
    random_num = int(input("Введите число от 3 до 20: "))
if random_num > 20:
    print("Число должно быть больше 3 и меньше 20")
    random_num = int(input("Введите число от 3 до 20: "))
for i in range(1, random_num):
    for j in range(i + 1, random_num):
        if i != j:
            pair_ = i + j
            rem = random_num % pair_
            if rem == 0:
                result.append([i, j])
print(result)



