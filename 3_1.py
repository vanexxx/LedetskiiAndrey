#Задача А
n = int(input())

for _ in range(n):
    word = input()
    first_letter = word[0]
    if first_letter != "а" and first_letter != "б" and first_letter != "в":
        print("NO")
        break
else:
    print("YES")

#Задача B
word = input()
print(*word, sep="\n")

#Задача C
max_length = int(input())
n = int(input())

for _ in range(n):
    sentence = input()
    if len(sentence) > max_length:
        print(f"{sentence[:max_length - 3]}...")
    else:
        print(sentence)

#Задача D
while (line := input()) != "":
    if line.endswith("@@@"):
        pass
    elif line.startswith("##"):
        print(line[2:])
    else:
        print(line)

#Задача E
print('YES' if (line := input()) == line[::-1] else 'NO')

#Задача F
n = int(input())
banny_counter = 0

for _ in range(n):
    items = input().split()
    for item in items:
        banny_counter += "зайка" == item.lower()

print(banny_counter)

#Задача G
numbers = input().split()
sum_of_numbers = 0

for number in numbers:
    sum_of_numbers += int(number)

print(sum_of_numbers)

#Задача H
n = int(input())

for _ in range(n):
    items = input()
    banny_index = items.find("зайка") + 1
    if banny_index:
        print(banny_index)
    else:
        print("Заек нет =(")

#Задача I
while line := input():
    stack = []
    flag = False

    for i in range(len(line)):
        char = line[i]

        if char == "#":
            if not i:
                flag = True
                break
            if not stack:
                print(f"{line[:i].rstrip()}")
                flag = True
                break

        if char in ["'", '"']:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

    if not flag:
        print(line)

#Задача J
CHAR_RANGE = 1104
lines = []

while (line := input()) != "ФИНИШ":
    lines.extend(line.lower().split())

char_count = [0] * CHAR_RANGE

for word in lines:
    for char in word:
        char_count[ord(char)] += 1

max_count = 0

for i in range(CHAR_RANGE):
    if char_count[i] > max_count:
        max_count = char_count[i]
        most_common_char = chr(i)

print(most_common_char if most_common_char else "")

#Задача K
n = int(input())

headers = [input() for _ in range(n)]

to_search = input().lower()

for header in headers:
    if to_search in header.lower():
        print(header)

#Задача L
PORRIDGE = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

n = int(input())

number_of_porridge = len(PORRIDGE)

for i in range(n):
    print(PORRIDGE[i % number_of_porridge])

#Задача M
n = int(input())

numbers = [int(input()) for _ in range(n)]
power = int(input())

for number in numbers:
    powered_number = number**power
    print(powered_number)

#Задача N
list_of_numbers = input().split()
power = int(input())

for number in list_of_numbers:
    powered_number = int(number) ** power
    print(powered_number, end=" ")

#Задача O
a = None

for number in input().split():
    if a is None:
        a = int(number)
        continue

    b = int(number)
    while b:
        a, b = b, a % b

gcd = a if a > 0 else -a
print(gcd)

#Задача P
length, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if length > 3:
        print(i[:length - 3] + "..." if len(i) >= length - 3 else (i + "..." if length == 4 else i))
        length -= len(i)