#Задача А
print("Привет, Яндекс!")

#Задача B
print("Как Вас зовут?")
print(f"Привет, {input()}")

#Задача C
something = input()
print(f"{something}\n" * 3, sep="", end="")

#Задача D
price = 38
weight = 2.5
money = int(input())
print(money - int(price * weight))

#Задача E
price = int(input())
weight = int(input())
money = int(input())
print(money - price * weight)

#Задача F
name = input()
price = int(input())
weight = int(input())
money = int(input())
total = int(price * weight)
change = money - total
answer = f"""Чек
{name} - {weight}кг - {price}руб/кг
Итого: {total}руб
Внесено: {money}руб
Сдача: {change}руб"""
print(answer)

#Задача G
phrase = "Купи слона!"
repeat_times = int(input())
phrase_to_print = (phrase + "\n") * repeat_times
print(phrase_to_print)

#Задача H
repeat_times = int(input())
phrase = input()
for i in range(repeat_times):
    print(f'Я больше никогда не буду писать "{phrase}"!')

#Задача I
n, m = int(input()), int(input())
print(n * m // 2)

#Задача J
name = input()
locker = input()
group = int(locker) // 100
bed = int(locker) // 10 % 10
number = int(locker) % 10
answer = f"""Группа №{group}.
{number}. {name}.
Шкафчик: {locker}.
Кроватка: {bed}."""
print(answer)

#Задача K
num = input()
print(num[:2][::-1], num[2:][::-1], sep="")

#Задача L
one = int(input())
two = int(input())
ones = (one % 10 + two % 10) % 10
tens = ((one // 10) % 10 + (two // 10) % 10) % 10
hundreds = (one // 100 + two // 100) % 10
result = ones + tens * 10 + hundreds * 100
print(result)

#Задача M
children = int(input())
candies = int(input())
if children:
    candies_per_child = candies // children
    candies_left = candies - candies_per_child * children
else:
    candies_left = candies
    candies_per_child = children
print(candies_per_child, candies_left, sep="\n")

#Задача N
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

#Задача O
hours = int(input())
minutes = int(input())
delivery_time = int(input())
if delivery_time < 60:
    minutes += delivery_time
else:
    hours += delivery_time // 60
    minutes += delivery_time % 60
if minutes >= 60:
    hours += minutes // 60
    minutes = minutes % 60
if hours > 23:
    hours %= 24
print(f"{hours:02d}:{minutes:02d}")

#Задача P
point_a = int(input())
point_b = int(input())
speed = int(input())
distance = ((point_b - point_a) ** 2) ** 0.5
time_to_point_b = distance / speed
print(f"{time_to_point_b:.2f}")