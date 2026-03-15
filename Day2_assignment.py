# assignment_day2.py
# Day 2 Assignment Programs

# 1. Check whether number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("---------------")

# 2. Largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)
print("Largest number is:", largest)

print("---------------")

# 3. Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("---------------")

# 4. Divisible by both 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

print("---------------")

# 5. Print numbers from 1 to N
n = int(input("Enter N: "))
for i in range(1, n+1):
    print(i)

print("---------------")

# 6. Print even numbers from 1 to N
n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

print("---------------")

# 7. Sum of first N natural numbers
n = int(input("Enter N: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum =", sum)

print("---------------")

# 8. Factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial =", fact)

print("---------------")

# 9. Multiplication table
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num*i)

print("---------------")

# 10. Count digits in number
num = int(input("Enter number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Digits:", count)

print("---------------")

# 11. Reverse a number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10
print("Reverse:", rev)

print("---------------")

# 12. Check palindrome
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not palindrome")

print("---------------")

# 13. Sum of digits
num = int(input("Enter number: "))
sum = 0

while num > 0:
    rem = num % 10
    sum += rem
    num = num // 10

print("Sum of digits:", sum)

print("---------------")

# 14. Armstrong number
num = int(input("Enter number: "))
temp = num
digits = len(str(num))
sum = 0

while num > 0:
    rem = num % 10
    sum += rem ** digits
    num = num // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not Armstrong")

print("---------------")

# 15. Numbers divisible by 7 between 1 and N
n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 7 == 0:
        print(i)
