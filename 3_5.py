#Задача А
from sys import stdin

sum_of_numbers = 0
for line in stdin:
    sum_of_numbers += sum(map(int, line.rstrip("\n").split()))
print(sum_of_numbers)

#Задача B
from sys import stdin

height = 0
counter = 0

for line in stdin:
    _, before, after = line.rstrip("\n").split()
    height += float(after) - float(before)
    counter += 1

avg_height_gain = round(height / counter)
print(avg_height_gain)

#Задача C
from sys import stdin

for line in stdin:
    line = line.rstrip("\n")
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

#Задача D
from sys import stdin

headers = [line.rstrip("\n") for line in stdin]
searching_word = headers.pop().lower()

for header in headers:
    if searching_word in header.lower():
        print(header)

#Задача E
from sys import stdin

words = set()
for line in stdin:
    words |= set(line.rstrip("\n").split())

for word in sorted(words):
    length = len(word)
    if length == 1:
        print(word)
    else:
        mid = length // 2
        index = mid + length % 2
        if word[:mid].lower() == word[index:][::-1].lower():
            print(word)

#Задача F
TRANS_DICT = {
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
with open("cyrillic.txt", "r", encoding="UTF-8") as file_in, open(
    "transliteration.txt", "w", encoding="UTF-8"
) as file_out:
    while cyrillic_line := file_in.readline():
        latin_text = []
        for char in cyrillic_line:
            trans_char = TRANS_DICT.get(char.upper(), char)
            if char.isupper():
                latin_text.append(trans_char.capitalize())
            else:
                latin_text.append(trans_char.lower())
        file_out.writelines(latin_text)

#Задача G
file_name = input()
array = []
counter = 0
positives = 0
total_sum = 0
minimum = float("inf")
maximum = float("-inf")

with open(file_name, "r", encoding="UTF-8") as file:
    while line := file.readline():
        for number in line.split():
            number = int(number)
            positives += number > 0
            minimum = min(minimum, number)
            maximum = max(maximum, number)
            total_sum += number
            counter += 1

avg = total_sum / counter

print(counter, positives, minimum, maximum, total_sum, f"{avg:.2f}", sep="\n")

#Задача H
file_one = input()
file_two = input()
file_out = input()

with open(file_one, "r", encoding="UTF-8") as file:
    first_set = set()
    while line := file.readline():
        words = line.rstrip("\n").split()
        first_set.update(words)

with open(file_two, "r", encoding="UTF-8") as file:
    second_set = set()
    while line := file.readline():
        words = line.rstrip("\n").split()
        second_set.update(words)

unique_words = sorted(first_set ^ second_set)

with open(file_out, "w", encoding="UTF-8") as file_out:
    file_out.write("\n".join(unique_words))

#Задача I
file_to_clean = input()
clean_file = input()

with open(file_to_clean, "r", encoding="UTF-8") as file_in, open(
    clean_file, "w", encoding="UTF-8"
) as file_out:
    while line := file_in.readline():
        words = line.replace("\t", "").split()
        if words:
            file_out.write(" ".join(words) + "\n")

#Задача J
file_name = input()
tail = int(input())

lines = []

with open(file_name, "r", encoding="UTF-8") as file:
    while line := file.readline():
        lines.append(line)

print(*lines[-tail:], sep="")

#Задача K
import json

file_name = input()
file_output = input()

counter = 0
positive_count = 0
total_sum = 0
minimum = float("inf")
maximum = float("-inf")

with open(file_name, "r", encoding="UTF-8") as file:
    while line := file.readline():
        for number in line.split():
            number = int(number)
            positive_count += number > 0
            total_sum += number
            minimum = min(minimum, number)
            maximum = max(maximum, number)
            counter += 1

average = round(total_sum / counter, 2)

json_like = {
    "count": counter,
    "positive_count": positive_count,
    "min": minimum,
    "max": maximum,
    "sum": total_sum,
    "average": average,
}

with open(file_output, "w", encoding="UTF-8") as json_file:
    json.dump(json_like, json_file, indent=4)

#Задача L
numbers_file = input()
even_file = input()
odd_file = input()
eq_file = input()

with (
    open(numbers_file, "r", encoding="UTF-8") as file_in,
    open(even_file, "w", encoding="UTF-8") as even_out,
    open(odd_file, "w", encoding="UTF-8") as odd_out,
    open(eq_file, "w", encoding="UTF-8") as equal_out,
):

    while line := file_in.readline():
        even_list, odd_list, equal_list = [], [], []
        for str_number in line.split():
            length = len(str_number)
            even, odd = 0, 0

            for i in range(length):
                digit = int(str_number[i])

                even += digit % 2 == 0
                odd += digit % 2 != 0

            if even == odd:
                equal_list.append(str_number)
            elif even > odd:
                even_list.append(str_number)
            else:
                odd_list.append(str_number)

        even_out.write(f"{' '.join(even_list)}\n")
        odd_out.write(f"{' '.join(odd_list)}\n")
        equal_out.write(f"{' '.join(equal_list)}\n")

#Задача M
import ast
import json
from sys import stdin

json_file = input()
with open(json_file, "r+", encoding="UTF-8") as file:
    json_to_update = json.load(file)

    for line in stdin:
        key, value = line.rstrip("\n").split(" == ")
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            pass
        json_to_update[key] = value

    file.seek(0)

    json.dump(json_to_update, file, ensure_ascii=False, indent=4)

    file.truncate()

#Задача N
import json

users_file = input()
updates_file = input()

with (
    open(users_file, "r+", encoding="UTF-8") as file_one,
    open(updates_file, "r", encoding="UTF-8") as file_two,
):
    users = json.load(file_one)
    updates = json.load(file_two)

    users += updates
    updated_users = {}

    for user in users:
        name = user["name"]
        updated_users[name] = updated_users.get(name, {})
        for key, value in user.items():
            if key != "name":
                flag = updated_users[name].get(key, "")
                if flag < value:
                    updated_users[name][key] = value

    file_one.seek(0)
    json.dump(updated_users, file_one, ensure_ascii=False, indent=4)
    file_one.truncate()

#Задача O
import json
from sys import stdin

student_answers = [line.rstrip("\n") for line in stdin]

with open("scoring.json", "r", encoding="UTF-8") as json_file:
    scoring = json.load(json_file)

student_grade = 0
index = 0

for problem in scoring:
    point_per_test = problem["points"] // len(problem["tests"])

    for test in problem["tests"]:
        studen_answer = student_answers[index]
        right_answer = test["pattern"]

        if studen_answer == right_answer:
            student_grade += point_per_test
        index += 1

print(student_grade)

#Задача P
from sys import stdin

searching_phrase = input().lower()

files_with_the_phrase = []
flag = True

for file_name in stdin:
    file_name = file_name.rstrip("\n")

    with open(file_name, "r", encoding="UTF-8") as file:
        clean_list = []

        while line := file.readline():
            clean_line = " ".join(line.replace("&nbsp;", " ").split())
            if clean_line:
                clean_list.append(clean_line)

    clean_text = " ".join(clean_list).lower()

    if searching_phrase in clean_text:
        print(file_name)
        flag = False

if flag:
    print("404. Not Found")
