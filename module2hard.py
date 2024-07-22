def create_pass(num):
    password = ""
    for j in range(1, (num // 2) + 1):
        for k in range(j, num):
            if (num % (j+k) == 0) and (j != k):
                password += f'{j}{k}'
    return password
num = 1
while num != 0:
    num = int(input("Введите число (от 3 до 20). Для выхода введите 0: "))
    if (num >= 3) and (num <= 20):
        result = create_pass(num)
        print(f"Для числа {num} пароль {result}")
    else:
        print("Вы ввели неверное число! Введите число от 3 до 20")
print("Спасибо")