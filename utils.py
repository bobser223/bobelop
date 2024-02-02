def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum(a, b):
    return a + b


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

def NSD(a, b):
    if b > a:
        a, b = b, a

    while b > 0:
        a, b = b, (a % b)

    return a



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Зчитуємо число від користувача
user_input = int(input("Введіть число: "))

# Перевіряємо, чи є число простим і виводимо результат
if is_prime(user_input):
    print(f"{user_input} - просте число")
else:
    print(f"{user_input} - не є простим числом")