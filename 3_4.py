#Задача А
items = input().split()

for index, item in enumerate(items, 1):
    print(f"{index}. {item}")

#Задача B
first_group = input().split(", ")
second_group = input().split(", ")

for child_one, child_two in zip(first_group, second_group):
    print(f"{child_one} - {child_two}")

#Задача C
start, end, step = map(float, input().split())
flag = step > 0

while True:
    if flag and start > end:
        break
    elif not flag and start < end:
        break
    print(f"{start:.2f}")
    start += step

#Задача D
text = input().split()

for i in range(1, len(text) + 1):
    print(*text[:i])

#Задача E
groceries = []
for _ in range(3):
    line = input().split(", ")
    if line[0]:
        groceries += line
groceries.sort()

for index, item in enumerate(groceries, 1):
    print(f"{index}. {item}")

#Задача F
from itertools import product

suits = ["пик", "треф", "бубен", "червей"]
pips_and_faces = list(range(2, 11))
pips_and_faces += ["валет", "дама", "король", "туз"]

suit_to_remove = input()
suits.remove(suit_to_remove)

for pip_or_face, suit in product(pips_and_faces, suits):
    print(pip_or_face, suit)

#Задача G
from itertools import combinations

n = int(input())
players = (input() for _ in range(n))
for player_one, player_two in combinations(players, 2):
    print(f"{player_one} - {player_two}")

#Задача H
n = int(input())
porridge = [input() for _ in range(n)]
repeats = int(input())

counter, i = 0, 0
while counter < repeats:
    print(porridge[i])
    counter += 1
    i += 1
    if i == n:
        i = 0

#Задача I
from itertools import product

n = int(input())
ENDS = [" ", "\n"]

for i, j in product(range(1, n + 1), repeat=2):
    print(i * j, end=ENDS[j == n])

#Задача J
from itertools import product

num = int(input())
print("А Б В")

for a, b in product(range(1, num - 1), repeat=2):
    c = num - a - b
    if c >= 1:
        print(a, b, c)

#Задача K
from itertools import product

n, m = int(input()), int(input())
formatter = len(str(n * m))
ENDS = [" ", "\n"]

for i, j in product(range(1, n + 1), range(1, m + 1)):
    number = (i - 1) * m + j
    print(f"{number:>{formatter}}", end=ENDS[j == m])

#Задача L
from itertools import chain

n = int(input())

groceries = chain.from_iterable(input().split(", ") for _ in range(n))
sorted_groceries = sorted(groceries)

index = 1
for item in sorted_groceries:
    if item:
        print(f"{index}. {item}")
        index += 1

#Задача M
from itertools import permutations

n = int(input())
athletes = sorted([input() for _ in range(n)])

for perm in permutations(athletes):
    print(", ".join(perm))

#Задача N
from itertools import permutations

n = int(input())
athletes = sorted([input() for _ in range(n)])
number_of_places = min(n, 3)

for top_3_or_less in permutations(athletes, number_of_places):
    print(", ".join(top_3_or_less))

#Задача O
from itertools import chain, permutations

n = int(input())
groceries = chain.from_iterable(input().split(", ") for _ in range(n))
sorted_groceries = sorted(groceries)

for options in permutations(sorted_groceries, 3):
    print(" ".join(options))

#Задача P
from itertools import permutations, product

given_suit = input().strip()
pip_to_drop = input()

CARD_SUITS = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}
suit = CARD_SUITS[given_suit]

pips_and_faces = list(map(str, range(2, 11)))
pips_and_faces += ["валет", "дама", "король", "туз"]
pips_and_faces.remove(pip_to_drop)

products = sorted(
    map(lambda x: " ".join(x), product(pips_and_faces, CARD_SUITS.values()))
)

answers = []
for line in permutations(products, 3):
    if len(answers) == 10:
        break
    elif any(suit in item for item in line):
        answers.append(sorted(line))

for line in answers:
    print(", ".join(sorted(line)))
