#Задача А
n = int(input())
ENDS = " \n"

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=ENDS[j == n])

#Задача B
n = int(input())
RNG = range(1, n + 1)
for i in RNG:
    for j in RNG:
        print(f"{j} * {i} = {i * j}")

#Задача C
n = int(input())
ENDS = " \n"
line = 1

for i in range(1, n + 1):
    cond = i == (line * (line + 1)) // 2
    line += cond
    print(i, end=ENDS[cond])

#Задача D
n = int(input())
total = 0
for _ in range(n):
    number = int(input())
    while number > 0:
        total += number % 10
        number //= 10
print(total)

#Задача E
n = int(input())
total = 0
for _ in range(n):
    bunnies = 0
    while (word := input()) != "ВСЁ":
        bunnies += word == "зайка"
    total += bool(bunnies)
print(total)

#Задача F
n = int(input())
a = int(input())
for _ in range(1, n):
    b = int(input())
    while b:
        a, b = b, a % b
gcd = a if a > 0 else -a
print(gcd)

#Задача G
n = int(input())
for i in range(n):
    for j in range(3 + i, 0, -1):
        print(f"До старта {j} секунд(ы)")
    print(f"Старт {i + 1}!!!")

#Задача H
n = int(input())
winner, max_number = None, 0

for _ in range(n):
    name = input()
    number = int(input())
    sum_of_digits = 0

    while number > 0:
        sum_of_digits += number % 10
        number //= 10

    if sum_of_digits >= max_number:
        max_number = sum_of_digits
        winner = name

print(winner)

#Задача I
n = int(input())
for _ in range(n):
    number = int(input())
    max_number = float("-inf")

    while number > 0:
        digit = number % 10
        if digit > max_number:
            max_number = digit
        number //= 10

    print(max_number, end="")

#Задача J
num = int(input())
print("А Б В")
for share_one in range(1, num - 1):
    for share_two in range(1, num - share_one):
        share_three = num - share_one - share_two
        print(share_one, share_two, share_three)

#Задача K
n = int(input())
prime_nums_counter = 0
for _ in range(n):
    number = int(input())
    if number < 2:
        continue
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            break
    else:
        prime_nums_counter += 1

print(prime_nums_counter)

#Задача L
n, m = int(input()), int(input())
ENDS = "\n "
prod_nm = n * m
array = range(1, prod_nm + 1)
formatter = 0

while prod_nm > 0:
    formatter += 1
    prod_nm //= 10

for num in array:
    print(f"{num:>{formatter}}", end=ENDS[bool(num % m)])

#Задача M
n, m = int(input()), int(input())
ENDS = " \n"
prod = n * m
formatter = 0

while prod > 0:
    prod //= 10
    formatter += 1

for i in range(1, n + 1):
    num = i
    for j in range(m):
        indx = j == m - 1
        print(f"{num:>{formatter}}", end=ENDS[indx])
        num += n

#Задача N
n, m = int(input()), int(input())
ENDS = " \n"
prod = n * m
formatter = 0

while prod > 0:
    prod //= 10
    formatter += 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i % 2:
            index = m * (i - 1) + j
        else:
            index = m * i - (j - 1)
        print(f"{index:>{formatter}}", end=ENDS[j == m])

#Задача O
n, m = int(input()), int(input())
ENDS = " \n"
prod = n * m
formatter = 0

while prod > 0:
    prod //= 10
    formatter += 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j % 2:
            index = n * (j - 1) + i
        else:
            index = n * j - i + 1
        print(f"{index:>{formatter}}", end=ENDS[j == m])

#Задача P
size, width = int(input()), int(input())
for i in range(1, size + 1):
    for j in range(1, size + 1):
        prod = i * j
        print(f"{prod:^{width}}", end="")
        if j < size:
            print("|", end="")
    length = size * width + size - 1
    if i < size:
        print("\n", "-" * length, sep="")