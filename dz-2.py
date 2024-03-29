# module-4/Home-work-2

import re


text = "1000.28 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів + 1000.00 з акцій та облігацій. 1001.101 ніч"


def generator_numbers(text: str) :
    # Find numbers in text
    pattern = r" \d+.\d+ " # Ваша порада. Знаходить все
    # pattern = r"(?<!^)(?<!\.\s)(?<![\.\d])\b\d+\.\d+\b" # Не шукає на початку речення та після крапки.
    income = re.findall(pattern, text)
    # Gradyally return values
    for money in income:
        yield float(money)


def sum_profit(text: str, func: callable) :
    total_income = 0
    # Taking the value from the function-generator
    for income in func(text):
        total_income += income
    return total_income


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

for number in generator_numbers(text):
    print(number)
