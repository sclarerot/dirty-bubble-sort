import random

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
        "Squidward: I order the food, you cook the food, the customer gets the food. We do that for 40 years, and then we die.",
        "SpongeBob: The pioneers used to ride these babies for miles!",
        "Patrick: Hey, you guys wanna hear a bathroom joke?",
        "Patrick: Then I guess you're gonna miss...The panty raid.",
        "SpongeBob: Remember, licking doorknobs is illegal on other planets.",
        "Tom: It took us three days to make that potato salad. Three days!",
        "Plankton: Goodbye everyone, I'll remember you all in therapy.",
        "SpongeBob: I thought of something funnier than 24...",
        "Squidward: But it's my only night to be fancy!",
        "SpongeBob: I knew a guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy, who knew this guy’s cousin…",
        "Patrick: What's so great about a nerdy pickle?",
        "Mr. Krabs: Did you smell it? That smell. A kind of smelly smell. The kind of smelly smell that smells…smelly.",
        "Plankton: That’s it, mister! You just lost your brain privileges.",
        "Patrick: I can't see my forehead... >:(",
        "Squidward: SpongeBob is the only guy I know who can have fun with a jellyfish…for 12 hours!",
        "Mr. Krabs: I used to have a kidney stone.",
        "SpongeBob: Run Mr. Krabs! Run like you’re not in a coma!",
        "Squilliam: I hope the audience brings lots of...Ibuprofen!",
        "SpongeBob: If I were to die right now in a fiery explosion due to the carelessness of a friend…Then that would be just alright."
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

def dirty_bubble_sort() -> None:
    dirty_list: list[int] = create_random_list()
    print(f"Oh no! The Dirty Bubble's d i r t y list of integers!\n{dirty_list}\n")
    sorted_list: list[int] = bubble_sort(dirty_list)
    print(f"The conch signal?\n{sorted_list}\nMermaid Man and Barnacle Boy save the day again!\n")
    
    quote: str = generate_quote()
    print(f"{quote}\n")
    print("You wanna see me do it again?")

def main():
    over: bool = False
    while not over:
        dirty_bubble_sort()
        asking: bool = True
        while asking:
            answer: str = input("[y/n?]: ").lower()
            match answer:
                case "y":
                    asking = False
                case "n":
                    print("(𓁹 𓁹)\nyou will come back to me, because you are the sweet nectar of life's fruit. you are all i have. i live for you...\n- The Dirty Bubble")
                    over = True
                    asking = False
                case _:
                    print("Type y or n, barnacle brain...")

if __name__ == "__main__":
    main()
