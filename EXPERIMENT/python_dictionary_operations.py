# Python Dictionary Operations, Frequency Analysis & Comprehensions

# 1. Count Characters Frequency in a String

text = "dictionary"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)


## 2. Filter Dictionary Items by Value

scores = {"A": 4, "B": 68, "C": 98, "D": 40}
filtered_scores = {}

for key, value in scores.items():
    if value > 50:
        filtered_scores[key] = value

print(filtered_scores)


## 3. Find the Key with Maximum Value

marks = {"Siri": 98, "Vendhan": 100, "Vikki": 88}

max_key = None
max_value = 0

for key, value in marks.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key)


## 4. Square Each Value in a Dictionary

nums = {"a": 2, "b": 4, "c": 6}
squared_nums = {}

for key, value in nums.items():
    squared_nums[key] = value ** 2

print(squared_nums)


## 5. Combine Two Lists into a Dictionary

keys = ["id", "name", "age"]
values = [10, "Leo", 20]

combined_dict = {}

for i in range(len(keys)):
    combined_dict[keys[i]] = values[i]

print(combined_dict)


## 6. Count Word Frequency in a Sentence

sentence = "Playing football is simple, but playing simple football is the hardest"

words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


## 7. Swap Keys and Values in a Dictionary

data = {"a": 1, "b": 2, "c": 3}
swapped_data = {}

for key, value in data.items():
    swapped_data[value] = key

print(swapped_data)


## 8. Sum All Values in a Dictionary

expenses = {"Food": 1000, "Rent": 6000, "Travel": 2400}

total = sum(expenses.values())

print(total)


## 9. Filter Dictionary by Value Using Comprehension

scores = {"A": 46, "B": 78, "C": 88, "D": 40}

filtered_scores = {key: value for key, value in scores.items() if value > 50}

print(filtered_scores)


## 10. Square All Values Using Dictionary Comprehension

numbers = {"a": 2, "b": 3, "c": 4}

squared_numbers = {key: value ** 2 for key, value in numbers.items()}

print(squared_numbers)


## 11. Invert Keys and Values using Dictionary Comprehension

data = {"a": 1, "b": 2, "c": 3}

inv_data = {value: key for key, value in data.items()}

print(inv_data)


## 12. Merge Two Dictionaries Keeping Larger Values

d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 25, "c": 15, "d": 40}

all_keys = set(d1) | set(d2)

merged = {
    key: max(d1.get(key, 0), d2.get(key, 0))
    for key in all_keys
}

print(merged)
