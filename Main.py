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
    if m1 == "m":
        m = "X"
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
    if m2 == "m"
        m = "X"
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
    if m3 == "m":
        m = "X"
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
    if m4 == "j":
        j = "X"
    if m4 == "k":
        k = "X"
    if m4 == "l":
        l = "X"
    if m4 == "m":
        m = "X"
    if m4 == "n":
        n = "X"
    if m4 == "o":
        o = "X"
    if m4 == "p":
        p = "X"
    if m4 == "q":
        q == "X"
    if m4 == "r":
        r = "X"
    if m4 == "s":
        s = "X"
    if m4 == "t":
        t = "X"
    if m4 == "u":
        u = "X"
    if m4 == "v":
        v = "X"
    if m4 == "w":
        w = "X"
    if m4 == "x":
        x = "X"
    if m4 == "y":
        y = "X"

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
    if m5 == "j":
        j = "X"
    if m5 == "k":
        k = "X"
    if m5 == "l":
        l = "X"
    if m5 == "m":
        m = "X"
    if m5 == "n":
        n = "X"
    if m5 == "o":
        o = "X"
    if m5 == "p":
        p = "X"
    if m5 == "q":
        q == "X"
    if m5 == "r":
        r = "X"
    if m5 == "s":
        s = "X"
    if m5 == "t":
        t = "X"
    if m5 == "u":
        u = "X"
    if m5 == "v":
        v = "X"
    if m5 == "w":
        w = "X"
    if m5 == "x":
        x = "X"
    if m5 == "y":
        y = "X"

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
    if m6 == "j":
        j = "X"
    if m6 == "k":
        k = "X"
    if m6 == "l":
        l = "X"
    if m6 == "m":
        m = "X"
    if m6 == "n":
        n = "X"
    if m6 == "o":
        o = "X"
    if m6 == "p":
        p = "X"
    if m6 == "q":
        q == "X"
    if m6 == "r":
        r = "X"
    if m6 == "s":
        s = "X"
    if m6 == "t":
        t = "X"
    if m6 == "u":
        u = "X"
    if m6 == "v":
        v = "X"
    if m6 == "w":
        w = "X"
    if m6 == "x":
        x = "X"
    if m6 == "y":
        y = "X"

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
    if m7 == "j":
        j = "X"
    if m7 == "k":
        k = "X"
    if m7 == "l":
        l = "X"
    if m7 == "m":
        m = "X"
    if m7 == "n":
        n = "X"
    if m7 == "o":
        o = "X"
    if m7 == "p":
        p = "X"
    if m7 == "q":
        q == "X"
    if m7 == "r":
        r = "X"
    if m7 == "s":
        s = "X"
    if m7 == "t":
        t = "X"
    if m7 == "u":
        u = "X"
    if m7 == "v":
        v = "X"
    if m7 == "w":
        w = "X"
    if m7 == "x":
        x = "X"
    if m7 == "y":
        y = "X"

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
    if m8 == "j":
        j = "X"
    if m8 == "k":
        k = "X"
    if m8 == "l":
        l = "X"
    if m8 == "m":
        m = "X"
    if m8 == "n":
        n = "X"
    if m8 == "o":
        o = "X"
    if m8 == "p":
        p = "X"
    if m8 == "q":
        q == "X"
    if m8 == "r":
        r = "X"
    if m8 == "s":
        s = "X"
    if m8 == "t":
        t = "X"
    if m8 == "u":
        u = "X"
    if m8 == "v":
        v = "X"
    if m8 == "w":
        w = "X"
    if m8 == "x":
        x = "X"
    if m8 == "y":
        y = "X"

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
    if m9 == "j":
        j = "X"
    if m9 == "k":
        k = "X"
    if m9 == "l":
        l = "X"
    if m9 == "m":
        m = "X"
    if m9 == "n":
        n = "X"
    if m9 == "o":
        o = "X"
    if m9 == "p":
        p = "X"
    if m9 == "q":
        q == "X"
    if m9 == "r":
        r = "X"
    if m9 == "s":
        s = "X"
    if m9 == "t":
        t = "X"
    if m9 == "u":
        u = "X"
    if m9 == "v":
        v = "X"
    if m9 == "w":
        w = "X"
    if m9 == "x":
        x = "X"
    if m9 == "y":
        y = "X"

    print("move 10")
    m10 = input()
    if m10 == "a":
        a = "X"
    if m10 == "b":
        b = "X"
    if m10 == "c":
        c = "X"
    if m10 == "d":
        d = "X"
    if m10 == "e":
        e = "X"
    if m10 == "f":
        f = "X"
    if m10 == "g":
        g = "X"
    if m10 == "h":
        h = "X"
    if m10 == "i":
        i = "X"
    if m10 == "j":
        j = "X"
    if m10 == "k":
        k = "X"
    if m10 == "l":
        l = "X"
    if m10 == "m":
        m = "X"
    if m10 == "n":
        n = "X"
    if m10 == "o":
        o = "X"
    if m10 == "p":
        p = "X"
    if m10 == "q":
        q == "X"
    if m10 == "r":
        r = "X"
    if m10 == "s":
        s = "X"
    if m10 == "t":
        t = "X"
    if m10 == "u":
        u = "X"
    if m10 == "v":
        v = "X"
    if m10 == "w":
        w = "X"
    if m10 == "x":
        x = "X"
    if m10 == "y":
        y = "X"

    print("move 11")
    m11 = input()
    if m11 == "a":
        a = "X"
    if m11 == "b":
        b = "X"
    if m11 == "c":
        c = "X"
    if m11 == "d":
        d = "X"
    if m11 == "e":
        e = "X"
    if m11 == "f":
        f = "X"
    if m11 == "g":
        g = "X"
    if m11 == "h":
        h = "X"
    if m11 == "i":
        i = "X"
    if m11 == "j":
        j = "X"
    if m11 == "k":
        k = "X"
    if m11 == "l":
        l = "X"
    if m11 == "m":
        m = "X"
    if m11 == "n":
        n = "X"
    if m11 == "o":
        o = "X"
    if m11 == "p":
        p = "X"
    if m11 == "q":
        q == "X"
    if m11 == "r":
        r = "X"
    if m11 == "s":
        s = "X"
    if m11 == "t":
        t = "X"
    if m11 == "u":
        u = "X"
    if m11 == "v":
        v = "X"
    if m11 == "w":
        w = "X"
    if m11 == "x":
        x = "X"
    if m11 == "y":
        y = "X"

    print("move 12")
    m12 = input()
    if m12 == "a":
        a = "X"
    if m12 == "b":
        b = "X"
    if m12 == "c":
        c = "X"
    if m12 == "d":
        d = "X"
    if m12 == "e":
        e = "X"
    if m12 == "f":
        f = "X"
    if m12 == "g":
        g = "X"
    if m12 == "h":
        h = "X"
    if m12 == "i":
        i = "X"
    if m12 == "j":
        j = "X"
    if m12 == "k":
        k = "X"
    if m12 == "l":
        l = "X"
    if m12 == "m":
        m = "X"
    if m12 == "n":
        n = "X"
    if m12 == "o":
        o = "X"
    if m12 == "p":
        p = "X"
    if m12 == "q":
        q == "X"
    if m12 == "r":
        r = "X"
    if m12 == "s":
        s = "X"
    if m12 == "t":
        t = "X"
    if m12 == "u":
        u = "X"
    if m12 == "v":
        v = "X"
    if m12 == "w":
        w = "X"
    if m12 == "x":
        x = "X"
    if m12 == "y":
        y = "X"

    print("move 13")
    m13 = input()
    if m13 == "a":
        a = "X"
    if m13 == "b":
        b = "X"
    if m13 == "c":
        c = "X"
    if m13 == "d":
        d = "X"
    if m13 == "e":
        e = "X"
    if m13 == "f":
        f = "X"
    if m13 == "g":
        g = "X"
    if m13 == "h":
        h = "X"
    if m13 == "i":
        i = "X"
    if m13 == "j":
        j = "X"
    if m13 == "k":
        k = "X"
    if m13 == "l":
        l = "X"
    if m13 == "m":
        m = "X"
    if m13 == "n":
        n = "X"
    if m13 == "o":
        o = "X"
    if m13 == "p":
        p = "X"
    if m13 == "q":
        q == "X"
    if m13 == "r":
        r = "X"
    if m13 == "s":
        s = "X"
    if m13 == "t":
        t = "X"
    if m13 == "u":
        u = "X"
    if m13 == "v":
        v = "X"
    if m13 == "w":
        w = "X"
    if m13 == "x":
        x = "X"
    if m13 == "y":
        y = "X"

    print("move 14")
    m14 = input()
    if m14 == "a":
        a = "X"
    if m14 == "b":
        b = "X"
    if m14 == "c":
        c = "X"
    if m14 == "d":
        d = "X"
    if m14 == "e":
        e = "X"
    if m14 == "f":
        f = "X"
    if m14 == "g":
        g = "X"
    if m14 == "h":
        h = "X"
    if m14 == "i":
        i = "X"
    if m14 == "j":
        j = "X"
    if m14 == "k":
        k = "X"
    if m14 == "l":
        l = "X"
    if m14 == "m":
        m = "X"
    if m14 == "n":
        n = "X"
    if m14 == "o":
        o = "X"
    if m14 == "p":
        p = "X"
    if m14 == "q":
        q == "X"
    if m14 == "r":
        r = "X"
    if m14 == "s":
        s = "X"
    if m14 == "t":
        t = "X"
    if m14 == "u":
        u = "X"
    if m14 == "v":
        v = "X"
    if m14 == "w":
        w = "X"
    if m14 == "x":
        x = "X"
    if m14 == "y":
        y = "X"

    print("move 15")
    m15 = input()
    if m15 == "a":
        a = "X"
    if m15 == "b":
        b = "X"
    if m15 == "c":
        c = "X"
    if m15 == "d":
        d = "X"
    if m15 == "e":
        e = "X"
    if m15 == "f":
        f = "X"
    if m15 == "g":
        g = "X"
    if m15 == "h":
        h = "X"
    if m15 == "i":
        i = "X"
    if m15 == "j":
        j = "X"
    if m15 == "k":
        k = "X"
    if m15 == "l":
        l = "X"
    if m15 == "m":
        m = "X"
    if m15 == "n":
        n = "X"
    if m15 == "o":
        o = "X"
    if m15 == "p":
        p = "X"
    if m15 == "q":
        q == "X"
    if m15 == "r":
        r = "X"
    if m15 == "s":
        s = "X"
    if m15 == "t":
        t = "X"
    if m15 == "u":
        u = "X"
    if m15 == "v":
        v = "X"
    if m15 == "w":
        w = "X"
    if m15 == "x":
        x = "X"
    if m15 == "y":
        y = "X"

    print("move 16")
    m16 = input()
    if m16 == "a":
        a = "X"
    if m16 == "b":
        b = "X"
    if m16 == "c":
        c = "X"
    if m16 == "d":
        d = "X"
    if m16 == "e":
        e = "X"
    if m16 == "f":
        f = "X"
    if m16 == "g":
        g = "X"
    if m16 == "h":
        h = "X"
    if m16 == "i":
        i = "X"
    if m16 == "j":
        j = "X"
    if m16 == "k":
        k = "X"
    if m16 == "l":
        l = "X"
    if m16 == "m":
        m = "X"
    if m16 == "n":
        n = "X"
    if m16 == "o":
        o = "X"
    if m16 == "p":
        p = "X"
    if m16 == "q":
        q == "X"
    if m16 == "r":
        r = "X"
    if m16 == "s":
        s = "X"
    if m16 == "t":
        t = "X"
    if m16 == "u":
        u = "X"
    if m16 == "v":
        v = "X"
    if m16 == "w":
        w = "X"
    if m16 == "x":
        x = "X"
    if m16 == "y":
        y = "X"

    print("move 17")
    m17 = input()
    if m17 == "a":
        a = "X"
    if m17 == "b":
        b = "X"
    if m17 == "c":
        c = "X"
    if m17 == "d":
        d = "X"
    if m17 == "e":
        e = "X"
    if m17 == "f":
        f = "X"
    if m17 == "g":
        g = "X"
    if m17 == "h":
        h = "X"
    if m17 == "i":
        i = "X"
    if m17 == "j":
        j = "X"
    if m17 == "k":
        k = "X"
    if m17 == "l":
        l = "X"
    if m17 == "m":
        m = "X"
    if m17 == "n":
        n = "X"
    if m17 == "o":
        o = "X"
    if m17 == "p":
        p = "X"
    if m17 == "q":
        q == "X"
    if m17 == "r":
        r = "X"
    if m17 == "s":
        s = "X"
    if m17 == "t":
        t = "X"
    if m17 == "u":
        u = "X"
    if m17 == "v":
        v = "X"
    if m17 == "w":
        w = "X"
    if m17 == "x":
        x = "X"
    if m17 == "y":
        y = "X"

    print("move 18")
    m18 = input()
    if m18 == "a":
        a = "X"
    if m18 == "b":
        b = "X"
    if m18 == "c":
        c = "X"
    if m18 == "d":
        d = "X"
    if m18 == "e":
        e = "X"
    if m18 == "f":
        f = "X"
    if m18 == "g":
        g = "X"
    if m18 == "h":
        h = "X"
    if m18 == "i":
        i = "X"
    if m18 == "j":
        j = "X"
    if m18 == "k":
        k = "X"
    if m18 == "l":
        l = "X"
    if m18 == "m":
        m = "X"
    if m18 == "n":
        n = "X"
    if m18 == "o":
        o = "X"
    if m18 == "p":
        p = "X"
    if m18 == "q":
        q == "X"
    if m18 == "r":
        r = "X"
    if m18 == "s":
        s = "X"
    if m18 == "t":
        t = "X"
    if m18 == "u":
        u = "X"
    if m18 == "v":
        v = "X"
    if m18 == "w":
        w = "X"
    if m18 == "x":
        x = "X"
    if m18 == "y":
        y = "X"

    print("move 19")
    m19 = input()
    if m19 == "a":
        a = "X"
    if m19 == "b":
        b = "X"
    if m19 == "c":
        c = "X"
    if m19 == "d":
        d = "X"
    if m19 == "e":
        e = "X"
    if m19 == "f":
        f = "X"
    if m19 == "g":
        g = "X"
    if m19 == "h":
        h = "X"
    if m19 == "i":
        i = "X"
    if m19 == "j":
        j = "X"
    if m19 == "k":
        k = "X"
    if m19 == "l":
        l = "X"
    if m19 == "m":
        m = "X"
    if m19 == "n":
        n = "X"
    if m19 == "o":
        o = "X"
    if m19 == "p":
        p = "X"
    if m19 == "q":
        q == "X"
    if m19 == "r":
        r = "X"
    if m19 == "s":
        s = "X"
    if m19 == "t":
        t = "X"
    if m19 == "u":
        u = "X"
    if m19 == "v":
        v = "X"
    if m19 == "w":
        w = "X"
    if m19 == "x":
        x = "X"
    if m19 == "y":
        y = "X"

    print("move 20")
    m20 = input()
    if m20 == "a":
        a = "X"
    if m20 == "b":
        b = "X"
    if m20 == "c":
        c = "X"
    if m20 == "d":
        d = "X"
    if m20 == "e":
        e = "X"
    if m20 == "f":
        f = "X"
    if m20 == "g":
        g = "X"
    if m20 == "h":
        h = "X"
    if m20 == "i":
        i = "X"
    if m20 == "j":
        j = "X"
    if m20 == "k":
        k = "X"
    if m20 == "l":
        l = "X"
    if m20 == "m":
        m = "X"
    if m20 == "n":
        n = "X"
    if m20 == "o":
        o = "X"
    if m20 == "p":
        p = "X"
    if m20 == "q":
        q == "X"
    if m20 == "r":
        r = "X"
    if m20 == "s":
        s = "X"
    if m20 == "t":
        t = "X"
    if m20 == "u":
        u = "X"
    if m20 == "v":
        v = "X"
    if m20 == "w":
        w = "X"
    if m20 == "x":
        x = "X"
    if m20 == "y":
        y = "X"

    print("move 21")
    m21 = input()
    if m21 == "a":
        a = "X"
    if m21 == "b":
        b = "X"
    if m21 == "c":
        c = "X"
    if m21 == "d":
        d = "X"
    if m21 == "e":
        e = "X"
    if m21 == "f":
        f = "X"
    if m21 == "g":
        g = "X"
    if m21 == "h":
        h = "X"
    if m21 == "i":
        i = "X"
    if m21 == "j":
        j = "X"
    if m21 == "k":
        k = "X"
    if m21 == "l":
        l = "X"
    if m21 == "m":
        m = "X"
    if m21 == "n":
        n = "X"
    if m21 == "o":
        o = "X"
    if m21 == "p":
        p = "X"
    if m21 == "q":
        q == "X"
    if m21 == "r":
        r = "X"
    if m21 == "s":
        s = "X"
    if m21 == "t":
        t = "X"
    if m21 == "u":
        u = "X"
    if m21 == "v":
        v = "X"
    if m21 == "w":
        w = "X"
    if m21 == "x":
        x = "X"
    if m21 == "y":
        y = "X"

    print("move 22")
    m22 = input()
    if m22 == "a":
        a = "X"
    if m22 == "b":
        b = "X"
    if m22 == "c":
        c = "X"
    if m22 == "d":
        d = "X"
    if m22 == "e":
        e = "X"
    if m22 == "f":
        f = "X"
    if m22 == "g":
        g = "X"
    if m22 == "h":
        h = "X"
    if m22 == "i":
        i = "X"
    if m22 == "j":
        j = "X"
    if m22 == "k":
        k = "X"
    if m22 == "l":
        l = "X"
    if m22 == "m":
        m = "X"
    if m22 == "n":
        n = "X"
    if m22 == "o":
        o = "X"
    if m22 == "p":
        p = "X"
    if m22 == "q":
        q == "X"
    if m22 == "r":
        r = "X"
    if m22 == "s":
        s = "X"
    if m22 == "t":
        t = "X"
    if m22 == "u":
        u = "X"
    if m22 == "v":
        v = "X"
    if m22 == "w":
        w = "X"
    if m22 == "x":
        x = "X"
    if m22 == "y":
        y = "X"

    print("move 23")
    m23 = input()
    if m23 == "a":
        a = "X"
    if m23 == "b":
        b = "X"
    if m23 == "c":
        c = "X"
    if m23 == "d":
        d = "X"
    if m23 == "e":
        e = "X"
    if m23 == "f":
        f = "X"
    if m23 == "g":
        g = "X"
    if m23 == "h":
        h = "X"
    if m23 == "i":
        i = "X"
    if m23 == "j":
        j = "X"
    if m23 == "k":
        k = "X"
    if m23 == "l":
        l = "X"
    if m23 == "m":
        m = "X"
    if m23 == "n":
        n = "X"
    if m23 == "o":
        o = "X"
    if m23 == "p":
        p = "X"
    if m23 == "q":
        q == "X"
    if m23 == "r":
        r = "X"
    if m23 == "s":
        s = "X"
    if m23 == "t":
        t = "X"
    if m23 == "u":
        u = "X"
    if m23 == "v":
        v = "X"
    if m23 == "w":
        w = "X"
    if m23 == "x":
        x = "X"
    if m23 == "y":
        y = "X"

    print("move 24")
    m24 = input()
    if m24 == "a":
        a = "X"
    if m24 == "b":
        b = "X"
    if m24 == "c":
        c = "X"
    if m24 == "d":
        d = "X"
    if m24 == "e":
        e = "X"
    if m24 == "f":
        f = "X"
    if m24 == "g":
        g = "X"
    if m24 == "h":
        h = "X"
    if m24 == "i":
        i = "X"
    if m24 == "j":
        j = "X"
    if m24 == "k":
        k = "X"
    if m24 == "l":
        l = "X"
    if m24 == "m":
        m = "X"
    if m24 == "n":
        n = "X"
    if m24 == "o":
        o= "X"
    if m24 == "p":
        p = "X"
    if m24 == "q":
        q == "X"
    if m24 == "r":
        r = "X"
    if m24 == "s":
        s = "X"
    if m24 == "t":
        t = "X"
    if m24 == "u":
        u = "X"
    if m24 == "v":
        v = "X"
    if m24 == "w":
        w = "X"
    if m24 == "x":
        x = "X"
    if m24 == "y":
        y = "X"

    print("move 25")
    m25 = input()
    if m25 == "a":
        a = "X"
    if m25 == "b":
        b = "X"
    if m25 == "c":
        c = "X"
    if m25 == "d":
        d = "X"
    if m25 == "e":
        e = "X"
    if m25 == "f":
        f = "X"
    if m25 == "g":
        g = "X"
    if m25 == "h":
        h = "X"
    if m25 == "i":
        i = "X"
    if m25 == "j":
        j = "X"
    if m25 == "k":
        k = "X"
    if m25 == "l":
        l = "X"
    if m25 == "m":
        m = "X"
    if m25 == "n":
        n = "X"
    if m25 == "o":
        o = "X"
    if m25 == "p":
        p = "X"
    if m25 == "q":
        q == "X"
    if m25 == "r":
        r = "X"
    if m25 == "s":
        s = "X"
    if m25 == "t":
        t = "X"
    if m25 == "u":
        u = "X"
    if m25 == "v":
        v = "X"
    if m25 == "w":
        w = "X"
    if m25 == "x":
        x = "X"
    if m25 == "y":
        y = "X"

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