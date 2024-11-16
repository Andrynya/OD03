def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda x: x < element, s))
    center = [x for x in s if x == element]
    right = list(filter(lambda x: x > element, s))

    return quick_sort(left) + center + quick_sort(right)

s = [1, 2, 4, 3, 8, 5, 7, 9]
print(quick_sort(s))