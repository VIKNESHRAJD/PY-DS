#SIMPLE PROGRAMS

n = int(input("Enter n: "))

total = n*(n+1) // 2

print("Sum:", total)


# SWAP TWO NUMBERs without a Temporray Variable

a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("a =", a, "b =", b)


# Largest of Three Numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print("Largest:", max(a,b,c))



# Reverse a String

string = input("Enter a string: ")
print("Reversed string:" , string[::-1])



#Count Digits in an Integer

n = int(input("Enter an integer: "))
count = len(str(abs(n)))
print("Number of digits: ", count)


# Sum of Element in a List

lst = list(map(int,input("Enter list elements: ").split()))
print("Sum:", sum(lst))

#Average MARKS OF STUDENTS

MARKS = list(map(float,input("Enter Marks: ").split()))
average = sum(MARKS) / len(MARKS)
print("Average marks: ", average)


#Even or ODD Check

n = int(input("Enter an integer: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


#Palindrome Check

p = input("Enter a String: ")
if p == p[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


#Amstrong Number Check

n = int(input("Enter a number: "))
digits = list(map(int, str(n)))
power = len(digits)
if sum(d ** power for d in digits) == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


#Factorial Using a Loop
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
 fact *= i
print("Factorial:", fact)


# First n Fibonacci Numbers
n = int(input("Enter n: "))
a, b = 0, 1
for _ in range(n):
 print(a, end=" ")
 a, b = b, a + b


#Multiplication Table of a Number
n = int(input("Enter a number: "))
for i in range(1, 11):
 print(n, "x", i, "=", n * i)
    
# Prime Numbers up to n
n = int(input("Enter n: "))
for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


# Count Even Numbers in a List
lst = list(map(int, input("Enter list elements: ").split()))
count = sum(1 for x in lst if x % 2 == 0)
print("Even count:", count)


## Count Vowels in a String
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Vowel count:", count)


#Remove Duplicate Elements from a List
lst = list(map(int, input("Enter list elements: ").split()))
unique = list(set(lst))
print("Without duplicates:", unique)
 ##Remove Duplicate Elements from a List
