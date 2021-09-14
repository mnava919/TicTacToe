# Morgan
# TicTacToe
# 09/09/2021

from tkinter import *
root = Tk()

# Display board
print("You have an array of 3 boards today!")
print("3x3, 5x5, 7x7")
print("What size board size would you like?")
def myClick1():
    print("|---|---|---|")
    print("| a | b | c |")
    print("|---|---|---|")
    print("| d | e | f |")
    print("|---|---|---|")
    print("| g | h | i |")
    print("|---|---|---|")
    root.destroy()
    # Determines players moves
    print("move 1")
    m1 = input()
    if m1 == "a":
        a = "X"
    if m1 == "b":
        b = "X"
    if m1 == "c":
        c = "X"
    if m1 == "d":
        d = "X"
    if m1 == "e":
        e = "X"
    if m1 == "f":
        f = "X"
    if m1 == "g":
        g = "X"
    if m1 == "h":
        h = "X"
    if m1 == "i":
        i = "X"

    print("move 2")
    m2 = input()
    if m2 == "a":
        a = "O"
    if m2 == "b":
        b = "O"
    if m2 == "c":
        c = "O"
    if m2 == "d":
        d = "O"
    if m2 == "e":
        e = "O"
    if m2 == "f":
        f = "O"
    if m2 == "g":
        g = "O"
    if m2 == "h":
        h = "O"
    if m2 == "i":
        i = "O"

    print("move 3")
    m3 = input()
    if m3 == "a":
        a = "X"
    if m3 == "b":
        b = "X"
    if m3 == "c":
        c = "X"
    if m3 == "d":
        d = "X"
    if m3 == "e":
        e = "X"
    if m3 == "f":
        f = "X"
    if m3 == "g":
        g = "X"
    if m3 == "h":
        h = "X"
    if m3 == "i":
        i = "X"

    print("move 4")
    m4 = input()
    if m4 == "a":
        a = "O"
    if m4 == "b":
        b = "O"
    if m4 == "c":
        c = "O"
    if m4 == "d":
        d = "O"
    if m4 == "e":
        e = "O"
    if m4 == "f":
        f = "O"
    if m4 == "g":
        g = "O"
    if m4 == "h":
        h = "O"
    if m4 == "i":
        i = "O"

    print("move 5")
    m5 = input()
    if m5 == "a":
        a = "X"
    if m5 == "b":
        b = "X"
    if m5 == "c":
        c = "X"
    if m5 == "d":
        d = "X"
    if m5 == "e":
        e = "X"
    if m5 == "f":
        f = "X"
    if m5 == "g":
        g = "X"
    if m5 == "h":
        h = "X"
    if m5 == "i":
        i = "X"

    print("move 6")
    m6 = input()
    if m6 == "a":
        a = "O"
    if m6 == "b":
        b = "O"
    if m6 == "c":
        c = "O"
    if m6 == "d":
        d = "O"
    if m6 == "e":
        e = "O"
    if m6 == "f":
        f = "O"
    if m6 == "g":
        g = "O"
    if m6 == "h":
        h = "O"
    if m6 == "i":
        i = "O"

    print("move 7")
    m7 = input()
    if m7 == "a":
        a = "X"
    if m7 == "b":
        b = "X"
    if m7 == "c":
        c = "X"
    if m7 == "d":
        d = "X"
    if m7 == "e":
        e = "X"
    if m7 == "f":
        f = "X"
    if m7 == "g":
        g = "X"
    if m7 == "h":
        h = "X"
    if m7 == "i":
        i = "X"

    print("move 8")
    m8 = input()
    if m8 == "a":
        a = "O"
    if m8 == "b":
        b = "O"
    if m8 == "c":
        c = "O"
    if m8 == "d":
        d = "O"
    if m8 == "e":
        e = "O"
    if m8 == "f":
        f = "O"
    if m8 == "g":
        g = "O"
    if m8 == "h":
        h = "O"
    if m8 == "i":
        i = "O"

    print("move 9")
    m9 = input()
    if m9 == "a":
        a = "X"
    if m9 == "b":
        b = "X"
    if m9 == "c":
        c = "X"
    if m9 == "d":
        d = "X"
    if m9 == "e":
        e = "X"
    if m9 == "f":
        f = "X"
    if m9 == "g":
        g = "X"
    if m9 == "h":
        h = "X"
    if m9 == "i":
        i = "X"

    # Displays final board
    print("|---|---|---|")
    print("|", a, "|", b, "|", c, "|")
    print("|---|---|---|")
    print("|", d, "|", e, "|", f, "|")
    print("|---|---|---|")
    print("|", g, "|", h, "|", i, "|")
    print("|---|---|---|")

    # Determines if X or O wins
    if a == "X" and b == "X" and c == "X":
        print("X wins")
    if a == "O" and b == "O" and c == "O":
        print("O wins")
    if a == "X" and d == "X" and g == "X":
        print("X wins")
    if a == "O" and d == "O" and g == "O":
        print("O wins")
    if c == "X" and f == "X" and i == "X":
        print("X wins")
    if c == "O" and f == "O" and i == "O":
        print("O wins")
    if g == "X" and h == "X" and i == "X":
        print("X wins")
    if g == "O" and h == "O" and i == "O":
        print("O wins")
    if a == "X" and e == "X" and i == "X":
        print("X wins")
    if a == "O" and e == "O" and i == "O":
        print("O wins")
    if g == "X" and e == "X" and c == "X":
        print("X wins")
    if g == "O" and e == "O" and c == "O":
        print("O wins")
    if d == "X" and e == "X" and f == "X":
        print("X wins")
    if d == "O" and e == "O" and f == "O":
        print("O wins")
    if b == "X" and e == "X" and h == "X":
        print("X wins")
    if b == "O" and e == "O" and h == "O":
        print("O wins")
