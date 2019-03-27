# ODD NUMBERS IN RANGE OF 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# COUNT IN 10S FROM 0 TO 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# COUNT DOWN FROM 20 TO 1
for i in range(20, -1, -1):
    print(i, end=' ')
print()

# PRINT NO. OF STARS
num_stars = int(input("Enter a number: "))
for i in range(num_stars):
    print("*", end=' ')

# PRINT NUMBER OF INCREASING STARS
stars_num = int(input("Enter Number of Stars: "))
for i in range(1, stars_num + 1):
    print("*" * i)
