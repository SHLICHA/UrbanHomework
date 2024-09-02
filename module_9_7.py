def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        counter = 0
        for i in range(2, result):
            if result % i == 0:
                counter += 1
        if counter == 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result = sum_three(3, 5, 8)
print(result)