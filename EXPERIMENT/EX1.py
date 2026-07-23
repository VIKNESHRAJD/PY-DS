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



