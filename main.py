import random

# TODO: Add more quotes.
def generate_quote() -> str:
    quotes_list: list[str] = [
        "Patrick: Why thank you, Sandy. Take patty. Too bad SpongeBob isn't here to enjoy this. These are his favorite. I sure wish he'd come home. Take bite.",
        "Patrick: The inner machinations of my mind are an enigma.",
        "Old Man Walker: See you later, Bran Flakes. What a nice cereal box!",
        "Mr. Krabs: Give to the children's fund? What have the children ever done for me?",
        "Mr. Krabs: One, two, blue, applesauce...",
        "Nat Peterson: Hey, pal. You just blow in from Stupid Town?",
        "Patrick: That penny has the most beautiful voice...",
        "Barnacle Boy: I'm tired of playing second banana to a man who wears a bra!",
        "The Dirty Bubble: Oh, and make him eat dirt!",
        "Squidward: I order the food, you cook the food, the customer gets the food. We do that for 40 years, and then we die."
    ]

    quote: str = random.choice(quotes_list)

    return quote

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

# TODO: Add main loop.
