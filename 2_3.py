#Задача А
while (shouts := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")

#Задача B
bunny_counter = 0
while (words := input()) != "Приехали!":
    bunny_counter += "зайка" in words.lower()
print(bunny_counter)

#Задача C
start, end = int(input()), int(input())
print(*range(start, end + 1))

#Задача D
start, end = int(input()), int(input())
if start > end:
    print(*range(start, end - 1, -1))
else:
    print(*range(start, end + 1))

#Задача E
total = 0
while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    total += price
print(total)

#Задача F
a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)

#Задача G
a = int(input())
b = int(input())
ab_prod = a * b
while b:
    a, b = b, a % b
lcm = ab_prod // a
print(lcm)

#Задача H
something = input()
repeat_times = int(input())
for _ in range(repeat_times):
    print(something)

#Задача I
number = int(input())
if number == 0:
    print(1)
else:
    for i in range(1, number):
        number *= i
    print(number)

#Задача J
x, y = 0, 0
is_direction = True
while (word := input()) != "СТОП":
    if is_direction:
        direction = word
        is_direction = False
    else:
        steps = int(word)
        match direction:
            case "СЕВЕР":
                x += steps
            case "ЮГ":
                x -= steps
            case "ВОСТОК":
                y += steps
            case "ЗАПАД":
                y -= steps
        is_direction = True
print(x, y, sep="\n")

#Задача K
num = int(input())
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(total)

#Задача L
number = int(input())
max_num = number % 10
while number > 0:
    digit = number % 10
    if digit > max_num:
        max_num = digit
    number //= 10
print(max_num)

#Задача M
n = int(input())
first_turn = None
for _ in range(n):
    name = input()
    if not first_turn:
        first_turn = name
    elif name < first_turn:
        first_turn = name
print(first_turn)

#Задача N
number = int(input())
is_prime = True
if number <= 1:
    is_prime = False
elif number <= 3:
    is_prime = True
elif number % 2 == 0 or number % 3 == 0:
    is_prime = False
elif is_prime:
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            is_prime = False
            break
        i += 6
if is_prime:
    print("YES")
else:
    print("NO")

#Задача O
n = int(input())
bunny_counter = 0
for _ in range(n):
    bunny_counter += "зайка" in input()
print(bunny_counter)

#Задача P
number = int(input())

number_copy = number
reversed_number = 0

while number_copy > 0:
    digit = number_copy % 10
    reversed_number = reversed_number * 10 + digit
    number_copy //= 10

is_palindrome = number == reversed_number

if is_palindrome:
    print("YES")
else:
    print("NO")