# Morgan
# TicTacToe
# 8/18

# Display board
print("|---|---|---|")
print("| a | b | c |")
print("|---|---|---|")
print("| d | e | f |")
print("|---|---|---|")
print("| g | h | i |")
print("|---|---|---|")

# Determines players moves
print("move 1")
m1 = input()
if m1 == "a":
    a = "X"

elif m1 == "b":
    b = "O"
elif m1 == "c":
    c = "X"
elif m1 == "d":
    d = "O"
elif m1 == "e":
    e = "X"
elif m1 == "f":
    f = "O"
elif m1 == "g":
    g = "X"
elif m1 == "h":
    h = "O"
elif m1 == "i":
    i = "O"

print("move 2")
m2 = input()
if m2 == "a":
    a = "X"
elif m2 == "b":
    b = "O"
elif m2 == "c":
    c = "X"
elif m2 == "d":
    d = "O"
elif m2 == "e":
    e = "X"
elif m2 == "f":
    f = "O"
elif m2 == "g":
    g = "X"
elif m2 == "h":
    h = "O"
elif m2 == "i":
    i = "O"

print("move 3")
m3 = input()
if m3 == "a":
    a = "X"
elif m3 == "b":
    b = "O"
elif m3 == "c":
    c = "X"
elif m3 == "d":
    d = "O"
elif m3 == "e":
    e = "X"
elif m3 == "f":
    f = "O"
elif m3 == "g":
    g = "X"
elif m3 == "h":
    h = "O"
elif m3 == "i":
    i = "O"

print("move 4")
m4 = input()
if m4 == "a":
    a = "X"
elif m4 == "b":
    b = "O"
elif m4 == "c":
    c = "X"
elif m4 == "d":
    d = "O"
elif m4 == "e":
    e = "X"
elif m4 == "f":
    f = "O"
elif m4 == "g":
    g = "X"
elif m4 == "h":
    h = "O"
elif m4 == "i":
    i = "O"

print("move 5")
m5 = input()
if m5 == "a":
    a = "X"
elif m5 == "b":
    b = "O"
elif m5 == "c":
    c = "X"
elif m5 == "d":
    d = "O"
elif m5 == "e":
    e = "X"
elif m5 == "f":
    f = "O"
elif m5 == "g":
    g = "X"
elif m5 == "h":
    h = "O"
elif m5 == "i":
    i = "O"

print("move 6")
m6 = input()
if m6 == "a":
    a = "X"
elif m6 == "b":
    b = "O"
elif m6 == "c":
    c = "X"
elif m6 == "d":
    d = "O"
elif m6 == "e":
    e = "X"
elif m6 == "f":
    f = "O"
elif m6 == "g":
    g = "X"
elif m6 == "h":
    h = "O"
elif m6 == "i":
    i = "O"

print("move 7")
m7 = input()
if m7 == "a":
    a = "X"
elif m7 == "b":
    b = "O"
elif m7 == "c":
    c = "X"
elif m7 == "d":
    d = "O"
elif m7 == "e":
    e = "X"
elif m7 == "f":
    f = "O"
elif m7 == "g":
    g = "X"
elif m7 == "h":
    h = "O"
elif m7 == "i":
    i = "O"

print("move 8")
m8 = input()
if m8 == "a":
    a = "X"
elif m8 == "b":
    b = "O"
elif m8 == "c":
    c = "X"
elif m8 == "d":
    d = "O"
elif m8 == "e":
    e = "X"
elif m8 == "f":
    f = "O"
elif m8 == "g":
    g = "X"
elif m8 == "h":
    h = "O"
elif m8 == "i":
    i = "O"

print("move 9")
m9 = input()

if m9 == "a":
    a = "X"
elif m9 == "b":
    b = "O"
elif m9 == "c":
    c = "X"
elif m9 == "d":
    d = "O"
elif m9 == "e":
    e = "X"
elif m9 == "f":
    f = "O"
elif m9 == "g":
    g = "X"
elif m9 == "h":
    h = "O"
elif m9 == "i":
    i = "O"

# Displays final board
print("|---|---|---|")
print("|" ,a, "|" ,b, "|" ,c, "|")
print("|---|---|---|")
print("|" ,d, "|" ,e, "|" ,f, "|")
print("|---|---|---|")
print("|" ,g, "|" ,h, "|" ,i, "|")
print("|---|---|---|")

# Determines if X or O wins
if a == "X" and b == "X" and c == "X":
    print("X wins")
elif a == "O" and b == "O" and c == "O":
    print("O wins")
elif a == "X" and d == "X" and g == "X":
    print("X wins")
elif a == "O" and d == "O" and g == "O":
    print("O wins")
elif c == "X" and f == "X" and i == "X":
    print("X wins")
elif c == "O" and f == "O" and i == "O":
    print("O wins")
elif g == "X" and h == "X" and i == "X":
    print("X wins")
elif g == "O" and h == "O" and i == "O":
    print("O wins")
elif a == "X" and e == "X" and i == "X":
    print("X wins")
elif a == "O" and e == "O" and i == "O":
    print("O wins")
elif g == "X" and e == "X" and c == "X":
    print("X wins")
elif g == "O" and e == "O" and c == "O":
    print("O wins")
elif d == "X" and e == "X" and f == "X":
    print("X wins")
elif d == "O" and e == "O" and f == "O":
    print("O wins")
elif b == "X" and e == "X" and h == "X":
    print("X wins")
elif b == "O" and e == "O" and h == "O":
    print("O wins")