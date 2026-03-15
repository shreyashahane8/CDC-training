# assignment_day1.py
# Day 1 Assignment Solutions

# 1. Program to calculate perimeter of a rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
perimeter = 2 * (length + width)
print("Perimeter of rectangle:", perimeter)

print("\n-----------------------\n")

# 2. Program to convert kilometers into meters and centimeters
km = float(input("Enter distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000
print("Meters:", meters)
print("Centimeters:", centimeters)

print("\n-----------------------\n")

# 3. Program to calculate total bill of 3 products
p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
total_bill = p1 + p2 + p3
print("Total bill amount:", total_bill)

print("\n-----------------------\n")

# 4. Program to convert hours into minutes and seconds
hours = float(input("Enter hours: "))
minutes = hours * 60
seconds = hours * 3600
print("Minutes:", minutes)
print("Seconds:", seconds)

print("\n-----------------------\n")

# 5. Program to calculate total seconds in given days
days = int(input("Enter number of days: "))
seconds = days * 24 * 60 * 60
print("Total seconds:", seconds)

print("\n-----------------------\n")

# 6. Program to convert rupees into paise
rupees = float(input("Enter amount in rupees: "))
paise = rupees * 100
print("Amount in paise:", paise)
