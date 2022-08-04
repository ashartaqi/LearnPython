def previous_current_num_adder(x):
    a = 0
    for i in range(x + 1):
        if i == 1 and a == 1:
            a = 0

        print(f'Current Number {i} Previous Number {a} Sum:  {i + a}')

        a += 1


def name_2_spaces(name):
    size = len(name)
    for i in range(1, size + 1, 2):
        print(name[i])


def odd_even_number_finder(number):
    if number % 2 == 0:
        print(f'{number} is a even number')
    else:
        print(f'{number} is a odd number')


def name_letter_counter(lst):
    name_with_less_than_5_letters = 0
    name_with_more_than_5_letters = 0
    for i in lst:
        if len(i) <= 5:
            name_with_less_than_5_letters += 1
        elif len(i) >= 6:
            name_with_more_than_5_letters += 1

    return name_with_less_than_5_letters, name_with_more_than_5_letters


def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


def factorial(n):
    a = 1
    fac = []
    for i in range(1, n + 1):
        a = a * i
        fac.append(a)

    if a in fac:
        print(fac[n - 1])


def pyramid(n):
    for i in range(n):
        for j in range(n - i):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print('')


def bubble_sorting(lst):
    x = len(lst)
    for i in range(x - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def insertion_sort(lst):
    x = len(lst)
    for i in range(1, x + 1):
        for j in range(i):
            if lst[j] > lst[j - 1]:
                lst[j], lst[j - 1] = lst[j], lst[j - 1]

    return lst


def selection_sort(lst):
    for i in range(0, len(lst) - 1):
        current_minimum = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[current_minimum]:
                current_minimum = j
        lst[i], lst[current_minimum] = lst[current_minimum], lst[i]

        return lst


def linear_search(lst, n):
    pos = -1
    for i in lst:
        if i == n:
            pos = i
            return True
    return False


# THE linear_search FUNCTION CAN BE USED LIKE MENTIONED BELOW

# lst1 = [2, 3, 5, 9, 1, 4]
# x = int(input())
# if linear_search(lst1, x):
#     print('found', pos + 1)
# else:
#     print('not found')


def binary_search(lst, x):
    upper_bound = len(lst) - 1
    lower_bound = 0

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2

        if lst[mid] == x:
            return True
        else:
            if x < lst[mid]:
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

    return False
# THE linear_search FUNCTION CAN BE USED LIKE MENTIONED BELOW

# lst1 = [2, 5, 1, 6, 5, 9, 56, 23, 9]
# lst1.sort()
# if binary_search(lst1, 3):
#     print('found')
# else:
#     print('not found')

