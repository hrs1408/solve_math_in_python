# This is a sample Python script.
import math


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# 1
def exp_taylor(x):
    # Khởi tạo giá trị ban đầu của biến k, giá trị của chuỗi và của mỗi số hạng trong chuỗi
    k = 0
    s = 1
    term = 1

    # Lặp cho đến khi đạt được độ chính xác mong muốn
    while abs(term) > 1e-8:
        # Tính giá trị của số hạng tiếp theo trong chuỗi Taylor
        k += 1
        term *= x / k
        s += term

    return s


# Nhập giá trị của x từ bàn phím và tính giá trị của e^x bằng hàm exp_taylor
x = float(input("Nhập giá trị của x: "))
result = exp_taylor(x)

# So sánh kết quả với giá trị tính được bởi hàm math.exp của Python
expected_result = math.exp(x)
print(f"Giá trị của e^{x} là {result:.8f}")
print(f"Kết quả mong đợi là {expected_result:.8f}")


# 2
def maclaurin(x, n):
    # Khởi tạo biến đếm và giá trị của chuỗi
    k = 1
    s = 1

    # Tính giá trị của từng số hạng trong chuỗi Maclaurin
    while k < n:
        # Tính các hệ số
        a = k + 1
        b = k + 2
        c = 2

        # Tính số hạng trong chuỗi
        term = (-1) ** k * a * b / c * x ** (3 * k)
        s += term
        k += 1

    return s


# Nhập giá trị của x từ bàn phím
x = float(input("Nhập giá trị của x: "))

# Tính giá trị của 1/(1+x^3) với 10 số hạng đầu tiên của chuỗi Maclaurin
n = 10
result = maclaurin(x, n)

# In ra kết quả
print(f"Giá trị của 1/(1+x^3) là {result}")


# 4
def sqrt_1_plus_x(x, terms=10):
    """Tính căn bậc hai của (1 + x) bằng chuỗi Taylor với số lượng terms"""
    result = 0
    for n in range(terms):
        numerator = 1
        denominator = 1
        for i in range(n):
            numerator *= (2 * i + 1)
            denominator *= (2 * i + 2)
        term = ((-1) ** n * numerator * x ** (n + 1)) / (denominator * 2 ** n)
        result += term
    return result + 1


# Kiểm tra với giá trị x = 0.5
x = 0.5
print(sqrt_1_plus_x(x))  # Kết quả phải gần bằng math.sqrt(1+x) = math.sqrt(1.5) = 1.224744871391589


# 5
def inv_sqrt_1_plus_x(x, terms=10):
    """Tính nghịch đảo căn bậc hai của (1 + x) bằng chuỗi Taylor với số lượng terms"""
    result = 1
    for n in range(1, terms):
        numerator = 1
        denominator = 1
        for i in range(n):
            numerator *= (2 * i - 1) if i > 0 else (-1)
            denominator *= (2 * i) if i > 0 else 1
        term = ((-1) ** n * numerator * x ** n) / (denominator * 2 ** (n - 1))
        result += term
    return result


# Kiểm tra với giá trị x = 0.5
x = 0.5
print(inv_sqrt_1_plus_x(x))  # Kết quả phải gần bằng 1/math.sqrt(1+x) = 1/math.sqrt(1.5) = 0.816496580927726


# 6
def sin(x, terms=10):
    """Tính giá trị của hàm sin(x) bằng chuỗi Taylor với số lượng terms"""
    result = 0
    sign = 1
    for n in range(terms):
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        term = sign * numerator / denominator
        result += term
        sign *= -1
    return result


# Kiểm tra với giá trị x = pi/4
x = math.pi / 4
print(sin(x))  # Kết quả phải gần bằng math.sin(x) = math.sin(pi/4) = 0.7071067811865476


#7
def cos(x, terms=10):
    """Tính giá trị của hàm cos(x) bằng chuỗi Taylor với số lượng terms"""
    result = 0
    sign = 1
    for n in range(terms):
        numerator = x ** (2 * n)
        denominator = math.factorial(2 * n)
        term = sign * numerator / denominator
        result += term
        sign *= -1
    return result


# Kiểm tra với giá trị x = pi/4
x = math.pi / 4
print(cos(x))  # Kết quả phải gần bằng math.cos(x) = math.cos(pi/4) = 0.7071067811865476


#8
import math

def arcsin(x, terms=10):
    """Tính giá trị của hàm arcsin(x) bằng chuỗi Taylor với số lượng terms"""
    result = 0
    for n in range(terms):
        numerator = 1
        for i in range(2*n):
            numerator *= i + 1
            if i % 2 == 1:
                numerator *= x
        denominator = 2**(2*n) * math.factorial(n)**2 * (2*n + 1)
        term = numerator / denominator
        result += term
    return result

# Kiểm tra với giá trị x = 0.5
x = 0.5
print(arcsin(x)) # Kết quả phải gần bằng math.asin(x) = math.asin(0.5) = 0.5235987755982989


#9
import math


def sin_over_x(x, n):
    """
    Tính giá trị sin(x)/x với n số lượng các số hạng của chuỗi Taylor
    """
    result = 1
    sign = -1
    factorial = 1
    power = x

    for i in range(1, n + 1):
        sign *= -1
        power *= x ** 2
        factorial *= (2 * i - 1) * (2 * i)
        result += sign * power / factorial

    return result


# Kiểm tra kết quả với x = 1 và n = 5
x = 1
n = 5
print(f"sin({x})/{x} = {sin_over_x(x, n)}")
print(f"Giá trị chính xác: {math.sin(x) / x}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
