# day2_number_programs.py
# Collection of number programs

# 1. Reverse of a Number
def reverse_number():
    no = int(input("Enter number: "))
    rev = 0
    while no > 0:
        rem = no % 10
        rev = rev * 10 + rem
        no = no // 10
    print("Reverse is:", rev)


# 2. Count digits in a number
def count_digits():
    no = int(input("Enter number: "))
    count = 0
    while no > 0:
        no = no // 10
        count = count + 1
    print("Total digits:", count)


# 3. Sum of digits of a number
def sum_of_digits():
    no = int(input("Enter number: "))
    total = 0
    while no > 0:
        rem = no % 10
        total = total + rem
        no = no // 10
    print("Sum of digits:", total)


# 4. Check palindrome number
def palindrome_check():
    no = int(input("Enter number: "))
    temp = no
    rev = 0

    while no > 0:
        rem = no % 10
        rev = rev * 10 + rem
        no = no // 10

    if temp == rev:
        print("Palindrome number")
    else:
        print("Not a palindrome number")


# 5. Check Armstrong number
def armstrong_check():
    no = int(input("Enter number: "))
    temp = no
    count = len(str(no))
    total = 0

    while no > 0:
        rem = no % 10
        total = total + rem ** count
        no = no // 10

    if temp == total:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


# 6. Armstrong numbers from 1 to 10000
def armstrong_range():
    print("Armstrong numbers between 1 and 10000:")
    for i in range(1, 10001):
        no = i
        temp = no
        count = len(str(no))
        total = 0

        while no > 0:
            rem = no % 10
            total = total + rem ** count
            no = no // 10

        if temp == total:
            print(i)


# 7. Series: 1 + x^1/1 + x^2/2 + x^3/3 + ... n
def series_sum():
    n = int(input("Enter n: "))
    x = int(input("Enter x: "))
    total = 1

    for i in range(1, n + 1):
        total = total + (x ** i) / i

    print("Series sum:", total)


# Main Menu
while True:
    print("\n--- Number Programs ---")
    print("1. Reverse a number")
    print("2. Count digits")
    print("3. Sum of digits")
    print("4. Palindrome check")
    print("5. Armstrong check")
    print("6. Armstrong numbers (1-10000)")
    print("7. Series sum")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        reverse_number()
    elif choice == 2:
        count_digits()
    elif choice == 3:
        sum_of_digits()
    elif choice == 4:
        palindrome_check()
    elif choice == 5:
        armstrong_check()
    elif choice == 6:
        armstrong_range()
    elif choice == 7:
        series_sum()
    elif choice == 8:
        print("Exiting program.")
        break
    else:
        print("Invalid choice!")
