# ex. 1
def sum_numbers(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    return total


print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc', 'param_1=2'))


# ex. 2
def sum_all_even_odd(n):
    if n == 0:
        return 0, 0, 0
    else:
        all_sum, even_sum, odd_sum = sum_all_even_odd(n - 1)
        all_sum += n
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
        return all_sum, even_sum, odd_sum


print(sum_all_even_odd(10))


# ex. 3
def read_int_from_keyboard():
    value = input("Enter a number: ")
    try:
        return int(value)
    except ValueError:
        return 0


num = read_int_from_keyboard()
print("The input number is:", num)
