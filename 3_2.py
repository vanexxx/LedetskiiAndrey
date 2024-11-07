#Задача А
set_it = set(input())
print(*set_it, sep="")

#Задача B
one = set(input())
two = set(input())
print(*one.intersection(two), sep="")

#Задача C
n = int(input())
neighborhoods = set()

for _ in range(n):
    neighborhoods |= set(input().split())

print(*neighborhoods, sep="\n")

#Задача D
n, m = int(input()), int(input())

porridge_one = {input() for _ in range(n)}
porridge_two = {input() for _ in range(m)}

length = len(porridge_one & porridge_two)

if length:
    print(length)
else:
    print("Таких нет")

#Задача E
n, m = int(input()), int(input())

unique_children = len({input() for _ in range(n + m)})

if not n or not m:
    print(max(n, m))

elif unique_children == n == m:
    print("Таких нет")

else:
    print(2 * unique_children - n - m)

#Задача F
n, m = int(input()), int(input())

one_porridge_lovers = set()

for _ in range(n + m):
    child = input()
    if child in one_porridge_lovers:
        one_porridge_lovers.remove(child)
    else:
        one_porridge_lovers.add(child)

if one_porridge_lovers:
    print(*sorted(one_porridge_lovers), sep="\n")
else:
    print("Таких нет")

#Задача G
MORSE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}
phrase = input().split()
for word in phrase:
    code = [MORSE_DICT[char.upper()] for char in word]
    print(*code)

#Задача H
n = int(input())
preferences = {}

for _ in range(n):
    line = input().split()
    # Last name -> porridge (might be plural)
    preferences[line[0]] = set(line[1:])

searching_porrigde = input()
last_names = set()

for last_name, porridge in preferences.items():
    if searching_porrigde in porridge:
        last_names.add(last_name)

if last_names:
    print(*sorted(last_names), sep="\n")
else:
    print("Таких нет")

#Задача I
counter = {}
while surroundings := input().split():
    for thing in surroundings:
        if thing not in counter:
            counter[thing] = 0
        counter[thing] += 1

sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

for key, value in sorted_counter:
    print(key, value)

#Задача J
trans_dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ь": "",
    "Ъ": "",
}
text = input()
latin_text = []
for char in text:
    trans_char = trans_dict.get(char.upper(), char)
    if char.isupper():
        latin_text.append(trans_char.capitalize())
    else:
        latin_text.append(trans_char.lower())
print("".join(latin_text))

#Задача K
from collections import defaultdict

n = int(input())
last_names_counter = defaultdict(int)

for _ in range(n):
    last_name = input()
    last_names_counter[last_name] += 1

result = 0
for counter in last_names_counter.values():
    result += counter if counter > 1 else 0

print(result)

#Задача L
from collections import defaultdict

n = int(input())
last_names_counter = defaultdict(int)

for _ in range(n):
    last_name = input()
    last_names_counter[last_name] += 1

flag = True

for last_name, counter in sorted(last_names_counter.items()):
    if counter > 1:
        print(f"{last_name} - {counter}")
        flag = False

if flag:
    print("Однофамильцев нет")

#Задача M
n = int(input())
all_dishes = set(input() for _ in range(n))

days = int(input())
served_dishes = set()

for _ in range(days):
    number_of_dishes = int(input())
    served_dishes |= set(input() for _ in range(number_of_dishes))

dishes_left = all_dishes - served_dishes

if dishes_left:
    print(*sorted(dishes_left), sep="\n")
else:
    print("Готовить нечего")

#Задача N
number_of_groceries = int(input())
groceries = set(input() for _ in range(number_of_groceries))
number_of_recipies = int(input())

recipies = []

for _ in range(number_of_recipies):
    recipie = input()
    number_of_ingredients = int(input())
    ingredients = set(input() for _ in range(number_of_ingredients))

    if ingredients.issubset(groceries):
        recipies.append(recipie)

if recipies:
    print(*sorted(recipies), sep="\n")
else:
    print("Готовить нечего")

#Задача O
digits = map(int, input().split())
answer = []
for digit in digits:
    binary = bin(digit)[2:]
    digits = len(binary)
    units = binary.count("1")
    zeros = digits - units
    answer.append({"digits": digits, "units": units, "zeros": zeros})
print(answer)

#Задача P
SEARCH_WORD = "зайка"
closest_objects = set()
while surroundings := input().split():
    n = len(surroundings)
    for i in range(n):
        if surroundings[i] == SEARCH_WORD:
            if i > 0:
                closest_objects.add(surroundings[i - 1])
            if i < n - 1:
                closest_objects.add(surroundings[i + 1])
print(*closest_objects, sep="\n")