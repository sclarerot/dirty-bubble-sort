import random

def bubble_sort(li: list[int]) -> list[int]:
    is_sorted: bool = False
    while not is_sorted:
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        if li == sorted(li):
            is_sorted = True
        
    return li

test_list = [4, 74, 23, 5, 5, 6, 8, 4]

print(test_list)
print(bubble_sort(test_list))