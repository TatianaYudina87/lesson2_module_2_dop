def generate_password(n):
    result = []
    # Перебираем все возможные пары чисел от 1 до 20
    for a in range(1, 21):
        for b in range(1, 21):
            # Проверяем, чтобы пары были уникальными (a != b)
            if a < b:
                pair_sum = a + b
                # Проверяем кратность
                if n % pair_sum == 0:
                    # Добавляем пару в строку результата
                    result.append(f"{a}{b}")

    # Объединяем все найденные пары в одну строку
    return ''.join(result)

# Основная программа
if __name__ == "__main__":
    n = int(input("Введите число от 3 до 20: "))
    if 3 <= n <= 20:
        password = generate_password(n)
        print("Нужный пароль:", password)
    else:
        print("Число должно быть в диапазоне от 3 до 20.")