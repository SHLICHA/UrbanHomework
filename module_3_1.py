def count_calls():
    global calls
    calls += 1

def string_info(string: str):
    count_calls()
    line_info = (len(string), string.upper(), string.lower())
    return line_info

def is_contains(line: str, list_to_search: list):
    count_calls()
    lower_list = [line.lower() for line in list_to_search]
    if line.lower() in lower_list:
        return True
    return False

calls = 0
print("1: ", string_info("Привет"))
print("2: ", string_info("Дивный новый мир"))
print("3: ", is_contains("Привет", ['привет', 'дивный', 'новый', 'мир']))
print("4: ", is_contains('ХоТеЛоСь', ['хотелось', 'бы', 'узнать', 'что-то', 'новое']))
print("5: ", is_contains("Нет", ['такое', 'слово', 'есть']))
print(f"Количество вызовов: {calls}")