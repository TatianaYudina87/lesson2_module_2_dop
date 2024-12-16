import random
def generate_password(first_number):
    if not 3 <= first_number <= 20:
        return None
    password = ""
    available_numbers = list(range(1, 11))
    while len(available_numbers) >= 2:
        found_pair = False
        for i in range(len(available_numbers)):
            for j in range(i + 1, len(available_numbers)):
                num1 = available_numbers[i]
                num2 = available_numbers[j]
                if (num1 + num2) % first_number == 0:
                    password += str(num1) + str(num2)
                    available_numbers.pop(j)
                    available_numbers.pop(i)
                    found_pair = True
                    break
            if found_pair:
                break
        if not found_pair:
            break
    return password

first_number = random.randint(3, 20)
print(f"Число из первой вставки: {first_number}")
password = generate_password(first_number)

if password:
    print(f"Пароль: {password}")
else:
    print("Ошибка: число должно быть в диапазоне от 3 до 20.")

first_number = 9
print(f"\nЧисло из первой вставки: {first_number}")
password = generate_password(first_number)
print(f"Пароль: {password}")

first_number = 11
print(f"\nЧисло из первой вставки: {first_number}")
password = generate_password(first_number)
print(f"Пароль: {password}")