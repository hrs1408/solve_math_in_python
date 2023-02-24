# This is a sample Python script.
import math


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(title):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{title}')  # Press F9 to toggle the breakpoint.


eps = 0.00001


# 1
def exercise_one(x):
    k = 0
    s = 1
    term = 1

    while abs(term) > 1e-8:
        k += 1
        term *= x / k
        s += term

    return s


# Kiểm tra với giá trị x = 5
print(f"Example One: {exercise_one(float(5)):.8f}")


# 2
def exercise_two(x):
    i = 1
    first = 1
    second = first - ((((i + 1) * (i + 2)) / 2) * x ** i)

    while abs(first - second) > eps:
        i += 1
        first = second

        if i % 2 == 0:
            second = first + ((((i + 1) * (i + 2)) / 2) * x ** i)
        else:
            second = first - ((((i + 1) * (i + 2)) / 2) * x ** i)

    return first


# Kiểm tra với giá trị x = 0.5
print(f"Example Two: {exercise_two(0.5)}")


# 3
def exercise_three(x):
    i = 1
    first = -x
    second = first - ((x ** (i + 1)) / (i + 1))

    while abs(second - first) > 0.0001:
        i += 1
        first = second
        second = first - ((x ** (i + 1)) / (i + 1))

    return first


print(f"Example Three: {exercise_three(float(-1))}")


# 4
def exercise_four(x):
    i = 1
    first = 1
    numerator = 1
    denominator = 2

    second = first + (numerator / denominator) * x
    numerator_step = 1
    denominator_step = 4

    while abs(first - second) > eps:
        i += 1
        first = second

        numerator *= numerator_step
        denominator *= denominator_step

        numerator_step += 2
        denominator_step += 2

        if i % 2 == 0:
            second -= (numerator / denominator) * x ** i
        else:
            second += (numerator / denominator) * x ** i

    return first


print(f"Example Four: {exercise_four(float(0.5))}")


# 5
def exercise_five(x):
    i = 1
    first = 1
    numerator = 1
    denominator = 2
    numerator_step = 3
    denominator_step = 4

    second = first - (numerator / denominator) * x
    while abs(first - second) > eps:
        i += 1
        numerator *= numerator_step
        denominator *= denominator_step

        numerator_step += 2
        denominator_step += 2
        first = second

        if i % 2 == 0:
            second += (numerator / denominator) * x ** i
        else:
            second -= (numerator / denominator) * x ** i

    return first


# Kiểm tra với giá trị x = 0.5
print(f"Example Five: {exercise_five(0.5)}")


# 6
def exercise_six(x):
    i = 3

    first = 1
    second = 1 - (x ** i) / math.factorial(i)
    y = 0

    while abs(first - second) > eps:
        i += 2
        y += 1

        first = second

        if i % 2 == 0:
            second -= x ** i / math.factorial(i)
        else:
            second += x ** i / math.factorial(i)

    return first


print(f"Example Six: {exercise_six(1)}")


# 7
def exercise_seven(x):
    i = 2

    first = 1
    second = 1 - (x ** i) / math.factorial(i)
    y = 0

    while abs(first - second) > eps:
        y += 1
        i += 2

        first = second

        if i % 2 != 0:
            second -= x ** i / math.factorial(i)
        else:
            second += x ** i / math.factorial(i)

    return first


print(f"Example Seven: {exercise_seven(1)}")


# # 8
def exercise_eight(x):
    i = 3
    first = x
    numerator = 1
    denominator = 2
    second = first + ((numerator / denominator) * (x ** i) / i)
    while abs(first - second) > eps:
        i += 2
        numerator = numerator * (i - 2)
        denominator = denominator * (i - 1)

        first = second
        second = first + ((numerator / denominator) * (x ** i) / i)
    return first


# Kiểm tra kết quả với x = 0.5
print(f"Example Eight: {exercise_eight(0.5)}")


# 9
def exercise_nine(x):
    step = 2
    i = 0
    first = 1
    second = (first - x ** step / math.factorial(step + 1))

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if i % 2 != 0:
            second = first + x ** step / math.factorial(step + 1)
        else:
            second = first - x ** step / math.factorial(step + 1)
    return first


# Kiểm tra kết quả với x = 1 và n = 5
print(f"Example Nine: {exercise_nine(1)}")


# 10
def exercise_ten(x):
    step = 3
    i = 0
    first = x
    second = (first - x ** step / step)

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if i % 2 != 0:
            second = first + x ** step / step
        else:
            second = first - x ** step / step

    return first


# Kiểm tra kết quả với x = 0.5
print(f"Example Ten: {exercise_ten(0.5)}")


# 11
def exercise_eleven(x):
    step = 3
    first = x
    second = first + x ** step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / step
    return first


# Kiểm tra kết quả với x = 0.5
print(f"Example Eleven: {exercise_eleven(0.5)}")


# 12
def exercise_twelve(x):
    step = 3
    first = x
    second = first + x ** step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / step
    return first


# Kiểm tra kết quả với x = 0.5
print(f"Example Twelve: {exercise_twelve(0.5)}")


# 13
def exercise_thirteen(x):
    step = 3
    first = x
    second = first + x ** step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / math.factorial(step)
    return first


# Kiểm tra kết quả với x = 0.5
print(f"Example Thirteen {exercise_thirteen(0.5)}")


# 14
def exercise_fourteen(x):
    step = 2
    first = x
    second = first + x ** step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / math.factorial(step)
    return first


# Kiểm tra kết quả với x = 0.5
print(f"Example Fourteen: {exercise_fourteen(0.5)}")

if __name__ == '__main__':
    print_hi('Exercise-end')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
