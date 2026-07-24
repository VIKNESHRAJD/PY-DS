'''# 1 Prime Number Check using Function

def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter : "))
x = is_prime(n)
print(x)
        
# Fibonacci Numbers Less Than n

n = int(input())
a, b = 0, 1
while a < n:
 print(a, end=" ")
 a, b = b, a + b

# Second Largest Element in a list

lst = list(map(int, input().split()))
largest = max(lst)
second = max(x for x in lst if x != largest)
print(second)

#Character TYPE Count

s= input("Enter a string")
upper = lower = digit = special = 0

for ch in s:
 if ch.isupper():
     upper += 1
 elif ch.islower():
     lower += 1
 elif ch.isdigit():
     digit += 1
 else:
     special += 1
print(upper, lower, digit, special)

# Merge Two Lists Without Duplicates

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
result = []
for x in l1 + l2:
    if x not in result:
        result.append(x)
print(result)

#Anagram Check

s1 = input().replace(" ", "").lower()
s2 = input().replace(" ", "").lower()
print(sorted(s1) == sorted(s2))

# GCD using FUNCTIONS

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
print(gcd(12, 18))
        

#Right Rotate a List by k

lst =list(map(int,input().split()))
k = int(input()) % len(lst)
print(lst[-k:] + lst[:-k])

# Character Frequency Using Dictionary

s = input()
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


## Separate EVEN AND ODD NumberS

lst = list(map(int, input().split()))
even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]
print(even)
print(odd)

## Amstrong NumberS in a Range

for num in range(1,1000):
    order = len(str(num))
    if num == sum(int(d)**order for d in str(num)):
        print(num)

## Perfect Number Check

n = int(input())
s = sum(i for i in range(1,n) if n % i == 0)
print(s == n)

## Sort Tuples by Second Element

lst = [(1,3),(4,1),(2,2)]
lst.sort(key=lambda x: x[1])
print(lst)


##Decimal to Binary, Octal, and Hexadecimal

n = int(input())
def convert(n, base):
    res = ""
    digits = "0123456789ABCDEF"
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res
print(convert(n, 2), convert(n, 8), convert(n, 16))

## First Non-Repeating Character
s = input()
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

#Transpose of a Matrix

matrix = [[1,2,3],[4,5,6]]
transpose = list(map(list, zip(*matrix)))
print(transpose)


# Password Validations

pwd = input()
valid = (len(pwd) >= 8 and
         any(c.isupper() for c in pwd) and
         any(c.islower() for c in pwd) and
         any(c.isdigit() for c in pwd))
print(valid)

# Student Marks Dicrionary

students ={"A":85, "B": 98, "C": 88}
top = max(students, key=students.get)
print(top, students[top])

## Menu Driven Calculator using Functions

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b != 0 else None


a = int("ENTER A :")
b = int("ENTER B :")
add


# Remove Duplicate
sentence = input().split()
result = []
for word in sentence:
    if word not in result:
        result.append(word)
print(" ".join(result))




