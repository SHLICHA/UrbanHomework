first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
if first == second and second == third:
    print("Ответ: 3")
elif first == second or second == third or first == third:
    print("Ответ: 2")
else:
    print("Ответ: 0")
