#Задача А
name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
whatsapp = input("Как дела?\n")
match whatsapp:
    case "плохо":
        print("Всё наладится!")
    case "хорошо":
        print("Я за вас рада!")

#Задача B
petya_speed = float(input())
vasya_speed = float(input())
if petya_speed > vasya_speed:
    print("Петя")
else:
    print("Вася")

#Задача C
petya_speed = float(input())
vasya_speed = float(input())
tolya_speed = float(input())
if petya_speed < vasya_speed > tolya_speed:
    print("Вася")
elif vasya_speed < petya_speed > tolya_speed:
    print("Петя")
else:
    print("Толя")

#Задача D
name_one = "Петя"
name_two = "Вася"
name_three = "Толя"
speed_one = float(input())
speed_two = float(input())
speed_three = float(input())
if speed_one < speed_two:
    speed_one, speed_two = speed_two, speed_one
    name_one, name_two = name_two, name_one
if speed_one < speed_three:
    speed_one, speed_three = speed_three, speed_one
    name_one, name_three = name_three, name_one
if speed_two < speed_three:
    speed_two, speed_three = speed_three, speed_two
    name_two, name_three = name_three, name_two
print(f"1. {name_one}")
print(f"2. {name_two}")
print(f"3. {name_three}")

#Задача E
petya = 7
vasya = 6
petya, vasya = petya - 3 + 2, vasya + 3 + 5 - 2
n, m = int(input()), int(input())
petya += n
vasya += m
if petya > vasya:
    print("Петя")
elif petya < vasya:
    print("Вася")
else:
    print("Ровно")

#Задача F
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print("YES")
else:
    print("NO")

#Задача G
str_number = input()
number = int(str_number)
ones = number % 10
tens = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number // 1000
if thousands == ones and tens == hundreds:
    print("YES")
else:
    print("NO")

#Задача H
string = input()
if "зайка" in string:
    print("YES")
else:
    print("NO")

#Задача I
name_one = input()
name_two = input()
name_three = input()
if name_one > name_two:
    name_one, name_two = name_two, name_one
if name_one > name_three:
    name_one, name_three = name_three, name_one
print(name_one)

#Задача J
password = int(input())
hundreds = password // 100
tens = password // 10 % 10
ones = password % 10
first_sum = tens + ones
second_sum = hundreds + tens
if first_sum > second_sum:
    print(f"{first_sum}{second_sum}")
else:
    print(f"{second_sum}{first_sum}")

#Задача K
number = int(input())
digit_one = number % 10
digit_two = number % 100 // 10
digit_three = number // 100
if digit_one < digit_two:
    digit_one, digit_two = digit_two, digit_one
if digit_one < digit_three:
    digit_one, digit_three = digit_three, digit_one
if digit_two < digit_three:
    digit_two, digit_three = digit_three, digit_two
is_beautiful = digit_one + digit_three == digit_two * 2
print("YES" if is_beautiful else "NO")

#Задача L
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

#Задача M
number_one = int(input())
number_two = int(input())
number_three = int(input())
first_one = number_one // 10
first_two = number_two // 10
first_three = number_three // 10
if first_one == first_two == first_three:
    print(first_one)
else:
    print(number_one % 10)

#Задача N
number = int(input())
digit_one = number % 10
digit_two = number % 100 // 10
digit_three = number // 100
if digit_one < digit_two:
    digit_one, digit_two = digit_two, digit_one
if digit_one < digit_three:
    digit_one, digit_three = digit_three, digit_one
if digit_two < digit_three:
    digit_two, digit_three = digit_three, digit_two

if digit_three > 0:
    minimum = digit_three * 10 + digit_two
elif digit_two == digit_three == 0:
    minimum = digit_one * 10
else:
    minimum = digit_two * 10

maximum = digit_one * 10 + digit_two
print(minimum, maximum)

#Задача O
number_one = int(input())
number_two = int(input())

digit_one = number_one % 10
digit_two = number_one // 10
digit_three = number_two % 10
digit_four = number_two // 10

if digit_one < digit_two:
    digit_one, digit_two = digit_two, digit_one

if digit_three < digit_four:
    digit_three, digit_four = digit_four, digit_three

if digit_one < digit_three:
    digit_one, digit_three = digit_three, digit_one

if digit_two < digit_four:
    digit_two, digit_four = digit_four, digit_two

hundreds = digit_one * 100
tens = ((digit_two + digit_three) % 10) * 10
units = digit_four

answer = hundreds + tens + units
print(answer)

#Задача P
name_one = "Петя"
name_two = "Вася"
name_three = "Толя"

speed_one = float(input())
speed_two = float(input())
speed_three = float(input())

if speed_one < speed_two:
    speed_one, speed_two = speed_two, speed_one
    name_one, name_two = name_two, name_one

if speed_one < speed_three:
    speed_one, speed_three = speed_three, speed_one
    name_one, name_three = name_three, name_one

if speed_two < speed_three:
    speed_two, speed_three = speed_three, speed_two
    name_two, name_three = name_three, name_two

width = 8
third_name_lenght = len(name_three)

formatter = width * 3 - (width - third_name_lenght) // 2

podium = f"""{name_one: ^24}
{name_two: ^{width}}
{name_three: >{formatter}}
{'II': ^{width}}{'I': ^{width}}{'III': ^{width}}"""

print(podium)