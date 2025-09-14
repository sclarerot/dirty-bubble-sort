import random

def create_random_list() -> list[int]:
    random_list: list[int] = []
    size_of_list: int = random.randrange(5, 50)

    for i in range(size_of_list):
        random_int: int = random.randrange(1, 999)
        random_list.append(random_int)

    return random_list


def bubble_sort(li: list[int]) -> list[int]:
    is_sorted: bool = False
    while not is_sorted:
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
        if li == sorted(li):
            is_sorted = True
        
    return li