def myClick2():
    print("|---|---|---|---|---|")
    print("| a | b | c | d | e |")
    print("|---|---|---|---|---|")
    print("| f | g | h | i | j |")
    print("|---|---|---|---|---|")
    print("| k | l | m | n | o |")
    print("|---|---|---|---|---|")
    print("| p | q | r | s | t |")
    print("|---|---|---|---|---|")
    print("| u | v | w | x | y |")
    print("|---|---|---|---|---|")
    root.destroy()
    # Determines players moves
    print("move 1")
    m1 = input()
    if m1 == "a":
        a = "X"
    if m1 == "b":
        b = "X"
    if m1 == "c":
        c = "X"
    if m1 == "d":
        d = "X"
    if m1 == "e":
        e = "X"
    if m1 == "f":
        f = "X"
    if m1 == "g":
        g = "X"
    if m1 == "h":
        h = "X"
    if m1 == "i":
        i = "X"
    if m1 == "j":
        j = "X"
    if m1 == "k":
        k = "X"
    if m1 == "l":
        l = "X"
    if m1 == "n":
        n = "X"
    if m1 == "o":
        o = "X"
    if m1 == "p":
        p = "X"
    if m1 == "q":
        q == "X"
    if m1 == "r":
        r = "X"
    if m1 == "s":
        s = "X"
    if m1 == "t":
        t = "X"
    if m1 == "u":
        u = "X"
    if m1 == "v":
        v = "X"
    if m1 == "w":
        w = "X"
    if m1 == "x":
        x = "X"
    if m1 == "y":
        y = "X"

    print("move 2")
    m2 = input()
    if m2 == "a":
        a = "O"
    if m2 == "b":
        b = "O"
    if m2 == "c":
        c = "O"
    if m2 == "d":
        d = "O"
    if m2 == "e":
        e = "O"
    if m2 == "f":
        f = "O"
    if m2 == "g":
        g = "O"
    if m2 == "h":
        h = "O"
    if m2 == "i":
        i = "O"
    if m2 == "j":
        j = "X"
    if m2 == "k":
        k = "X"
    if m2 == "l":
        l = "X"
    if m2 == "n":
        n = "X"
    if m2 == "o":
        o = "X"
    if m2 == "p":
        p = "X"
    if m2 == "q":
        q == X
    if m2 == "r":
        r = "X"
    if m2 == "s":
        s = "X"
    if m2 == "t":
        t = "X"
    if m2 == "u":
        u = "X"
    if m2 == "v":
        v = "X"
    if m2 == "w":
        w = "X"
    if m2 == "x":
        x = "X"
    if m2 == "y":
        y = "X"

    print("move 3")
    m3 = input()
    if m3 == "a":
        a = "X"
    if m3 == "b":
        b = "X"
    if m3 == "c":
        c = "X"
    if m3 == "d":
        d = "X"
    if m3 == "e":
        e = "X"
    if m3 == "f":
        f = "X"
    if m3 == "g":
        g = "X"
    if m3 == "h":
        h = "X"
    if m3 == "i":
        i = "X"
    if m3 == "j":
        j = "X"
    if m3 == "k":
        k = "X"
    if m3 == "l":
        l = "X"
    if m3 == "n":
        n = "X"
    if m3 == "o":
        o = "X"
    if m3 == "p":
        p = "X"
    if m3 == "q":
        q == X
    if m3 == "r":
        r = "X"
    if m3 == "s":
        s = "X"
    if m3 == "t":
        t = "X"
    if m3 == "u":
        u = "X"
    if m3 == "v":
        v = "X"
    if m3 == "w":
        w = "X"
    if m3 == "x":
        x = "X"
    if m3 == "y":
        y = "X"

    print("move 4")
    m4 = input()
    if m4 == "a":
        a = "O"
    if m4 == "b":
        b = "O"
    if m4 == "c":
        c = "O"
    if m4 == "d":
        d = "O"
    if m4 == "e":
        e = "O"
    if m4 == "f":
        f = "O"
    if m4 == "g":
        g = "O"
    if m4 == "h":
        h = "O"
    if m4 == "i":
        i = "O"

    print("move 5")
    m5 = input()
    if m5 == "a":
        a = "X"
    if m5 == "b":
        b = "X"
    if m5 == "c":
        c = "X"
    if m5 == "d":
        d = "X"
    if m5 == "e":
        e = "X"
    if m5 == "f":
        f = "X"
    if m5 == "g":
        g = "X"
    if m5 == "h":
        h = "X"
    if m5 == "i":
        i = "X"

    print("move 6")
    m6 = input()
    if m6 == "a":
        a = "O"
    if m6 == "b":
        b = "O"
    if m6 == "c":
        c = "O"
    if m6 == "d":
        d = "O"
    if m6 == "e":
        e = "O"
    if m6 == "f":
        f = "O"
    if m6 == "g":
        g = "O"
    if m6 == "h":
        h = "O"
    if m6 == "i":
        i = "O"

    print("move 7")
    m7 = input()
    if m7 == "a":
        a = "X"
    if m7 == "b":
        b = "X"
    if m7 == "c":
        c = "X"
    if m7 == "d":
        d = "X"
    if m7 == "e":
        e = "X"
    if m7 == "f":
        f = "X"
    if m7 == "g":
        g = "X"
    if m7 == "h":
        h = "X"
    if m7 == "i":
        i = "X"

    print("move 8")
    m8 = input()
    if m8 == "a":
        a = "O"
    if m8 == "b":
        b = "O"
    if m8 == "c":
        c = "O"
    if m8 == "d":
        d = "O"
    if m8 == "e":
        e = "O"
    if m8 == "f":
        f = "O"
    if m8 == "g":
        g = "O"
    if m8 == "h":
        h = "O"
    if m8 == "i":
        i = "O"

    print("move 9")
    m9 = input()
    if m9 == "a":
        a = "X"
    if m9 == "b":
        b = "X"
    if m9 == "c":
        c = "X"
    if m9 == "d":
        d = "X"
    if m9 == "e":
        e = "X"
    if m9 == "f":
        f = "X"
    if m9 == "g":
        g = "X"
    if m9 == "h":
        h = "X"
    if m9 == "i":
        i = "X"

    # Displays final board
    print("|---|---|---|")
    print("|", a, "|", b, "|", c, "|")
    print("|---|---|---|")
    print("|", d, "|", e, "|", f, "|")
    print("|---|---|---|")
    print("|", g, "|", h, "|", i, "|")
    print("|---|---|---|")

    # Determines if X or O wins
    if a == "X" and b == "X" and c == "X":
        print("X wins")
    if a == "O" and b == "O" and c == "O":
        print("O wins")
    if a == "X" and d == "X" and g == "X":
        print("X wins")
    if a == "O" and d == "O" and g == "O":
        print("O wins")
    if c == "X" and f == "X" and i == "X":
        print("X wins")
    if c == "O" and f == "O" and i == "O":
        print("O wins")
    if g == "X" and h == "X" and i == "X":
        print("X wins")
    if g == "O" and h == "O" and i == "O":
        print("O wins")
    if a == "X" and e == "X" and i == "X":
        print("X wins")
    if a == "O" and e == "O" and i == "O":
        print("O wins")
    if g == "X" and e == "X" and c == "X":
        print("X wins")
    if g == "O" and e == "O" and c == "O":
        print("O wins")
    if d == "X" and e == "X" and f == "X":
        print("X wins")
    if d == "O" and e == "O" and f == "O":
        print("O wins")
    if b == "X" and e == "X" and h == "X":
        print("X wins")
    if b == "O" and e == "O" and h == "O":
        print("O wins")
def myClick3():
    print("|---|---|---|---|---|---|---|")
    print("| a | b | c | d | e | f | g |")
    print("|---|---|---|---|---|---|---|")
    print("| h | i | j | k | l | m | n |")
    print("|---|---|---|---|---|---|---|")
    print("| o | p | q | r | s | t | u |")
    print("|---|---|---|---|---|---|---|")
    print("| v | w | x | y | z |aa |ab |")
    print("|---|---|---|---|---|---|---|")
    print("|ac |ad |ae |af |ag |ah |ai |")
    print("|---|---|---|---|---|---|---|")
    print("|aj |ak |al |am |an |ao |ap |")
    print("|---|---|---|---|---|---|---|")
    print("|aq |ar |as |at |au |av |aw |")
    print("|---|---|---|---|---|---|---|")
    root.destroy()

myButton1 = Button(root, text="3x3", command=myClick1, fg="white", bg="black", padx=50, pady=3)
myButton1.pack()

myButton2 = Button(root, text="5x5", command=myClick2, fg="white", bg="black", padx=50, pady=3)
myButton2.pack()

myButton3 = Button(root, text="7x7", command=myClick3, fg="white", bg="black", padx=50, pady=3)
myButton3.pack()

root.mainloop()