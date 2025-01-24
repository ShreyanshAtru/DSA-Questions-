#1.  Program to print half pyramid using *
"""
*
* *
* * *
* * * *
* * * * *
"""
rows = int(input())
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()


# 2. Program to print half pyramid number 
"""
1
12
123
1234
12345
"""

rows = int(input())
for i in range(rows):
    for j in range(i+1):
        print(j+1, end="")
    print()

# 3. Program to print half pyramid using alphabets
"""
A
BB
CCC
DDDD
EEEEE
"""
ascii = 65
for i in range(rows):
    for j in range(i+1):
        print(ascii, end="")
    ascii += 1
    print()

# 4. Programs to print inverted half pyramid using * and numbers
"""
* * * * *
* * * *
* * *
* *
*
"""
for i in range(rows, 1, -1):
    for j in range(i-1):
        print("* ", end="")
    print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""    
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j,end="")
    print()