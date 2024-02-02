import utils

print(utils.factorial(6))

print(utils.NSD(120, 5))

print(utils.sum(120, 5))

print(utils.fibonacci(5))



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

print(utils.pyatirka(3))
