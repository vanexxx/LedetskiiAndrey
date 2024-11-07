#Задача А
[i**2 for i in range(a, b + 1)]

#Задача B
[[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

#Задача C
[len(word) for word in sentence.split()]

#Задача D
{number for number in numbers if number & 1}

#Задача E
{num for num in numbers if int(num**0.5) == num**0.5}

#Задача F
{
    char: sum(c == char for c in text.lower())
    for char in text.lower()
    if char.isalpha()
}

#Задача G
{
    num: [i for i in range(1, num + 1) if num % i == 0]
    for num in numbers
}

#Задача H
"".join([word[0].upper() for word in string.split()])

#Задача I
" - ".join(map(str, sorted(set(numbers))))

#Задача J
"".join(i * j for i, j in rle)