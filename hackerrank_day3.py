# Day 3 – HackerRank Basic Problems Practice


# 1. Solve Me First
def solveMeFirst(a, b):
    return a + b

a = int(input())
b = int(input())
print(solveMeFirst(a, b))


# ----------------------------------

# 2. Simple Array Sum
n = int(input())
arr = list(map(int, input().split()))

total = 0
for i in arr:
    total += i

print(total)


# ----------------------------------

# 3. Compare the Triplets
a = list(map(int, input().split()))
b = list(map(int, input().split()))

alice = 0
bob = 0

for i in range(3):
    if a[i] > b[i]:
        alice += 1
    elif a[i] < b[i]:
        bob += 1

print(alice, bob)


# ----------------------------------

# 4. A Very Big Sum
n = int(input())
arr = list(map(int, input().split()))

print(sum(arr))


# ----------------------------------

# 5. Simple Python Division
a = int(input())
b = int(input())

print(a // b)
print(a / b)


# ----------------------------------

# 6. Python If-Else
n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
