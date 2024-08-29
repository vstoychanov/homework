def find_password(n):
    # Список для хранения пар
    pairs = []

    # Перебираем все пары чисел от 1 до n-1
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            # Если n кратно сумме i и j, добавляем пару в список
            if n % (i + j) == 0:
                pairs.append(f"{i}{j}")

    # Формируем результат
    result = ''.join(pairs)
    return result


# Пример использования
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    print(f"Нужный пароль: {find_password(n)}")
else:
    print("Число должно быть от 3 до 20!")
