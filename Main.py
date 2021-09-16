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
        q = "X"
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
        j = "O"
    if m2 == "k":
        k = "O"
    if m2 == "l":
        l = "O"
    if m2 == "m":
        m = "O"
    if m2 == "n":
        n = "O"
    if m2 == "o":
        o = "O"
    if m2 == "p":
        p = "O"
    if m2 == "q":
        q = "O"
    if m2 == "r":
        r = "O"
    if m2 == "s":
        s = "O"
    if m2 == "t":
        t = "O"
    if m2 == "u":
        u = "O"
    if m2 == "v":
        v = "O"
    if m2 == "w":
        w = "O"
    if m2 == "x":
        x = "O"
    if m2 == "y":
        y = "O"

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
        q = "X"
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
        j = "O"
    if m4 == "k":
        k = "O"
    if m4 == "l":
        l = "O"
    if m4 == "m":
        m = "O"
    if m4 == "n":
        n = "O"
    if m4 == "o":
        o = "O"
    if m4 == "p":
        p = "O"
    if m4 == "q":
        q = "O"
    if m4 == "r":
        r = "O"
    if m4 == "s":
        s = "O"
    if m4 == "t":
        t = "O"
    if m4 == "u":
        u = "O"
    if m4 == "v":
        v = "O"
    if m4 == "w":
        w = "O"
    if m4 == "x":
        x = "O"
    if m4 == "y":
        y = "O"

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
        q = "X"
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
        j = "O"
    if m6 == "k":
        k = "O"
    if m6 == "l":
        l = "O"
    if m6 == "m":
        m = "O"
    if m6 == "n":
        n = "O"
    if m6 == "o":
        o = "O"
    if m6 == "p":
        p = "O"
    if m6 == "q":
        q = "O"
    if m6 == "r":
        r = "O"
    if m6 == "s":
        s = "O"
    if m6 == "t":
        t = "O"
    if m6 == "u":
        u = "O"
    if m6 == "v":
        v = "O"
    if m6 == "w":
        w = "O"
    if m6 == "x":
        x = "O"
    if m6 == "y":
        y = "O"

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
        q = "X"
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
        j = "O"
    if m8 == "k":
        k = "O"
    if m8 == "l":
        l = "O"
    if m8 == "m":
        m = "O"
    if m8 == "n":
        n = "O"
    if m8 == "o":
        o = "O"
    if m8 == "p":
        p = "O"
    if m8 == "q":
        q = "O"
    if m8 == "r":
        r = "O"
    if m8 == "s":
        s = "O"
    if m8 == "t":
        t = "O"
    if m8 == "u":
        u = "O"
    if m8 == "v":
        v = "O"
    if m8 == "w":
        w = "O"
    if m8 == "x":
        x = "O"
    if m8 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m10 == "b":
        b = "O"
    if m10 == "c":
        c = "O"
    if m10 == "d":
        d = "O"
    if m10 == "e":
        e = "O"
    if m10 == "f":
        f = "O"
    if m10 == "g":
        g = "O"
    if m10 == "h":
        h = "O"
    if m10 == "i":
        i = "O"
    if m10 == "j":
        j = "O"
    if m10 == "k":
        k = "O"
    if m10 == "l":
        l = "O"
    if m10 == "m":
        m = "O"
    if m10 == "n":
        n = "O"
    if m10 == "o":
        o = "O"
    if m10 == "p":
        p = "O"
    if m10 == "q":
        q = "O"
    if m10 == "r":
        r = "O"
    if m10 == "s":
        s = "O"
    if m10 == "t":
        t = "O"
    if m10 == "u":
        u = "O"
    if m10 == "v":
        v = "O"
    if m10 == "w":
        w = "O"
    if m10 == "x":
        x = "O"
    if m10 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m12 == "b":
        b = "O"
    if m12 == "c":
        c = "O"
    if m12 == "d":
        d = "O"
    if m12 == "e":
        e = "O"
    if m12 == "f":
        f = "O"
    if m12 == "g":
        g = "O"
    if m12 == "h":
        h = "O"
    if m12 == "i":
        i = "O"
    if m12 == "j":
        j = "O"
    if m12 == "k":
        k = "O"
    if m12 == "l":
        l = "O"
    if m12 == "m":
        m = "O"
    if m12 == "n":
        n = "O"
    if m12 == "o":
        o = "O"
    if m12 == "p":
        p = "O"
    if m12 == "q":
        q = "O"
    if m12 == "r":
        r = "O"
    if m12 == "s":
        s = "O"
    if m12 == "t":
        t = "O"
    if m12 == "u":
        u = "O"
    if m12 == "v":
        v = "O"
    if m12 == "w":
        w = "O"
    if m12 == "x":
        x = "O"
    if m12 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m14 == "b":
        b = "O"
    if m14 == "c":
        c = "O"
    if m14 == "d":
        d = "O"
    if m14 == "e":
        e = "O"
    if m14 == "f":
        f = "O"
    if m14 == "g":
        g = "O"
    if m14 == "h":
        h = "O"
    if m14 == "i":
        i = "O"
    if m14 == "j":
        j = "O"
    if m14 == "k":
        k = "O"
    if m14 == "l":
        l = "O"
    if m14 == "m":
        m = "O"
    if m14 == "n":
        n = "O"
    if m14 == "o":
        o = "O"
    if m14 == "p":
        p = "O"
    if m14 == "q":
        q = "O"
    if m14 == "r":
        r = "O"
    if m14 == "s":
        s = "O"
    if m14 == "t":
        t = "O"
    if m14 == "u":
        u = "O"
    if m14 == "v":
        v = "O"
    if m14 == "w":
        w = "O"
    if m14 == "x":
        x = "O"
    if m14 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m16 == "b":
        b = "O"
    if m16 == "c":
        c = "O"
    if m16 == "d":
        d = "O"
    if m16 == "e":
        e = "O"
    if m16 == "f":
        f = "O"
    if m16 == "g":
        g = "O"
    if m16 == "h":
        h = "O"
    if m16 == "i":
        i = "O"
    if m16 == "j":
        j = "O"
    if m16 == "k":
        k = "O"
    if m16 == "l":
        l = "O"
    if m16 == "m":
        m = "O"
    if m16 == "n":
        n = "O"
    if m16 == "o":
        o = "O"
    if m16 == "p":
        p = "O"
    if m16 == "q":
        q = "O"
    if m16 == "r":
        r = "O"
    if m16 == "s":
        s = "O"
    if m16 == "t":
        t = "O"
    if m16 == "u":
        u = "O"
    if m16 == "v":
        v = "O"
    if m16 == "w":
        w = "O"
    if m16 == "x":
        x = "O"
    if m16 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m18 == "b":
        b = "O"
    if m18 == "c":
        c = "O"
    if m18 == "d":
        d = "O"
    if m18 == "e":
        e = "O"
    if m18 == "f":
        f = "O"
    if m18 == "g":
        g = "O"
    if m18 == "h":
        h = "O"
    if m18 == "i":
        i = "O"
    if m18 == "j":
        j = "O"
    if m18 == "k":
        k = "O"
    if m18 == "l":
        l = "O"
    if m18 == "m":
        m = "O"
    if m18 == "n":
        n = "O"
    if m18 == "o":
        o = "O"
    if m18 == "p":
        p = "O"
    if m18 == "q":
        q = "O"
    if m18 == "r":
        r = "O"
    if m18 == "s":
        s = "O"
    if m18 == "t":
        t = "O"
    if m18 == "u":
        u = "O"
    if m18 == "v":
        v = "O"
    if m18 == "w":
        w = "O"
    if m18 == "x":
        x = "O"
    if m18 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m20 == "b":
        b = "O"
    if m20 == "c":
        c = "O"
    if m20 == "d":
        d = "O"
    if m20 == "e":
        e = "O"
    if m20 == "f":
        f = "O"
    if m20 == "g":
        g = "O"
    if m20 == "h":
        h = "O"
    if m20 == "i":
        i = "O"
    if m20 == "j":
        j = "O"
    if m20 == "k":
        k = "O"
    if m20 == "l":
        l = "O"
    if m20 == "m":
        m = "O"
    if m20 == "n":
        n = "O"
    if m20 == "o":
        o = "O"
    if m20 == "p":
        p = "O"
    if m20 == "q":
        q = "O"
    if m20 == "r":
        r = "O"
    if m20 == "s":
        s = "O"
    if m20 == "t":
        t = "O"
    if m20 == "u":
        u = "O"
    if m20 == "v":
        v = "O"
    if m20 == "w":
        w = "O"
    if m20 == "x":
        x = "O"
    if m20 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m22 == "b":
        b = "O"
    if m22 == "c":
        c = "O"
    if m22 == "d":
        d = "O"
    if m22 == "e":
        e = "O"
    if m22 == "f":
        f = "O"
    if m22 == "g":
        g = "O"
    if m22 == "h":
        h = "O"
    if m22 == "i":
        i = "O"
    if m22 == "j":
        j = "O"
    if m22 == "k":
        k = "O"
    if m22 == "l":
        l = "O"
    if m22 == "m":
        m = "O"
    if m22 == "n":
        n = "O"
    if m22 == "o":
        o = "O"
    if m22 == "p":
        p = "O"
    if m22 == "q":
        q = "O"
    if m22 == "r":
        r = "O"
    if m22 == "s":
        s = "O"
    if m22 == "t":
        t = "O"
    if m22 == "u":
        u = "O"
    if m22 == "v":
        v = "O"
    if m22 == "w":
        w = "O"
    if m22 == "x":
        x = "O"
    if m22 == "y":
        y = "O"

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
        q = "X"
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
        a = "O"
    if m24 == "b":
        b = "O"
    if m24 == "c":
        c = "O"
    if m24 == "d":
        d = "O"
    if m24 == "e":
        e = "O"
    if m24 == "f":
        f = "O"
    if m24 == "g":
        g = "O"
    if m24 == "h":
        h = "O"
    if m24 == "i":
        i = "O"
    if m24 == "j":
        j = "O"
    if m24 == "k":
        k = "O"
    if m24 == "l":
        l = "O"
    if m24 == "m":
        m = "O"
    if m24 == "n":
        n = "O"
    if m24 == "o":
        o = "O"
    if m24 == "p":
        p = "O"
    if m24 == "q":
        q = "O"
    if m24 == "r":
        r = "O"
    if m24 == "s":
        s = "O"
    if m24 == "t":
        t = "O"
    if m24 == "u":
        u = "O"
    if m24 == "v":
        v = "O"
    if m24 == "w":
        w = "O"
    if m24 == "x":
        x = "O"
    if m24 == "y":
        y = "O"

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
        q = "X"
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
    print("|---|---|---|---|---|")
    print("|", a, "|", b, "|", c, "|", d, "|", e, "|")
    print("|---|---|---|---|---|")
    print("|", f, "|", g, "|", h, "|", i, "|", j, "|")
    print("|---|---|---|---|---|")
    print("|", k, "|", l, "|", m, "|", n, "|", o, "|")
    print("|---|---|---|---|---|")
    print("|", p, "|", q, "|", r, "|", s, "|", t, "|")
    print("|---|---|---|---|---|")
    print("|", u, "|", v, "|", w, "|", x, "|", y, "|")

    # Determines if X or O wins
    if a == "X" and b == "X" and c == "X" and d == "X" and e == "X":
        print("X wins")
    if a == "O" and b == "O" and c == "O" and d == "O" and e == "O":
        print("O wins")
    if f == "X" and g == "X" and h == "X" and i == "X" and j == "X":
        print("X wins")
    if f == "O" and g == "O" and h == "O" and i == "O" and j == "O":
        print("O wins")
    if k == "X" and l == "X" and m == "X" and n == "X" and o == "X":
        print("X wins")
    if k == "O" and l == "O" and m == "O" and n == "O" and o == "O":
        print("O wins")
    if p == "X" and q == "X" and r == "X" and s == "X" and t == "X":
        print("X wins")
    if p == "O" and q == "O" and r == "O" and s == "O" and t == "O":
        print("O wins")
    if u == "X" and v == "X" and w == "X" and x == "X" and y == "X":
        print("X wins")
    if u == "O" and v == "O" and w == "O" and x == "O" and y == "O":
        print("O wins")
    if a == "X" and f == "X" and k == "X" and p == "X" and u == "X":
        print("X wins")
    if a == "O" and f == "O" and k == "O" and p == "O" and u == "O":
        print("O wins")
    if b == "X" and g == "X" and l == "X" and q == "X" and v == "X":
        print("X wins")
    if b == "O" and g == "O" and l == "O" and q == "O" and v == "O":
        print("O wins")
    if c == "X" and h == "X" and m == "X" and r == "X" and w == "X":
        print("X wins")
    if c == "O" and h == "O" and m == "O" and r == "O" and w == "O":
        print("O wins")
    if d == "X" and h == "X" and m == "X" and r == "X" and w == "X":
        print("X wins")
    if d == "O" and h == "O" and m == "O" and r == "O" and w == "O":
        print("O wins")
    if e == "X" and j == "X" and o == "X" and t == "X" and y == "X":
        print("X wins")
    if e == "O" and j == "O" and o == "O" and t == "O" and y == "O":
        print("O wins")
    if a == "X" and g == "X" and m == "X" and s == "X" and y == "X":
        print("X wins")
    if a == "O" and g == "O" and m == "O" and s == "O" and y == "O":
        print("O wins")
    if e == "X" and i == "X" and m == "X" and q == "X" and u == "X":
        print("X wins")
    if e == "O" and i == "O" and m == "O" and q == "O" and u == "O":
        print("O wins")

def myClick3():
    print("|---|---|---|---|---|---|---|")
    print("| a | b | c | d | e | f | g |")
    print("|---|---|---|---|---|---|---|")
    print("| h | i | j | k | l | m | n |")
    print("|---|---|---|---|---|---|---|")
    print("| o | p | q | r | s | t | u |")
    print("|---|---|---|---|---|---|---|")
    print("| v | w | x | y | z |a1 |b1 |")
    print("|---|---|---|---|---|---|---|")
    print("|c1 |d1 |e1 |f1 |g1 |h1 |i1 |")
    print("|---|---|---|---|---|---|---|")
    print("|j1 |k1 |l1 |n1 |o1 |p1 |q1 |")
    print("|---|---|---|---|---|---|---|")
    print("|r1 |s1 |t1 |u1 |v1 |w1 |x1 |")
    print("|---|---|---|---|---|---|---|")
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
        q = "X"
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
    if m1 == "z":
        z = "X"
    if m1 == "a1":
        a1 = "X"
    if m1 == "b1":
        b1 = "X"
    if m1 == "c1":
        c1 = "X"
    if m1 == "d1":
        d1 = "X"
    if m1 == "e1":
        e1 = "X"
    if m1 == "f1":
        f1 = "X"
    if m1 == "g1":
        g1 = "X"
    if m1 == "h1":
        h1 = "X"
    if m1 == "i1":
        i1 = "X"
    if m1 == "j1":
        j1 = "X"
    if m1 == "k1":
        k1 = "X"
    if m1 == "l1":
        l1 = "X"
    if m1 == "n1":
        n1 = "X"
    if m1 == "o1":
        o1 = "X"
    if m1 == "p1":
        p1 = "X"
    if m1 == "q1":
        q1 = "X"
    if m1 == "r1":
        r1 = "X"
    if m1 == "s1":
        s1 = "X"
    if m1 == "t1":
        t1 = "X"
    if m1 == "u1":
        u1 = "X"
    if m1 == "v1":
        v1 = "X"
    if m1 == "w1":
        w1 = "X"
    if m1 == "x1":
        x1 = "X"

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
        j = "O"
    if m2 == "k":
        k = "O"
    if m2 == "l":
        l = "O"
    if m2 == "m":
        m = "O"
    if m2 == "n":
        n = "O"
    if m2 == "o":
        o = "O"
    if m2 == "p":
        p = "O"
    if m2 == "q":
        q = "O"
    if m2 == "r":
        r = "O"
    if m2 == "s":
        s = "O"
    if m2 == "t":
        t = "O"
    if m2 == "u":
        u = "O"
    if m2 == "v":
        v = "O"
    if m2 == "w":
        w = "O"
    if m2 == "x":
        x = "O"
    if m2 == "y":
        y = "O"
    if m2 == "z":
        z = "O"
    if m2 == "a1":
        a1 = "O"
    if m2 == "b1":
        b1 = "O"
    if m2 == "c1":
        c1 = "O"
    if m2 == "d1":
        d1 = "O"
    if m2 == "e1":
        e1 = "O"
    if m2 == "f1":
        f1 = "O"
    if m2 == "g1":
        g1 = "O"
    if m2 == "h1":
        h1 = "O"
    if m2 == "i1":
        i1 = "O"
    if m2 == "j1":
        j1 = "O"
    if m2 == "k1":
        k1 = "O"
    if m2 == "l1":
        l1 = "O"
    if m2 == "n1":
        n1 = "O"
    if m2 == "o1":
        o1 = "O"
    if m2 == "p1":
        p1 = "O"
    if m2 == "q1":
        q1 = "O"
    if m2 == "r1":
        r1 = "O"
    if m2 == "s1":
        s1 = "O"
    if m2 == "t1":
        t1 = "O"
    if m2 == "u1":
        u1 = "O"
    if m2 == "v1":
        v1 = "O"
    if m2 == "w1":
        w1 = "O"
    if m2 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m3 == "z":
        z = "X"
    if m3 == "a1":
        a1 = "X"
    if m3 == "b1":
        b1 = "X"
    if m3 == "c1":
        c1 = "X"
    if m3 == "d1":
        d1 = "X"
    if m3 == "e1":
        e1 = "X"
    if m3 == "f1":
        f1 = "X"
    if m3 == "g1":
        g1 = "X"
    if m3 == "h1":
        h1 = "X"
    if m3 == "i1":
        i1 = "X"
    if m3 == "j1":
        j1 = "X"
    if m3 == "k1":
        k1 = "X"
    if m3 == "l1":
        l1 = "X"
    if m3 == "n1":
        n1 = "X"
    if m3 == "o1":
        o1 = "X"
    if m3 == "p1":
        p1 = "X"
    if m3 == "q1":
        q1 = "X"
    if m3 == "r1":
        r1 = "X"
    if m3 == "s1":
        s1 = "X"
    if m3 == "t1":
        t1 = "X"
    if m3 == "u1":
        u1 = "X"
    if m3 == "v1":
        v1 = "X"
    if m3 == "w1":
        w1 = "X"
    if m3 == "x1":
        x1 = "X"

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
        j = "O"
    if m4 == "k":
        k = "O"
    if m4 == "l":
        l = "O"
    if m4 == "m":
        m = "O"
    if m4 == "n":
        n = "O"
    if m4 == "o":
        o = "O"
    if m4 == "p":
        p = "O"
    if m4 == "q":
        q = "O"
    if m4 == "r":
        r = "O"
    if m4 == "s":
        s = "O"
    if m4 == "t":
        t = "O"
    if m4 == "u":
        u = "O"
    if m4 == "v":
        v = "O"
    if m4 == "w":
        w = "O"
    if m4 == "x":
        x = "O"
    if m4 == "y":
        y = "O"
    if m4 == "z":
        z = "O"
    if m4 == "a1":
        a1 = "O"
    if m4 == "b1":
        b1 = "O"
    if m4 == "c1":
        c1 = "O"
    if m4 == "d1":
        d1 = "O"
    if m4 == "e1":
        e1 = "O"
    if m4 == "f1":
        f1 = "O"
    if m4 == "g1":
        g1 = "O"
    if m4 == "h1":
        h1 = "O"
    if m4 == "i1":
        i1 = "O"
    if m4 == "j1":
        j1 = "O"
    if m4 == "k1":
        k1 = "O"
    if m4 == "l1":
        l1 = "O"
    if m4 == "n1":
        n1 = "O"
    if m4 == "o1":
        o1 = "O"
    if m4 == "p1":
        p1 = "O"
    if m4 == "q1":
        q1 = "O"
    if m4 == "r1":
        r1 = "O"
    if m4 == "s1":
        s1 = "O"
    if m4 == "t1":
        t1 = "O"
    if m4 == "u1":
        u1 = "O"
    if m4 == "v1":
        v1 = "O"
    if m4 == "w1":
        w1 = "O"
    if m4 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m5 == "z":
        z = "X"
    if m5 == "a1":
        a1 = "X"
    if m5 == "b1":
        b1 = "X"
    if m5 == "c1":
        c1 = "X"
    if m5 == "d1":
        d1 = "X"
    if m5 == "e1":
        e1 = "X"
    if m5 == "f1":
        f1 = "X"
    if m5 == "g1":
        g1 = "X"
    if m5 == "h1":
        h1 = "X"
    if m5 == "i1":
        i1 = "X"
    if m5 == "j1":
        j1 = "X"
    if m5 == "k1":
        k1 = "X"
    if m5 == "l1":
        l1 = "X"
    if m5 == "n1":
        n1 = "X"
    if m5 == "o1":
        o1 = "X"
    if m5 == "p1":
        p1 = "X"
    if m5 == "q1":
        q1 = "X"
    if m5 == "r1":
        r1 = "X"
    if m5 == "s1":
        s1 = "X"
    if m5 == "t1":
        t1 = "X"
    if m5 == "u1":
        u1 = "X"
    if m5 == "v1":
        v1 = "X"
    if m5 == "w1":
        w1 = "X"
    if m5 == "x1":
        x1 = "X"

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
        j = "O"
    if m6 == "k":
        k = "O"
    if m6 == "l":
        l = "O"
    if m6 == "m":
        m = "O"
    if m6 == "n":
        n = "O"
    if m6 == "o":
        o = "O"
    if m6 == "p":
        p = "O"
    if m6 == "q":
        q = "O"
    if m6 == "r":
        r = "O"
    if m6 == "s":
        s = "O"
    if m6 == "t":
        t = "O"
    if m6 == "u":
        u = "O"
    if m6 == "v":
        v = "O"
    if m6 == "w":
        w = "O"
    if m6 == "x":
        x = "O"
    if m6 == "y":
        y = "O"
    if m6 == "z":
        z = "O"
    if m6 == "a1":
        a1 = "O"
    if m6 == "b1":
        b1 = "O"
    if m6 == "c1":
        c1 = "O"
    if m6 == "d1":
        d1 = "O"
    if m6 == "e1":
        e1 = "O"
    if m6 == "f1":
        f1 = "O"
    if m6 == "g1":
        g1 = "O"
    if m6 == "h1":
        h1 = "O"
    if m6 == "i1":
        i1 = "O"
    if m6 == "j1":
        j1 = "O"
    if m6 == "k1":
        k1 = "O"
    if m6 == "l1":
        l1 = "O"
    if m6 == "n1":
        n1 = "O"
    if m6 == "o1":
        o1 = "O"
    if m6 == "p1":
        p1 = "O"
    if m6 == "q1":
        q1 = "O"
    if m6 == "r1":
        r1 = "O"
    if m6 == "s1":
        s1 = "O"
    if m6 == "t1":
        t1 = "O"
    if m6 == "u1":
        u1 = "O"
    if m6 == "v1":
        v1 = "O"
    if m6 == "w1":
        w1 = "O"
    if m6 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m7 == "z":
        z = "X"
    if m7 == "a1":
        a1 = "X"
    if m7 == "b1":
        b1 = "X"
    if m7 == "c1":
        c1 = "X"
    if m7 == "d1":
        d1 = "X"
    if m7 == "e1":
        e1 = "X"
    if m7 == "f1":
        f1 = "X"
    if m7 == "g1":
        g1 = "X"
    if m7 == "h1":
        h1 = "X"
    if m7 == "i1":
        i1 = "X"
    if m7 == "j1":
        j1 = "X"
    if m7 == "k1":
        k1 = "X"
    if m7 == "l1":
        l1 = "X"
    if m7 == "n1":
        n1 = "X"
    if m7 == "o1":
        o1 = "X"
    if m7 == "p1":
        p1 = "X"
    if m7 == "q1":
        q1 = "X"
    if m7 == "r1":
        r1 = "X"
    if m7 == "s1":
        s1 = "X"
    if m7 == "t1":
        t1 = "X"
    if m7 == "u1":
        u1 = "X"
    if m7 == "v1":
        v1 = "X"
    if m7 == "w1":
        w1 = "X"
    if m7 == "x1":
        x1 = "X"

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
        j = "O"
    if m8 == "k":
        k = "O"
    if m8 == "l":
        l = "O"
    if m8 == "m":
        m = "O"
    if m8 == "n":
        n = "O"
    if m8 == "o":
        o = "O"
    if m8 == "p":
        p = "O"
    if m8 == "q":
        q = "O"
    if m8 == "r":
        r = "O"
    if m8 == "s":
        s = "O"
    if m8 == "t":
        t = "O"
    if m8 == "u":
        u = "O"
    if m8 == "v":
        v = "O"
    if m8 == "w":
        w = "O"
    if m8 == "x":
        x = "O"
    if m8 == "y":
        y = "O"
    if m8 == "z":
        z = "O"
    if m8 == "a1":
        a1 = "O"
    if m8 == "b1":
        b1 = "O"
    if m8 == "c1":
        c1 = "O"
    if m8 == "d1":
        d1 = "O"
    if m8 == "e1":
        e1 = "O"
    if m8 == "f1":
        f1 = "O"
    if m8 == "g1":
        g1 = "O"
    if m8 == "h1":
        h1 = "O"
    if m8 == "i1":
        i1 = "O"
    if m8 == "j1":
        j1 = "O"
    if m8 == "k1":
        k1 = "O"
    if m8 == "l1":
        l1 = "O"
    if m8 == "n1":
        n1 = "O"
    if m8 == "o1":
        o1 = "O"
    if m8 == "p1":
        p1 = "O"
    if m8 == "q1":
        q1 = "O"
    if m8 == "r1":
        r1 = "O"
    if m8 == "s1":
        s1 = "O"
    if m8 == "t1":
        t1 = "O"
    if m8 == "u1":
        u1 = "O"
    if m8 == "v1":
        v1 = "O"
    if m8 == "w1":
        w1 = "O"
    if m8 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m9 == "z":
        z = "X"
    if m9 == "a1":
        a1 = "X"
    if m9 == "b1":
        b1 = "X"
    if m9 == "c1":
        c1 = "X"
    if m9 == "d1":
        d1 = "X"
    if m9 == "e1":
        e1 = "X"
    if m9 == "f1":
        f1 = "X"
    if m9 == "g1":
        g1 = "X"
    if m9 == "h1":
        h1 = "X"
    if m9 == "i1":
        i1 = "X"
    if m9 == "j1":
        j1 = "X"
    if m9 == "k1":
        k1 = "X"
    if m9 == "l1":
        l1 = "X"
    if m9 == "n1":
        n1 = "X"
    if m9 == "o1":
        o1 = "X"
    if m9 == "p1":
        p1 = "X"
    if m9 == "q1":
        q1 = "X"
    if m9 == "r1":
        r1 = "X"
    if m9 == "s1":
        s1 = "X"
    if m9 == "t1":
        t1 = "X"
    if m9 == "u1":
        u1 = "X"
    if m9 == "v1":
        v1 = "X"
    if m9 == "w1":
        w1 = "X"
    if m9 == "x1":
        x1 = "X"

    print("move 10")
    m10 = input()
    if m10 == "a":
        a = "O"
    if m10 == "b":
        b = "O"
    if m10 == "c":
        c = "O"
    if m10 == "d":
        d = "O"
    if m10 == "e":
        e = "O"
    if m10 == "f":
        f = "O"
    if m10 == "g":
        g = "O"
    if m10 == "h":
        h = "O"
    if m10 == "i":
        i = "O"
    if m10 == "j":
        j = "O"
    if m10 == "k":
        k = "O"
    if m10 == "l":
        l = "O"
    if m10 == "m":
        m = "O"
    if m10 == "n":
        n = "O"
    if m10 == "o":
        o = "O"
    if m10 == "p":
        p = "O"
    if m10 == "q":
        q = "O"
    if m10 == "r":
        r = "O"
    if m10 == "s":
        s = "O"
    if m10 == "t":
        t = "O"
    if m10 == "u":
        u = "O"
    if m10 == "v":
        v = "O"
    if m10 == "w":
        w = "O"
    if m10 == "x":
        x = "O"
    if m10 == "y":
        y = "O"
    if m10 == "z":
        z = "O"
    if m10 == "a1":
        a1 = "O"
    if m10 == "b1":
        b1 = "O"
    if m10 == "c1":
        c1 = "O"
    if m10 == "d1":
        d1 = "O"
    if m10 == "e1":
        e1 = "O"
    if m10 == "f1":
        f1 = "O"
    if m10 == "g1":
        g1 = "O"
    if m10 == "h1":
        h1 = "O"
    if m10 == "i1":
        i1 = "O"
    if m10 == "j1":
        j1 = "O"
    if m10 == "k1":
        k1 = "O"
    if m10 == "l1":
        l1 = "O"
    if m10 == "n1":
        n1 = "O"
    if m10 == "o1":
        o1 = "O"
    if m10 == "p1":
        p1 = "O"
    if m10 == "q1":
        q1 = "O"
    if m10 == "r1":
        r1 = "O"
    if m10 == "s1":
        s1 = "O"
    if m10 == "t1":
        t1 = "O"
    if m10 == "u1":
        u1 = "O"
    if m10 == "v1":
        v1 = "O"
    if m10 == "w1":
        w1 = "O"
    if m10 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m11 == "z":
        z = "X"
    if m11 == "a1":
        a1 = "X"
    if m11 == "b1":
        b1 = "X"
    if m11 == "c1":
        c1 = "X"
    if m11 == "d1":
        d1 = "X"
    if m11 == "e1":
        e1 = "X"
    if m11 == "f1":
        f1 = "X"
    if m11 == "g1":
        g1 = "X"
    if m11 == "h1":
        h1 = "X"
    if m11 == "i1":
        i1 = "X"
    if m11 == "j1":
        j1 = "X"
    if m11 == "k1":
        k1 = "X"
    if m11 == "l1":
        l1 = "X"
    if m11 == "n1":
        n1 = "X"
    if m11 == "o1":
        o1 = "X"
    if m11 == "p1":
        p1 = "X"
    if m11 == "q1":
        q1 = "X"
    if m11 == "r1":
        r1 = "X"
    if m11 == "s1":
        s1 = "X"
    if m11 == "t1":
        t1 = "X"
    if m11 == "u1":
        u1 = "X"
    if m11 == "v1":
        v1 = "X"
    if m11 == "w1":
        w1 = "X"
    if m11 == "x1":
        x1 = "X"

    print("move 12")
    m12 = input()
    if m12 == "a":
        a = "O"
    if m12 == "b":
        b = "O"
    if m12 == "c":
        c = "O"
    if m12 == "d":
        d = "O"
    if m12 == "e":
        e = "O"
    if m12 == "f":
        f = "O"
    if m12 == "g":
        g = "O"
    if m12 == "h":
        h = "O"
    if m12 == "i":
        i = "O"
    if m12 == "j":
        j = "O"
    if m12 == "k":
        k = "O"
    if m12 == "l":
        l = "O"
    if m12 == "m":
        m = "O"
    if m12 == "n":
        n = "O"
    if m12 == "o":
        o = "O"
    if m12 == "p":
        p = "O"
    if m12 == "q":
        q = "O"
    if m12 == "r":
        r = "O"
    if m12 == "s":
        s = "O"
    if m12 == "t":
        t = "O"
    if m12 == "u":
        u = "O"
    if m12 == "v":
        v = "O"
    if m12 == "w":
        w = "O"
    if m12 == "x":
        x = "O"
    if m12 == "y":
        y = "O"
    if m12 == "z":
        z = "O"
    if m12 == "a1":
        a1 = "O"
    if m12 == "b1":
        b1 = "O"
    if m12 == "c1":
        c1 = "O"
    if m12 == "d1":
        d1 = "O"
    if m12 == "e1":
        e1 = "O"
    if m12 == "f1":
        f1 = "O"
    if m12 == "g1":
        g1 = "O"
    if m12 == "h1":
        h1 = "O"
    if m12 == "i1":
        i1 = "O"
    if m12 == "j1":
        j1 = "O"
    if m12 == "k1":
        k1 = "O"
    if m12 == "l1":
        l1 = "O"
    if m12 == "n1":
        n1 = "O"
    if m12 == "o1":
        o1 = "O"
    if m12 == "p1":
        p1 = "O"
    if m12 == "q1":
        q1 = "O"
    if m12 == "r1":
        r1 = "O"
    if m12 == "s1":
        s1 = "O"
    if m12 == "t1":
        t1 = "O"
    if m12 == "u1":
        u1 = "O"
    if m12 == "v1":
        v1 = "O"
    if m12 == "w1":
        w1 = "O"
    if m12 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m13 == "z":
        z = "X"
    if m13 == "a1":
        a1 = "X"
    if m13 == "b1":
        b1 = "X"
    if m13 == "c1":
        c1 = "X"
    if m13 == "d1":
        d1 = "X"
    if m13 == "e1":
        e1 = "X"
    if m13 == "f1":
        f1 = "X"
    if m13 == "g1":
        g1 = "X"
    if m13 == "h1":
        h1 = "X"
    if m13 == "i1":
        i1 = "X"
    if m13 == "j1":
        j1 = "X"
    if m13 == "k1":
        k1 = "X"
    if m13 == "l1":
        l1 = "X"
    if m13 == "n1":
        n1 = "X"
    if m13 == "o1":
        o1 = "X"
    if m13 == "p1":
        p1 = "X"
    if m13 == "q1":
        q1 = "X"
    if m13 == "r1":
        r1 = "X"
    if m13 == "s1":
        s1 = "X"
    if m13 == "t1":
        t1 = "X"
    if m13 == "u1":
        u1 = "X"
    if m13 == "v1":
        v1 = "X"
    if m13 == "w1":
        w1 = "X"
    if m13 == "x1":
        x1 = "X"

    print("move 14")
    m14 = input()
    if m14 == "a":
        a = "O"
    if m14 == "b":
        b = "O"
    if m14 == "c":
        c = "O"
    if m14 == "d":
        d = "O"
    if m14 == "e":
        e = "O"
    if m14 == "f":
        f = "O"
    if m14 == "g":
        g = "O"
    if m14 == "h":
        h = "O"
    if m14 == "i":
        i = "O"
    if m14 == "j":
        j = "O"
    if m14 == "k":
        k = "O"
    if m14 == "l":
        l = "O"
    if m14 == "m":
        m = "O"
    if m14 == "n":
        n = "O"
    if m14 == "o":
        o = "O"
    if m14 == "p":
        p = "O"
    if m14 == "q":
        q = "O"
    if m14 == "r":
        r = "O"
    if m14 == "s":
        s = "O"
    if m14 == "t":
        t = "O"
    if m14 == "u":
        u = "O"
    if m14 == "v":
        v = "O"
    if m14 == "w":
        w = "O"
    if m14 == "x":
        x = "O"
    if m14 == "y":
        y = "O"
    if m14 == "z":
        z = "O"
    if m14 == "a1":
        a1 = "O"
    if m14 == "b1":
        b1 = "O"
    if m14 == "c1":
        c1 = "O"
    if m14 == "d1":
        d1 = "O"
    if m14 == "e1":
        e1 = "O"
    if m14 == "f1":
        f1 = "O"
    if m14 == "g1":
        g1 = "O"
    if m14 == "h1":
        h1 = "O"
    if m14 == "i1":
        i1 = "O"
    if m14 == "j1":
        j1 = "O"
    if m14 == "k1":
        k1 = "O"
    if m14 == "l1":
        l1 = "O"
    if m14 == "n1":
        n1 = "O"
    if m14 == "o1":
        o1 = "O"
    if m14 == "p1":
        p1 = "O"
    if m14 == "q1":
        q1 = "O"
    if m14 == "r1":
        r1 = "O"
    if m14 == "s1":
        s1 = "O"
    if m14 == "t1":
        t1 = "O"
    if m14 == "u1":
        u1 = "O"
    if m14 == "v1":
        v1 = "O"
    if m14 == "w1":
        w1 = "O"
    if m14 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m15 == "z":
        z = "X"
    if m15 == "a1":
        a1 = "X"
    if m15 == "b1":
        b1 = "X"
    if m15 == "c1":
        c1 = "X"
    if m15 == "d1":
        d1 = "X"
    if m15 == "e1":
        e1 = "X"
    if m15 == "f1":
        f1 = "X"
    if m15 == "g1":
        g1 = "X"
    if m15 == "h1":
        h1 = "X"
    if m15 == "i1":
        i1 = "X"
    if m15 == "j1":
        j1 = "X"
    if m15 == "k1":
        k1 = "X"
    if m15 == "l1":
        l1 = "X"
    if m15 == "n1":
        n1 = "X"
    if m15 == "o1":
        o1 = "X"
    if m15 == "p1":
        p1 = "X"
    if m15 == "q1":
        q1 = "X"
    if m15 == "r1":
        r1 = "X"
    if m15 == "s1":
        s1 = "X"
    if m15 == "t1":
        t1 = "X"
    if m15 == "u1":
        u1 = "X"
    if m15 == "v1":
        v1 = "X"
    if m15 == "w1":
        w1 = "X"
    if m15 == "x1":
        x1 = "X"

    print("move 16")
    m16 = input()
    if m16 == "a":
        a = "O"
    if m16 == "b":
        b = "O"
    if m16 == "c":
        c = "O"
    if m16 == "d":
        d = "O"
    if m16 == "e":
        e = "O"
    if m16 == "f":
        f = "O"
    if m16 == "g":
        g = "O"
    if m16 == "h":
        h = "O"
    if m16 == "i":
        i = "O"
    if m16 == "j":
        j = "O"
    if m16 == "k":
        k = "O"
    if m16 == "l":
        l = "O"
    if m16 == "m":
        m = "O"
    if m16 == "n":
        n = "O"
    if m16 == "o":
        o = "O"
    if m16 == "p":
        p = "O"
    if m16 == "q":
        q = "O"
    if m16 == "r":
        r = "O"
    if m16 == "s":
        s = "O"
    if m16 == "t":
        t = "O"
    if m16 == "u":
        u = "O"
    if m16 == "v":
        v = "O"
    if m16 == "w":
        w = "O"
    if m16 == "x":
        x = "O"
    if m16 == "y":
        y = "O"
    if m16 == "z":
        z = "O"
    if m16 == "a1":
        a1 = "O"
    if m16 == "b1":
        b1 = "O"
    if m16 == "c1":
        c1 = "O"
    if m16 == "d1":
        d1 = "O"
    if m16 == "e1":
        e1 = "O"
    if m16 == "f1":
        f1 = "O"
    if m16 == "g1":
        g1 = "O"
    if m16 == "h1":
        h1 = "O"
    if m16 == "i1":
        i1 = "O"
    if m16 == "j1":
        j1 = "O"
    if m16 == "k1":
        k1 = "O"
    if m16 == "l1":
        l1 = "O"
    if m16 == "n1":
        n1 = "O"
    if m16 == "o1":
        o1 = "O"
    if m16 == "p1":
        p1 = "O"
    if m16 == "q1":
        q1 = "O"
    if m16 == "r1":
        r1 = "O"
    if m16 == "s1":
        s1 = "O"
    if m16 == "t1":
        t1 = "O"
    if m16 == "u1":
        u1 = "O"
    if m16 == "v1":
        v1 = "O"
    if m16 == "w1":
        w1 = "O"
    if m16 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m17 == "z":
        z = "X"
    if m17 == "a1":
        a1 = "X"
    if m17 == "b1":
        b1 = "X"
    if m17 == "c1":
        c1 = "X"
    if m17 == "d1":
        d1 = "X"
    if m17 == "e1":
        e1 = "X"
    if m17 == "f1":
        f1 = "X"
    if m17 == "g1":
        g1 = "X"
    if m17 == "h1":
        h1 = "X"
    if m17 == "i1":
        i1 = "X"
    if m17 == "j1":
        j1 = "X"
    if m17 == "k1":
        k1 = "X"
    if m17 == "l1":
        l1 = "X"
    if m17 == "n1":
        n1 = "X"
    if m17 == "o1":
        o1 = "X"
    if m17 == "p1":
        p1 = "X"
    if m17 == "q1":
        q1 = "X"
    if m17 == "r1":
        r1 = "X"
    if m17 == "s1":
        s1 = "X"
    if m17 == "t1":
        t1 = "X"
    if m17 == "u1":
        u1 = "X"
    if m17 == "v1":
        v1 = "X"
    if m17 == "w1":
        w1 = "X"
    if m17 == "x1":
        x1 = "X"

    print("move 18")
    m18 = input()
    if m18 == "a":
        a = "O"
    if m18 == "b":
        b = "O"
    if m18 == "c":
        c = "O"
    if m18 == "d":
        d = "O"
    if m18 == "e":
        e = "O"
    if m18 == "f":
        f = "O"
    if m18 == "g":
        g = "O"
    if m18 == "h":
        h = "O"
    if m18 == "i":
        i = "O"
    if m18 == "j":
        j = "O"
    if m18 == "k":
        k = "O"
    if m18 == "l":
        l = "O"
    if m18 == "m":
        m = "O"
    if m18 == "n":
        n = "O"
    if m18 == "o":
        o = "O"
    if m18 == "p":
        p = "O"
    if m18 == "q":
        q = "O"
    if m18 == "r":
        r = "O"
    if m18 == "s":
        s = "O"
    if m18 == "t":
        t = "O"
    if m18 == "u":
        u = "O"
    if m18 == "v":
        v = "O"
    if m18 == "w":
        w = "O"
    if m18 == "x":
        x = "O"
    if m18 == "y":
        y = "O"
    if m18 == "z":
        z = "O"
    if m18 == "a1":
        a1 = "O"
    if m18 == "b1":
        b1 = "O"
    if m18 == "c1":
        c1 = "O"
    if m18 == "d1":
        d1 = "O"
    if m18 == "e1":
        e1 = "O"
    if m18 == "f1":
        f1 = "O"
    if m18 == "g1":
        g1 = "O"
    if m18 == "h1":
        h1 = "O"
    if m18 == "i1":
        i1 = "O"
    if m18 == "j1":
        j1 = "O"
    if m18 == "k1":
        k1 = "O"
    if m18 == "l1":
        l1 = "O"
    if m18 == "n1":
        n1 = "O"
    if m18 == "o1":
        o1 = "O"
    if m18 == "p1":
        p1 = "O"
    if m18 == "q1":
        q1 = "O"
    if m18 == "r1":
        r1 = "O"
    if m18 == "s1":
        s1 = "O"
    if m18 == "t1":
        t1 = "O"
    if m18 == "u1":
        u1 = "O"
    if m18 == "v1":
        v1 = "O"
    if m18 == "w1":
        w1 = "O"
    if m18 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m19 == "z":
        z = "X"
    if m19 == "a1":
        a1 = "X"
    if m19 == "b1":
        b1 = "X"
    if m19 == "c1":
        c1 = "X"
    if m19 == "d1":
        d1 = "X"
    if m19 == "e1":
        e1 = "X"
    if m19 == "f1":
        f1 = "X"
    if m19 == "g1":
        g1 = "X"
    if m19 == "h1":
        h1 = "X"
    if m19 == "i1":
        i1 = "X"
    if m19 == "j1":
        j1 = "X"
    if m19 == "k1":
        k1 = "X"
    if m19 == "l1":
        l1 = "X"
    if m19 == "n1":
        n1 = "X"
    if m19 == "o1":
        o1 = "X"
    if m19 == "p1":
        p1 = "X"
    if m19 == "q1":
        q1 = "X"
    if m19 == "r1":
        r1 = "X"
    if m19 == "s1":
        s1 = "X"
    if m19 == "t1":
        t1 = "X"
    if m19 == "u1":
        u1 = "X"
    if m19 == "v1":
        v1 = "X"
    if m19 == "w1":
        w1 = "X"
    if m19 == "x1":
        x1 = "X"

    print("move 20")
    m20 = input()
    if m20 == "a":
        a = "O"
    if m20 == "b":
        b = "O"
    if m20 == "c":
        c = "O"
    if m20 == "d":
        d = "O"
    if m20 == "e":
        e = "O"
    if m20 == "f":
        f = "O"
    if m20 == "g":
        g = "O"
    if m20 == "h":
        h = "O"
    if m20 == "i":
        i = "O"
    if m20 == "j":
        j = "O"
    if m20 == "k":
        k = "O"
    if m20 == "l":
        l = "O"
    if m20 == "m":
        m = "O"
    if m20 == "n":
        n = "O"
    if m20 == "o":
        o = "O"
    if m20 == "p":
        p = "O"
    if m20 == "q":
        q = "O"
    if m20 == "r":
        r = "O"
    if m20 == "s":
        s = "O"
    if m20 == "t":
        t = "O"
    if m20 == "u":
        u = "O"
    if m20 == "v":
        v = "O"
    if m20 == "w":
        w = "O"
    if m20 == "x":
        x = "O"
    if m20 == "y":
        y = "O"
    if m20 == "z":
        z = "O"
    if m20 == "a1":
        a1 = "O"
    if m20 == "b1":
        b1 = "O"
    if m20 == "c1":
        c1 = "O"
    if m20 == "d1":
        d1 = "O"
    if m20 == "e1":
        e1 = "O"
    if m20 == "f1":
        f1 = "O"
    if m20 == "g1":
        g1 = "O"
    if m20 == "h1":
        h1 = "O"
    if m20 == "i1":
        i1 = "O"
    if m20 == "j1":
        j1 = "O"
    if m20 == "k1":
        k1 = "O"
    if m20 == "l1":
        l1 = "O"
    if m20 == "n1":
        n1 = "O"
    if m20 == "o1":
        o1 = "O"
    if m20 == "p1":
        p1 = "O"
    if m20 == "q1":
        q1 = "O"
    if m20 == "r1":
        r1 = "O"
    if m20 == "s1":
        s1 = "O"
    if m20 == "t1":
        t1 = "O"
    if m20 == "u1":
        u1 = "O"
    if m20 == "v1":
        v1 = "O"
    if m20 == "w1":
        w1 = "O"
    if m20 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m21 == "z":
        z = "X"
    if m21 == "a1":
        a1 = "X"
    if m21 == "b1":
        b1 = "X"
    if m21 == "c1":
        c1 = "X"
    if m21 == "d1":
        d1 = "X"
    if m21 == "e1":
        e1 = "X"
    if m21 == "f1":
        f1 = "X"
    if m21 == "g1":
        g1 = "X"
    if m21 == "h1":
        h1 = "X"
    if m21 == "i1":
        i1 = "X"
    if m21 == "j1":
        j1 = "X"
    if m21 == "k1":
        k1 = "X"
    if m21 == "l1":
        l1 = "X"
    if m21 == "n1":
        n1 = "X"
    if m21 == "o1":
        o1 = "X"
    if m21 == "p1":
        p1 = "X"
    if m21 == "q1":
        q1 = "X"
    if m21 == "r1":
        r1 = "X"
    if m21 == "s1":
        s1 = "X"
    if m21 == "t1":
        t1 = "X"
    if m21 == "u1":
        u1 = "X"
    if m21 == "v1":
        v1 = "X"
    if m21 == "w1":
        w1 = "X"
    if m21 == "x1":
        x1 = "X"

    print("move 22")
    m22 = input()
    if m22 == "a":
        a = "O"
    if m22 == "b":
        b = "O"
    if m22 == "c":
        c = "O"
    if m22 == "d":
        d = "O"
    if m22 == "e":
        e = "O"
    if m22 == "f":
        f = "O"
    if m22 == "g":
        g = "O"
    if m22 == "h":
        h = "O"
    if m22 == "i":
        i = "O"
    if m22 == "j":
        j = "O"
    if m22 == "k":
        k = "O"
    if m22 == "l":
        l = "O"
    if m22 == "m":
        m = "O"
    if m22 == "n":
        n = "O"
    if m22 == "o":
        o = "O"
    if m22 == "p":
        p = "O"
    if m22 == "q":
        q = "O"
    if m22 == "r":
        r = "O"
    if m22 == "s":
        s = "O"
    if m22 == "t":
        t = "O"
    if m22 == "u":
        u = "O"
    if m22 == "v":
        v = "O"
    if m22 == "w":
        w = "O"
    if m22 == "x":
        x = "O"
    if m22 == "y":
        y = "O"
    if m22 == "z":
        z = "O"
    if m22 == "a1":
        a1 = "O"
    if m22 == "b1":
        b1 = "O"
    if m22 == "c1":
        c1 = "O"
    if m22 == "d1":
        d1 = "O"
    if m22 == "e1":
        e1 = "O"
    if m22 == "f1":
        f1 = "O"
    if m22 == "g1":
        g1 = "O"
    if m22 == "h1":
        h1 = "O"
    if m22 == "i1":
        i1 = "O"
    if m22 == "j1":
        j1 = "O"
    if m22 == "k1":
        k1 = "O"
    if m22 == "l1":
        l1 = "O"
    if m22 == "n1":
        n1 = "O"
    if m22 == "o1":
        o1 = "O"
    if m22 == "p1":
        p1 = "O"
    if m22 == "q1":
        q1 = "O"
    if m22 == "r1":
        r1 = "O"
    if m22 == "s1":
        s1 = "O"
    if m22 == "t1":
        t1 = "O"
    if m22 == "u1":
        u1 = "O"
    if m22 == "v1":
        v1 = "O"
    if m22 == "w1":
        w1 = "O"
    if m22 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m23 == "z":
        z = "X"
    if m23 == "a1":
        a1 = "X"
    if m23 == "b1":
        b1 = "X"
    if m23 == "c1":
        c1 = "X"
    if m23 == "d1":
        d1 = "X"
    if m23 == "e1":
        e1 = "X"
    if m23 == "f1":
        f1 = "X"
    if m23 == "g1":
        g1 = "X"
    if m23 == "h1":
        h1 = "X"
    if m23 == "i1":
        i1 = "X"
    if m23 == "j1":
        j1 = "X"
    if m23 == "k1":
        k1 = "X"
    if m23 == "l1":
        l1 = "X"
    if m23 == "n1":
        n1 = "X"
    if m23 == "o1":
        o1 = "X"
    if m23 == "p1":
        p1 = "X"
    if m23 == "q1":
        q1 = "X"
    if m23 == "r1":
        r1 = "X"
    if m23 == "s1":
        s1 = "X"
    if m23 == "t1":
        t1 = "X"
    if m23 == "u1":
        u1 = "X"
    if m23 == "v1":
        v1 = "X"
    if m23 == "w1":
        w1 = "X"
    if m23 == "x1":
        x1 = "X"

    print("move 24")
    m24 = input()
    if m24 == "a":
        a = "O"
    if m24 == "b":
        b = "O"
    if m24 == "c":
        c = "O"
    if m24 == "d":
        d = "O"
    if m24 == "e":
        e = "O"
    if m24 == "f":
        f = "O"
    if m24 == "g":
        g = "O"
    if m24 == "h":
        h = "O"
    if m24 == "i":
        i = "O"
    if m24 == "j":
        j = "O"
    if m24 == "k":
        k = "O"
    if m24 == "l":
        l = "O"
    if m24 == "m":
        m = "O"
    if m24 == "n":
        n = "O"
    if m24 == "o":
        o = "O"
    if m24 == "p":
        p = "O"
    if m24 == "q":
        q = "O"
    if m24 == "r":
        r = "O"
    if m24 == "s":
        s = "O"
    if m24 == "t":
        t = "O"
    if m24 == "u":
        u = "O"
    if m24 == "v":
        v = "O"
    if m24 == "w":
        w = "O"
    if m24 == "x":
        x = "O"
    if m24 == "y":
        y = "O"
    if m24 == "z":
        z = "O"
    if m24 == "a1":
        a1 = "O"
    if m24 == "b1":
        b1 = "O"
    if m24 == "c1":
        c1 = "O"
    if m24 == "d1":
        d1 = "O"
    if m24 == "e1":
        e1 = "O"
    if m24 == "f1":
        f1 = "O"
    if m24 == "g1":
        g1 = "O"
    if m24 == "h1":
        h1 = "O"
    if m24 == "i1":
        i1 = "O"
    if m24 == "j1":
        j1 = "O"
    if m24 == "k1":
        k1 = "O"
    if m24 == "l1":
        l1 = "O"
    if m24 == "n1":
        n1 = "O"
    if m24 == "o1":
        o1 = "O"
    if m24 == "p1":
        p1 = "O"
    if m24 == "q1":
        q1 = "O"
    if m24 == "r1":
        r1 = "O"
    if m24 == "s1":
        s1 = "O"
    if m24 == "t1":
        t1 = "O"
    if m24 == "u1":
        u1 = "O"
    if m24 == "v1":
        v1 = "O"
    if m24 == "w1":
        w1 = "O"
    if m24 == "x1":
        x1 = "O"

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
        q = "X"
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
    if m25 == "z":
        z = "X"
    if m25 == "a1":
        a1 = "X"
    if m25 == "b1":
        b1 = "X"
    if m25 == "c1":
        c1 = "X"
    if m25 == "d1":
        d1 = "X"
    if m25 == "e1":
        e1 = "X"
    if m25 == "f1":
        f1 = "X"
    if m25 == "g1":
        g1 = "X"
    if m25 == "h1":
        h1 = "X"
    if m25 == "i1":
        i1 = "X"
    if m25 == "j1":
        j1 = "X"
    if m25 == "k1":
        k1 = "X"
    if m25 == "l1":
        l1 = "X"
    if m25 == "n1":
        n1 = "X"
    if m25 == "o1":
        o1 = "X"
    if m25 == "p1":
        p1 = "X"
    if m25 == "q1":
        q1 = "X"
    if m25 == "r1":
        r1 = "X"
    if m25 == "s1":
        s1 = "X"
    if m25 == "t1":
        t1 = "X"
    if m25 == "u1":
        u1 = "X"
    if m25 == "v1":
        v1 = "X"
    if m25 == "w1":
        w1 = "X"
    if m25 == "x1":
        x1 = "X"

    print("move 26")
    m26 = input()
    if m26 == "a":
        a = "O"
    if m26 == "b":
        b = "O"
    if m26 == "c":
        c = "O"
    if m26 == "d":
        d = "O"
    if m26 == "e":
        e = "O"
    if m26 == "f":
        f = "O"
    if m26 == "g":
        g = "O"
    if m26 == "h":
        h = "O"
    if m26 == "i":
        i = "O"
    if m26 == "j":
        j = "O"
    if m26 == "k":
        k = "O"
    if m26 == "l":
        l = "O"
    if m26 == "m":
        m = "O"
    if m26 == "n":
        n = "O"
    if m26 == "o":
        o = "O"
    if m26 == "p":
        p = "O"
    if m26 == "q":
        q = "O"
    if m26 == "r":
        r = "O"
    if m26 == "s":
        s = "O"
    if m26 == "t":
        t = "O"
    if m26 == "u":
        u = "O"
    if m26 == "v":
        v = "O"
    if m26 == "w":
        w = "O"
    if m26 == "x":
        x = "O"
    if m26 == "y":
        y = "O"
    if m26 == "z":
        z = "O"
    if m26 == "a1":
        a1 = "O"
    if m26 == "b1":
        b1 = "O"
    if m26 == "c1":
        c1 = "O"
    if m26 == "d1":
        d1 = "O"
    if m26 == "e1":
        e1 = "O"
    if m26 == "f1":
        f1 = "O"
    if m26 == "g1":
        g1 = "O"
    if m26 == "h1":
        h1 = "O"
    if m26 == "i1":
        i1 = "O"
    if m26 == "j1":
        j1 = "O"
    if m26 == "k1":
        k1 = "O"
    if m26 == "l1":
        l1 = "O"
    if m26 == "n1":
        n1 = "O"
    if m26 == "o1":
        o1 = "O"
    if m26 == "p1":
        p1 = "O"
    if m26 == "q1":
        q1 = "O"
    if m26 == "r1":
        r1 = "O"
    if m26 == "s1":
        s1 = "O"
    if m26 == "t1":
        t1 = "O"
    if m26 == "u1":
        u1 = "O"
    if m26 == "v1":
        v1 = "O"
    if m26 == "w1":
        w1 = "O"
    if m26 == "x1":
        x1 = "O"

    print("move 27")
    m27 = input()
    if m27 == "a":
        a = "X"
    if m27 == "b":
        b = "X"
    if m27 == "c":
        c = "X"
    if m27 == "d":
        d = "X"
    if m27 == "e":
        e = "X"
    if m27 == "f":
        f = "X"
    if m27 == "g":
        g = "X"
    if m27 == "h":
        h = "X"
    if m27 == "i":
        i = "X"
    if m27 == "j":
        j = "X"
    if m27 == "k":
        k = "X"
    if m27 == "l":
        l = "X"
    if m27 == "m":
        m = "X"
    if m27 == "n":
        n = "X"
    if m27 == "o":
        o = "X"
    if m27 == "p":
        p = "X"
    if m27 == "q":
        q = "X"
    if m27 == "r":
        r = "X"
    if m27 == "s":
        s = "X"
    if m27 == "t":
        t = "X"
    if m27 == "u":
        u = "X"
    if m27 == "v":
        v = "X"
    if m27 == "w":
        w = "X"
    if m27 == "x":
        x = "X"
    if m27 == "y":
        y = "X"
    if m27 == "z":
        z = "X"
    if m27 == "a1":
        a1 = "X"
    if m27 == "b1":
        b1 = "X"
    if m27 == "c1":
        c1 = "X"
    if m27 == "d1":
        d1 = "X"
    if m27 == "e1":
        e1 = "X"
    if m27 == "f1":
        f1 = "X"
    if m27 == "g1":
        g1 = "X"
    if m27 == "h1":
        h1 = "X"
    if m27 == "i1":
        i1 = "X"
    if m27 == "j1":
        j1 = "X"
    if m27 == "k1":
        k1 = "X"
    if m27 == "l1":
        l1 = "X"
    if m27 == "n1":
        n1 = "X"
    if m27 == "o1":
        o1 = "X"
    if m27 == "p1":
        p1 = "X"
    if m27 == "q1":
        q1 = "X"
    if m27 == "r1":
        r1 = "X"
    if m27 == "s1":
        s1 = "X"
    if m27 == "t1":
        t1 = "X"
    if m27 == "u1":
        u1 = "X"
    if m27 == "v1":
        v1 = "X"
    if m27 == "w1":
        w1 = "X"
    if m27 == "x1":
        x1 = "X"

    print("move 28")
    m28 = input()
    if m28 == "a":
        a = "O"
    if m28 == "b":
        b = "O"
    if m28 == "c":
        c = "O"
    if m28 == "d":
        d = "O"
    if m28 == "e":
        e = "O"
    if m28 == "f":
        f = "O"
    if m28 == "g":
        g = "O"
    if m28 == "h":
        h = "O"
    if m28 == "i":
        i = "O"
    if m28 == "j":
        j = "O"
    if m28 == "k":
        k = "O"
    if m28 == "l":
        l = "O"
    if m28 == "m":
        m = "O"
    if m28 == "n":
        n = "O"
    if m28 == "o":
        o = "O"
    if m28 == "p":
        p = "O"
    if m28 == "q":
        q = "O"
    if m28 == "r":
        r = "O"
    if m28 == "s":
        s = "O"
    if m28 == "t":
        t = "O"
    if m28 == "u":
        u = "O"
    if m28 == "v":
        v = "O"
    if m28 == "w":
        w = "O"
    if m28 == "x":
        x = "O"
    if m28 == "y":
        y = "O"
    if m28 == "z":
        z = "O"
    if m28 == "a1":
        a1 = "O"
    if m28 == "b1":
        b1 = "O"
    if m28 == "c1":
        c1 = "O"
    if m28 == "d1":
        d1 = "O"
    if m28 == "e1":
        e1 = "O"
    if m28 == "f1":
        f1 = "O"
    if m28 == "g1":
        g1 = "O"
    if m28 == "h1":
        h1 = "O"
    if m28 == "i1":
        i1 = "O"
    if m28 == "j1":
        j1 = "O"
    if m28 == "k1":
        k1 = "O"
    if m28 == "l1":
        l1 = "O"
    if m28 == "n1":
        n1 = "O"
    if m28 == "o1":
        o1 = "O"
    if m28 == "p1":
        p1 = "O"
    if m28 == "q1":
        q1 = "O"
    if m28 == "r1":
        r1 = "O"
    if m28 == "s1":
        s1 = "O"
    if m28 == "t1":
        t1 = "O"
    if m28 == "u1":
        u1 = "O"
    if m28 == "v1":
        v1 = "O"
    if m28 == "w1":
        w1 = "O"
    if m28 == "x1":
        x1 = "O"

    print("move 29")
    m29 = input()
    if m29 == "a":
        a = "X"
    if m29 == "b":
        b = "X"
    if m29 == "c":
        c = "X"
    if m29 == "d":
        d = "X"
    if m29 == "e":
        e = "X"
    if m29 == "f":
        f = "X"
    if m29 == "g":
        g = "X"
    if m29 == "h":
        h = "X"
    if m29 == "i":
        i = "X"
    if m29 == "j":
        j = "X"
    if m29 == "k":
        k = "X"
    if m29 == "l":
        l = "X"
    if m29 == "m":
        m = "X"
    if m29 == "n":
        n = "X"
    if m29 == "o":
        o = "X"
    if m29 == "p":
        p = "X"
    if m29 == "q":
        q = "X"
    if m29 == "r":
        r = "X"
    if m29 == "s":
        s = "X"
    if m29 == "t":
        t = "X"
    if m29 == "u":
        u = "X"
    if m29 == "v":
        v = "X"
    if m29 == "w":
        w = "X"
    if m29 == "x":
        x = "X"
    if m29 == "y":
        y = "X"
    if m29 == "z":
        z = "X"
    if m29 == "a1":
        a1 = "X"
    if m29 == "b1":
        b1 = "X"
    if m29 == "c1":
        c1 = "X"
    if m29 == "d1":
        d1 = "X"
    if m29 == "e1":
        e1 = "X"
    if m29 == "f1":
        f1 = "X"
    if m29 == "g1":
        g1 = "X"
    if m29 == "h1":
        h1 = "X"
    if m29 == "i1":
        i1 = "X"
    if m29 == "j1":
        j1 = "X"
    if m29 == "k1":
        k1 = "X"
    if m29 == "l1":
        l1 = "X"
    if m29 == "n1":
        n1 = "X"
    if m29 == "o1":
        o1 = "X"
    if m29 == "p1":
        p1 = "X"
    if m29 == "q1":
        q1 = "X"
    if m29 == "r1":
        r1 = "X"
    if m29 == "s1":
        s1 = "X"
    if m29 == "t1":
        t1 = "X"
    if m29 == "u1":
        u1 = "X"
    if m29 == "v1":
        v1 = "X"
    if m29 == "w1":
        w1 = "X"
    if m29 == "x1":
        x1 = "X"

    print("move 30")
    m30 = input()
    if m30 == "a":
        a = "O"
    if m30 == "b":
        b = "O"
    if m30 == "c":
        c = "O"
    if m30 == "d":
        d = "O"
    if m30 == "e":
        e = "O"
    if m30 == "f":
        f = "O"
    if m30 == "g":
        g = "O"
    if m30 == "h":
        h = "O"
    if m30 == "i":
        i = "O"
    if m30 == "j":
        j = "O"
    if m30 == "k":
        k = "O"
    if m30 == "l":
        l = "O"
    if m30 == "m":
        m = "O"
    if m30 == "n":
        n = "O"
    if m30 == "o":
        o = "O"
    if m30 == "p":
        p = "O"
    if m30 == "q":
        q = "O"
    if m30 == "r":
        r = "O"
    if m30 == "s":
        s = "O"
    if m30 == "t":
        t = "O"
    if m30 == "u":
        u = "O"
    if m30 == "v":
        v = "O"
    if m30 == "w":
        w = "O"
    if m30 == "x":
        x = "O"
    if m30 == "y":
        y = "O"
    if m30 == "z":
        z = "O"
    if m30 == "a1":
        a1 = "O"
    if m30 == "b1":
        b1 = "O"
    if m30 == "c1":
        c1 = "O"
    if m30 == "d1":
        d1 = "O"
    if m30 == "e1":
        e1 = "O"
    if m30 == "f1":
        f1 = "O"
    if m30 == "g1":
        g1 = "O"
    if m30 == "h1":
        h1 = "O"
    if m30 == "i1":
        i1 = "O"
    if m30 == "j1":
        j1 = "O"
    if m30 == "k1":
        k1 = "O"
    if m30 == "l1":
        l1 = "O"
    if m30 == "n1":
        n1 = "O"
    if m30 == "o1":
        o1 = "O"
    if m30 == "p1":
        p1 = "O"
    if m30 == "q1":
        q1 = "O"
    if m30 == "r1":
        r1 = "O"
    if m30 == "s1":
        s1 = "O"
    if m30 == "t1":
        t1 = "O"
    if m30 == "u1":
        u1 = "O"
    if m30 == "v1":
        v1 = "O"
    if m30 == "w1":
        w1 = "O"
    if m30 == "x1":
        x1 = "O"

    print("move 31")
    m31 = input()
    if m31 == "a":
        a = "X"
    if m31 == "b":
        b = "X"
    if m31 == "c":
        c = "X"
    if m31 == "d":
        d = "X"
    if m31 == "e":
        e = "X"
    if m31 == "f":
        f = "X"
    if m31 == "g":
        g = "X"
    if m31 == "h":
        h = "X"
    if m31 == "i":
        i = "X"
    if m31 == "j":
        j = "X"
    if m31 == "k":
        k = "X"
    if m31 == "l":
        l = "X"
    if m31 == "m":
        m = "X"
    if m31 == "n":
        n = "X"
    if m31 == "o":
        o = "X"
    if m31 == "p":
        p = "X"
    if m31 == "q":
        q = "X"
    if m31 == "r":
        r = "X"
    if m31 == "s":
        s = "X"
    if m31 == "t":
        t = "X"
    if m31 == "u":
        u = "X"
    if m31 == "v":
        v = "X"
    if m31 == "w":
        w = "X"
    if m31 == "x":
        x = "X"
    if m31 == "y":
        y = "X"
    if m31 == "z":
        z = "X"
    if m31 == "a1":
        a1 = "X"
    if m31 == "b1":
        b1 = "X"
    if m31 == "c1":
        c1 = "X"
    if m31 == "d1":
        d1 = "X"
    if m31 == "e1":
        e1 = "X"
    if m31 == "f1":
        f1 = "X"
    if m31 == "g1":
        g1 = "X"
    if m31 == "h1":
        h1 = "X"
    if m31 == "i1":
        i1 = "X"
    if m31 == "j1":
        j1 = "X"
    if m31 == "k1":
        k1 = "X"
    if m31 == "l1":
        l1 = "X"
    if m31 == "n1":
        n1 = "X"
    if m31 == "o1":
        o1 = "X"
    if m31 == "p1":
        p1 = "X"
    if m31 == "q1":
        q1 = "X"
    if m31 == "r1":
        r1 = "X"
    if m31 == "s1":
        s1 = "X"
    if m31 == "t1":
        t1 = "X"
    if m31 == "u1":
        u1 = "X"
    if m31 == "v1":
        v1 = "X"
    if m31 == "w1":
        w1 = "X"
    if m31 == "x1":
        x1 = "X"

    print("move 32")
    m32 = input()
    if m32 == "a":
        a = "O"
    if m32 == "b":
        b = "O"
    if m32 == "c":
        c = "O"
    if m32 == "d":
        d = "O"
    if m32 == "e":
        e = "O"
    if m32 == "f":
        f = "O"
    if m32 == "g":
        g = "O"
    if m32 == "h":
        h = "O"
    if m32 == "i":
        i = "O"
    if m32 == "j":
        j = "O"
    if m32 == "k":
        k = "O"
    if m32 == "l":
        l = "O"
    if m32 == "m":
        m = "O"
    if m32 == "n":
        n = "O"
    if m32 == "o":
        o = "O"
    if m32 == "p":
        p = "O"
    if m32 == "q":
        q = "O"
    if m32 == "r":
        r = "O"
    if m32 == "s":
        s = "O"
    if m32 == "t":
        t = "O"
    if m32 == "u":
        u = "O"
    if m32 == "v":
        v = "O"
    if m32 == "w":
        w = "O"
    if m32 == "x":
        x = "O"
    if m32 == "y":
        y = "O"
    if m32 == "z":
        z = "O"
    if m32 == "a1":
        a1 = "O"
    if m32 == "b1":
        b1 = "O"
    if m32 == "c1":
        c1 = "O"
    if m32 == "d1":
        d1 = "O"
    if m32 == "e1":
        e1 = "O"
    if m32 == "f1":
        f1 = "O"
    if m32 == "g1":
        g1 = "O"
    if m32 == "h1":
        h1 = "O"
    if m32 == "i1":
        i1 = "O"
    if m32 == "j1":
        j1 = "O"
    if m32 == "k1":
        k1 = "O"
    if m32 == "l1":
        l1 = "O"
    if m32 == "n1":
        n1 = "O"
    if m32 == "o1":
        o1 = "O"
    if m32 == "p1":
        p1 = "O"
    if m32 == "q1":
        q1 = "O"
    if m32 == "r1":
        r1 = "O"
    if m32 == "s1":
        s1 = "O"
    if m32 == "t1":
        t1 = "O"
    if m32 == "u1":
        u1 = "O"
    if m32 == "v1":
        v1 = "O"
    if m32 == "w1":
        w1 = "O"
    if m32 == "x1":
        x1 = "O"

    print("move 33")
    m33 = input()
    if m33 == "a":
        a = "X"
    if m33 == "b":
        b = "X"
    if m33 == "c":
        c = "X"
    if m33 == "d":
        d = "X"
    if m33 == "e":
        e = "X"
    if m33 == "f":
        f = "X"
    if m33 == "g":
        g = "X"
    if m33 == "h":
        h = "X"
    if m33 == "i":
        i = "X"
    if m33 == "j":
        j = "X"
    if m33 == "k":
        k = "X"
    if m33 == "l":
        l = "X"
    if m33 == "m":
        m = "X"
    if m33 == "n":
        n = "X"
    if m33 == "o":
        o = "X"
    if m33 == "p":
        p = "X"
    if m33 == "q":
        q = "X"
    if m33 == "r":
        r = "X"
    if m33 == "s":
        s = "X"
    if m33 == "t":
        t = "X"
    if m33 == "u":
        u = "X"
    if m33 == "v":
        v = "X"
    if m33 == "w":
        w = "X"
    if m33 == "x":
        x = "X"
    if m33 == "y":
        y = "X"
    if m33 == "z":
        z = "X"
    if m33 == "a1":
        a1 = "X"
    if m33 == "b1":
        b1 = "X"
    if m33 == "c1":
        c1 = "X"
    if m33 == "d1":
        d1 = "X"
    if m33 == "e1":
        e1 = "X"
    if m33 == "f1":
        f1 = "X"
    if m33 == "g1":
        g1 = "X"
    if m33 == "h1":
        h1 = "X"
    if m33 == "i1":
        i1 = "X"
    if m33 == "j1":
        j1 = "X"
    if m33 == "k1":
        k1 = "X"
    if m33 == "l1":
        l1 = "X"
    if m33 == "n1":
        n1 = "X"
    if m33 == "o1":
        o1 = "X"
    if m33 == "p1":
        p1 = "X"
    if m33 == "q1":
        q1 = "X"
    if m33 == "r1":
        r1 = "X"
    if m33 == "s1":
        s1 = "X"
    if m33 == "t1":
        t1 = "X"
    if m33 == "u1":
        u1 = "X"
    if m33 == "v1":
        v1 = "X"
    if m33 == "w1":
        w1 = "X"
    if m33 == "x1":
        x1 = "X"

    print("move 34")
    m34 = input()
    if m34 == "a":
        a = "O"
    if m34 == "b":
        b = "O"
    if m34 == "c":
        c = "O"
    if m34 == "d":
        d = "O"
    if m34 == "e":
        e = "O"
    if m34 == "f":
        f = "O"
    if m34 == "g":
        g = "O"
    if m34 == "h":
        h = "O"
    if m34 == "i":
        i = "O"
    if m34 == "j":
        j = "O"
    if m34 == "k":
        k = "O"
    if m34 == "l":
        l = "O"
    if m34 == "m":
        m = "O"
    if m34 == "n":
        n = "O"
    if m34 == "o":
        o = "O"
    if m34 == "p":
        p = "O"
    if m34 == "q":
        q = "O"
    if m34 == "r":
        r = "O"
    if m34 == "s":
        s = "O"
    if m34 == "t":
        t = "O"
    if m34 == "u":
        u = "O"
    if m34 == "v":
        v = "O"
    if m34 == "w":
        w = "O"
    if m34 == "x":
        x = "O"
    if m34 == "y":
        y = "O"
    if m34 == "z":
        z = "O"
    if m34 == "a1":
        a1 = "O"
    if m34 == "b1":
        b1 = "O"
    if m34 == "c1":
        c1 = "O"
    if m34 == "d1":
        d1 = "O"
    if m34 == "e1":
        e1 = "O"
    if m34 == "f1":
        f1 = "O"
    if m34 == "g1":
        g1 = "O"
    if m34 == "h1":
        h1 = "O"
    if m34 == "i1":
        i1 = "O"
    if m34 == "j1":
        j1 = "O"
    if m34 == "k1":
        k1 = "O"
    if m34 == "l1":
        l1 = "O"
    if m34 == "n1":
        n1 = "O"
    if m34 == "o1":
        o1 = "O"
    if m34 == "p1":
        p1 = "O"
    if m34 == "q1":
        q1 = "O"
    if m34 == "r1":
        r1 = "O"
    if m34 == "s1":
        s1 = "O"
    if m34 == "t1":
        t1 = "O"
    if m34 == "u1":
        u1 = "O"
    if m34 == "v1":
        v1 = "O"
    if m34 == "w1":
        w1 = "O"
    if m34 == "x1":
        x1 = "O"

    print("move 35")
    m35 = input()
    if m35 == "a":
        a = "X"
    if m35 == "b":
        b = "X"
    if m35 == "c":
        c = "X"
    if m35 == "d":
        d = "X"
    if m35 == "e":
        e = "X"
    if m35 == "f":
        f = "X"
    if m35 == "g":
        g = "X"
    if m35 == "h":
        h = "X"
    if m35 == "i":
        i = "X"
    if m35 == "j":
        j = "X"
    if m35 == "k":
        k = "X"
    if m35 == "l":
        l = "X"
    if m35 == "m":
        m = "X"
    if m35 == "n":
        n = "X"
    if m35 == "o":
        o = "X"
    if m35 == "p":
        p = "X"
    if m35 == "q":
        q = "X"
    if m35 == "r":
        r = "X"
    if m35 == "s":
        s = "X"
    if m35 == "t":
        t = "X"
    if m35 == "u":
        u = "X"
    if m35 == "v":
        v = "X"
    if m35 == "w":
        w = "X"
    if m35 == "x":
        x = "X"
    if m35 == "y":
        y = "X"
    if m35 == "z":
        z = "X"
    if m35 == "a1":
        a1 = "X"
    if m35 == "b1":
        b1 = "X"
    if m35 == "c1":
        c1 = "X"
    if m35 == "d1":
        d1 = "X"
    if m35 == "e1":
        e1 = "X"
    if m35 == "f1":
        f1 = "X"
    if m35 == "g1":
        g1 = "X"
    if m35 == "h1":
        h1 = "X"
    if m35 == "i1":
        i1 = "X"
    if m35 == "j1":
        j1 = "X"
    if m35 == "k1":
        k1 = "X"
    if m35 == "l1":
        l1 = "X"
    if m35 == "n1":
        n1 = "X"
    if m35 == "o1":
        o1 = "X"
    if m35 == "p1":
        p1 = "X"
    if m35 == "q1":
        q1 = "X"
    if m35 == "r1":
        r1 = "X"
    if m35 == "s1":
        s1 = "X"
    if m35 == "t1":
        t1 = "X"
    if m35 == "u1":
        u1 = "X"
    if m35 == "v1":
        v1 = "X"
    if m35 == "w1":
        w1 = "X"
    if m35 == "x1":
        x1 = "X"

    print("move 36")
    m36 = input()
    if m36 == "a":
        a = "O"
    if m36 == "b":
        b = "O"
    if m36 == "c":
        c = "O"
    if m36 == "d":
        d = "O"
    if m36 == "e":
        e = "O"
    if m36 == "f":
        f = "O"
    if m36 == "g":
        g = "O"
    if m36 == "h":
        h = "O"
    if m36 == "i":
        i = "O"
    if m36 == "j":
        j = "O"
    if m36 == "k":
        k = "O"
    if m36 == "l":
        l = "O"
    if m36 == "m":
        m = "O"
    if m36 == "n":
        n = "O"
    if m36 == "o":
        o = "O"
    if m36 == "p":
        p = "O"
    if m36 == "q":
        q = "O"
    if m36 == "r":
        r = "O"
    if m36 == "s":
        s = "O"
    if m36 == "t":
        t = "O"
    if m36 == "u":
        u = "O"
    if m36 == "v":
        v = "O"
    if m36 == "w":
        w = "O"
    if m36 == "x":
        x = "O"
    if m36 == "y":
        y = "O"
    if m36 == "z":
        z = "O"
    if m36 == "a1":
        a1 = "O"
    if m36 == "b1":
        b1 = "O"
    if m36 == "c1":
        c1 = "O"
    if m36 == "d1":
        d1 = "O"
    if m36 == "e1":
        e1 = "O"
    if m36 == "f1":
        f1 = "O"
    if m36 == "g1":
        g1 = "O"
    if m36 == "h1":
        h1 = "O"
    if m36 == "i1":
        i1 = "O"
    if m36 == "j1":
        j1 = "O"
    if m36 == "k1":
        k1 = "O"
    if m36 == "l1":
        l1 = "O"
    if m36 == "n1":
        n1 = "O"
    if m36 == "o1":
        o1 = "O"
    if m36 == "p1":
        p1 = "O"
    if m36 == "q1":
        q1 = "O"
    if m36 == "r1":
        r1 = "O"
    if m36 == "s1":
        s1 = "O"
    if m36 == "t1":
        t1 = "O"
    if m36 == "u1":
        u1 = "O"
    if m36 == "v1":
        v1 = "O"
    if m36 == "w1":
        w1 = "O"
    if m36 == "x1":
        x1 = "O"

    print("move 37")
    m37 = input()
    if m37 == "a":
        a = "X"
    if m37 == "b":
        b = "X"
    if m37 == "c":
        c = "X"
    if m37 == "d":
        d = "X"
    if m37 == "e":
        e = "X"
    if m37 == "f":
        f = "X"
    if m37 == "g":
        g = "X"
    if m37 == "h":
        h = "X"
    if m37 == "i":
        i = "X"
    if m37 == "j":
        j = "X"
    if m37 == "k":
        k = "X"
    if m37 == "l":
        l = "X"
    if m37 == "m":
        m = "X"
    if m37 == "n":
        n = "X"
    if m37 == "o":
        o = "X"
    if m37 == "p":
        p = "X"
    if m37 == "q":
        q = "X"
    if m37 == "r":
        r = "X"
    if m37 == "s":
        s = "X"
    if m37 == "t":
        t = "X"
    if m37 == "u":
        u = "X"
    if m37 == "v":
        v = "X"
    if m37 == "w":
        w = "X"
    if m37 == "x":
        x = "X"
    if m37 == "y":
        y = "X"
    if m37 == "z":
        z = "X"
    if m37 == "a1":
        a1 = "X"
    if m37 == "b1":
        b1 = "X"
    if m37 == "c1":
        c1 = "X"
    if m37 == "d1":
        d1 = "X"
    if m37 == "e1":
        e1 = "X"
    if m37 == "f1":
        f1 = "X"
    if m37 == "g1":
        g1 = "X"
    if m37 == "h1":
        h1 = "X"
    if m37 == "i1":
        i1 = "X"
    if m37 == "j1":
        j1 = "X"
    if m37 == "k1":
        k1 = "X"
    if m37 == "l1":
        l1 = "X"
    if m37 == "n1":
        n1 = "X"
    if m37 == "o1":
        o1 = "X"
    if m37 == "p1":
        p1 = "X"
    if m37 == "q1":
        q1 = "X"
    if m37 == "r1":
        r1 = "X"
    if m37 == "s1":
        s1 = "X"
    if m37 == "t1":
        t1 = "X"
    if m37 == "u1":
        u1 = "X"
    if m37 == "v1":
        v1 = "X"
    if m37 == "w1":
        w1 = "X"
    if m37 == "x1":
        x1 = "X"

    print("move 38")
    m38 = input()
    if m38 == "a":
        a = "O"
    if m38 == "b":
        b = "O"
    if m38 == "c":
        c = "O"
    if m38 == "d":
        d = "O"
    if m38 == "e":
        e = "O"
    if m38 == "f":
        f = "O"
    if m38 == "g":
        g = "O"
    if m38 == "h":
        h = "O"
    if m38 == "i":
        i = "O"
    if m38 == "j":
        j = "O"
    if m38 == "k":
        k = "O"
    if m38 == "l":
        l = "O"
    if m38 == "m":
        m = "O"
    if m38 == "n":
        n = "O"
    if m38 == "o":
        o = "O"
    if m38 == "p":
        p = "O"
    if m38 == "q":
        q = "O"
    if m38 == "r":
        r = "O"
    if m38 == "s":
        s = "O"
    if m38 == "t":
        t = "O"
    if m38 == "u":
        u = "O"
    if m38 == "v":
        v = "O"
    if m38 == "w":
        w = "O"
    if m38 == "x":
        x = "O"
    if m38 == "y":
        y = "O"
    if m38 == "z":
        z = "O"
    if m38 == "a1":
        a1 = "O"
    if m38 == "b1":
        b1 = "O"
    if m38 == "c1":
        c1 = "O"
    if m38 == "d1":
        d1 = "O"
    if m38 == "e1":
        e1 = "O"
    if m38 == "f1":
        f1 = "O"
    if m38 == "g1":
        g1 = "O"
    if m38 == "h1":
        h1 = "O"
    if m38 == "i1":
        i1 = "O"
    if m38 == "j1":
        j1 = "O"
    if m38 == "k1":
        k1 = "O"
    if m38 == "l1":
        l1 = "O"
    if m38 == "n1":
        n1 = "O"
    if m38 == "o1":
        o1 = "O"
    if m38 == "p1":
        p1 = "O"
    if m38 == "q1":
        q1 = "O"
    if m38 == "r1":
        r1 = "O"
    if m38 == "s1":
        s1 = "O"
    if m38 == "t1":
        t1 = "O"
    if m38 == "u1":
        u1 = "O"
    if m38 == "v1":
        v1 = "O"
    if m38 == "w1":
        w1 = "O"
    if m38 == "x1":
        x1 = "O"

    print("move 39")
    m39 = input()
    if m39 == "a":
        a = "X"
    if m39 == "b":
        b = "X"
    if m39 == "c":
        c = "X"
    if m39 == "d":
        d = "X"
    if m39 == "e":
        e = "X"
    if m39 == "f":
        f = "X"
    if m39 == "g":
        g = "X"
    if m39 == "h":
        h = "X"
    if m39 == "i":
        i = "X"
    if m39 == "j":
        j = "X"
    if m39 == "k":
        k = "X"
    if m39 == "l":
        l = "X"
    if m39 == "m":
        m = "X"
    if m39 == "n":
        n = "X"
    if m39 == "o":
        o = "X"
    if m39 == "p":
        p = "X"
    if m39 == "q":
        q = "X"
    if m39 == "r":
        r = "X"
    if m39 == "s":
        s = "X"
    if m39 == "t":
        t = "X"
    if m39 == "u":
        u = "X"
    if m39 == "v":
        v = "X"
    if m39 == "w":
        w = "X"
    if m39 == "x":
        x = "X"
    if m39 == "y":
        y = "X"
    if m39 == "z":
        z = "X"
    if m39 == "a1":
        a1 = "X"
    if m39 == "b1":
        b1 = "X"
    if m39 == "c1":
        c1 = "X"
    if m39 == "d1":
        d1 = "X"
    if m39 == "e1":
        e1 = "X"
    if m39 == "f1":
        f1 = "X"
    if m39 == "g1":
        g1 = "X"
    if m39 == "h1":
        h1 = "X"
    if m39 == "i1":
        i1 = "X"
    if m39 == "j1":
        j1 = "X"
    if m39 == "k1":
        k1 = "X"
    if m39 == "l1":
        l1 = "X"
    if m39 == "n1":
        n1 = "X"
    if m39 == "o1":
        o1 = "X"
    if m39 == "p1":
        p1 = "X"
    if m39 == "q1":
        q1 = "X"
    if m39 == "r1":
        r1 = "X"
    if m39 == "s1":
        s1 = "X"
    if m39 == "t1":
        t1 = "X"
    if m39 == "u1":
        u1 = "X"
    if m39 == "v1":
        v1 = "X"
    if m39 == "w1":
        w1 = "X"
    if m39 == "x1":
        x1 = "X"

    print("move 40")
    m40 = input()
    if m40 == "a":
        a = "O"
    if m40 == "b":
        b = "O"
    if m40 == "c":
        c = "O"
    if m40 == "d":
        d = "O"
    if m40 == "e":
        e = "O"
    if m40 == "f":
        f = "O"
    if m40 == "g":
        g = "O"
    if m40 == "h":
        h = "O"
    if m40 == "i":
        i = "O"
    if m40 == "j":
        j = "O"
    if m40 == "k":
        k = "O"
    if m40 == "l":
        l = "O"
    if m40 == "m":
        m = "O"
    if m40 == "n":
        n = "O"
    if m40 == "o":
        o = "O"
    if m40 == "p":
        p = "O"
    if m40 == "q":
        q = "O"
    if m40 == "r":
        r = "O"
    if m40 == "s":
        s = "O"
    if m40 == "t":
        t = "O"
    if m40 == "u":
        u = "O"
    if m40 == "v":
        v = "O"
    if m40 == "w":
        w = "O"
    if m40 == "x":
        x = "O"
    if m40 == "y":
        y = "O"
    if m40 == "z":
        z = "O"
    if m40 == "a1":
        a1 = "O"
    if m40 == "b1":
        b1 = "O"
    if m40 == "c1":
        c1 = "O"
    if m40 == "d1":
        d1 = "O"
    if m40 == "e1":
        e1 = "O"
    if m40 == "f1":
        f1 = "O"
    if m40 == "g1":
        g1 = "O"
    if m40 == "h1":
        h1 = "O"
    if m40 == "i1":
        i1 = "O"
    if m40 == "j1":
        j1 = "O"
    if m40 == "k1":
        k1 = "O"
    if m40 == "l1":
        l1 = "O"
    if m40 == "n1":
        n1 = "O"
    if m40 == "o1":
        o1 = "O"
    if m40 == "p1":
        p1 = "O"
    if m40 == "q1":
        q1 = "O"
    if m40 == "r1":
        r1 = "O"
    if m40 == "s1":
        s1 = "O"
    if m40 == "t1":
        t1 = "O"
    if m40 == "u1":
        u1 = "O"
    if m40 == "v1":
        v1 = "O"
    if m40 == "w1":
        w1 = "O"
    if m40 == "x1":
        x1 = "O"

    print("move 41")
    m41 = input()
    if m41 == "a":
        a = "X"
    if m41 == "b":
        b = "X"
    if m41 == "c":
        c = "X"
    if m41 == "d":
        d = "X"
    if m41 == "e":
        e = "X"
    if m41 == "f":
        f = "X"
    if m41 == "g":
        g = "X"
    if m41 == "h":
        h = "X"
    if m41 == "i":
        i = "X"
    if m41 == "j":
        j = "X"
    if m41 == "k":
        k = "X"
    if m41 == "l":
        l = "X"
    if m41 == "m":
        m = "X"
    if m41 == "n":
        n = "X"
    if m41 == "o":
        o = "X"
    if m41 == "p":
        p = "X"
    if m41 == "q":
        q = "X"
    if m41 == "r":
        r = "X"
    if m41 == "s":
        s = "X"
    if m41 == "t":
        t = "X"
    if m41 == "u":
        u = "X"
    if m41 == "v":
        v = "X"
    if m41 == "w":
        w = "X"
    if m41 == "x":
        x = "X"
    if m41 == "y":
        y = "X"
    if m41 == "z":
        z = "X"
    if m41 == "a1":
        a1 = "X"
    if m41 == "b1":
        b1 = "X"
    if m41 == "c1":
        c1 = "X"
    if m41 == "d1":
        d1 = "X"
    if m41 == "e1":
        e1 = "X"
    if m41 == "f1":
        f1 = "X"
    if m41 == "g1":
        g1 = "X"
    if m41 == "h1":
        h1 = "X"
    if m41 == "i1":
        i1 = "X"
    if m41 == "j1":
        j1 = "X"
    if m41 == "k1":
        k1 = "X"
    if m41 == "l1":
        l1 = "X"
    if m41 == "n1":
        n1 = "X"
    if m41 == "o1":
        o1 = "X"
    if m41 == "p1":
        p1 = "X"
    if m41 == "q1":
        q1 = "X"
    if m41 == "r1":
        r1 = "X"
    if m41 == "s1":
        s1 = "X"
    if m41 == "t1":
        t1 = "X"
    if m41 == "u1":
        u1 = "X"
    if m41 == "v1":
        v1 = "X"
    if m41 == "w1":
        w1 = "X"
    if m41 == "x1":
        x1 = "X"

    print("move 42")
    m42 = input()
    if m42 == "a":
        a = "O"
    if m42 == "b":
        b = "O"
    if m42 == "c":
        c = "O"
    if m42 == "d":
        d = "O"
    if m42 == "e":
        e = "O"
    if m42 == "f":
        f = "O"
    if m42 == "g":
        g = "O"
    if m42 == "h":
        h = "O"
    if m42 == "i":
        i = "O"
    if m42 == "j":
        j = "O"
    if m42 == "k":
        k = "O"
    if m42 == "l":
        l = "O"
    if m42 == "m":
        m = "O"
    if m42 == "n":
        n = "O"
    if m42 == "o":
        o = "O"
    if m42 == "p":
        p = "O"
    if m42 == "q":
        q = "O"
    if m42 == "r":
        r = "O"
    if m42 == "s":
        s = "O"
    if m42 == "t":
        t = "O"
    if m42 == "u":
        u = "O"
    if m42 == "v":
        v = "O"
    if m42 == "w":
        w = "O"
    if m42 == "x":
        x = "O"
    if m42 == "y":
        y = "O"
    if m42 == "z":
        z = "O"
    if m42 == "a1":
        a1 = "O"
    if m42 == "b1":
        b1 = "O"
    if m42 == "c1":
        c1 = "O"
    if m42 == "d1":
        d1 = "O"
    if m42 == "e1":
        e1 = "O"
    if m42 == "f1":
        f1 = "O"
    if m42 == "g1":
        g1 = "O"
    if m42 == "h1":
        h1 = "O"
    if m42 == "i1":
        i1 = "O"
    if m42 == "j1":
        j1 = "O"
    if m42 == "k1":
        k1 = "O"
    if m42 == "l1":
        l1 = "O"
    if m42 == "n1":
        n1 = "O"
    if m42 == "o1":
        o1 = "O"
    if m42 == "p1":
        p1 = "O"
    if m42 == "q1":
        q1 = "O"
    if m42 == "r1":
        r1 = "O"
    if m42 == "s1":
        s1 = "O"
    if m42 == "t1":
        t1 = "O"
    if m42 == "u1":
        u1 = "O"
    if m42 == "v1":
        v1 = "O"
    if m42 == "w1":
        w1 = "O"
    if m42 == "x1":
        x1 = "O"

    print("move 43")
    m43 = input()
    if m43 == "a":
        a = "X"
    if m43 == "b":
        b = "X"
    if m43 == "c":
        c = "X"
    if m43 == "d":
        d = "X"
    if m43 == "e":
        e = "X"
    if m43 == "f":
        f = "X"
    if m43 == "g":
        g = "X"
    if m43 == "h":
        h = "X"
    if m43 == "i":
        i = "X"
    if m43 == "j":
        j = "X"
    if m43 == "k":
        k = "X"
    if m43 == "l":
        l = "X"
    if m43 == "m":
        m = "X"
    if m43 == "n":
        n = "X"
    if m43 == "o":
        o = "X"
    if m43 == "p":
        p = "X"
    if m43 == "q":
        q = "X"
    if m43 == "r":
        r = "X"
    if m43 == "s":
        s = "X"
    if m43 == "t":
        t = "X"
    if m43 == "u":
        u = "X"
    if m43 == "v":
        v = "X"
    if m43 == "w":
        w = "X"
    if m43 == "x":
        x = "X"
    if m43 == "y":
        y = "X"
    if m43 == "z":
        z = "X"
    if m43 == "a1":
        a1 = "X"
    if m43 == "b1":
        b1 = "X"
    if m43 == "c1":
        c1 = "X"
    if m43 == "d1":
        d1 = "X"
    if m43 == "e1":
        e1 = "X"
    if m43 == "f1":
        f1 = "X"
    if m43 == "g1":
        g1 = "X"
    if m43 == "h1":
        h1 = "X"
    if m43 == "i1":
        i1 = "X"
    if m43 == "j1":
        j1 = "X"
    if m43 == "k1":
        k1 = "X"
    if m43 == "l1":
        l1 = "X"
    if m43 == "n1":
        n1 = "X"
    if m43 == "o1":
        o1 = "X"
    if m43 == "p1":
        p1 = "X"
    if m43 == "q1":
        q1 = "X"
    if m43 == "r1":
        r1 = "X"
    if m43 == "s1":
        s1 = "X"
    if m43 == "t1":
        t1 = "X"
    if m43 == "u1":
        u1 = "X"
    if m43 == "v1":
        v1 = "X"
    if m43 == "w1":
        w1 = "X"
    if m43 == "x1":
        x1 = "X"

    print("move 44")
    m44 = input()
    if m44 == "a":
        a = "O"
    if m44 == "b":
        b = "O"
    if m44 == "c":
        c = "O"
    if m44 == "d":
        d = "O"
    if m44 == "e":
        e = "O"
    if m44 == "f":
        f = "O"
    if m44 == "g":
        g = "O"
    if m44 == "h":
        h = "O"
    if m44 == "i":
        i = "O"
    if m44 == "j":
        j = "O"
    if m44 == "k":
        k = "O"
    if m44 == "l":
        l = "O"
    if m44 == "m":
        m = "O"
    if m44 == "n":
        n = "O"
    if m44 == "o":
        o = "O"
    if m44 == "p":
        p = "O"
    if m44 == "q":
        q = "O"
    if m44 == "r":
        r = "O"
    if m44 == "s":
        s = "O"
    if m44 == "t":
        t = "O"
    if m44 == "u":
        u = "O"
    if m44 == "v":
        v = "O"
    if m44 == "w":
        w = "O"
    if m44 == "x":
        x = "O"
    if m44 == "y":
        y = "O"
    if m44 == "z":
        z = "O"
    if m44 == "a1":
        a1 = "O"
    if m44 == "b1":
        b1 = "O"
    if m44 == "c1":
        c1 = "O"
    if m44 == "d1":
        d1 = "O"
    if m44 == "e1":
        e1 = "O"
    if m44 == "f1":
        f1 = "O"
    if m44 == "g1":
        g1 = "O"
    if m44 == "h1":
        h1 = "O"
    if m44 == "i1":
        i1 = "O"
    if m44 == "j1":
        j1 = "O"
    if m44 == "k1":
        k1 = "O"
    if m44 == "l1":
        l1 = "O"
    if m44 == "n1":
        n1 = "O"
    if m44 == "o1":
        o1 = "O"
    if m44 == "p1":
        p1 = "O"
    if m44 == "q1":
        q1 = "O"
    if m44 == "r1":
        r1 = "O"
    if m44 == "s1":
        s1 = "O"
    if m44 == "t1":
        t1 = "O"
    if m44 == "u1":
        u1 = "O"
    if m44 == "v1":
        v1 = "O"
    if m44 == "w1":
        w1 = "O"
    if m44 == "x1":
        x1 = "O"

    print("move 45")
    m45 = input()
    if m45 == "a":
        a = "X"
    if m45 == "b":
        b = "X"
    if m45 == "c":
        c = "X"
    if m45 == "d":
        d = "X"
    if m45 == "e":
        e = "X"
    if m45 == "f":
        f = "X"
    if m45 == "g":
        g = "X"
    if m45 == "h":
        h = "X"
    if m45 == "i":
        i = "X"
    if m45 == "j":
        j = "X"
    if m45 == "k":
        k = "X"
    if m45 == "l":
        l = "X"
    if m45 == "m":
        m = "X"
    if m45 == "n":
        n = "X"
    if m45 == "o":
        o = "X"
    if m45 == "p":
        p = "X"
    if m45 == "q":
        q = "X"
    if m45 == "r":
        r = "X"
    if m45 == "s":
        s = "X"
    if m45 == "t":
        t = "X"
    if m45 == "u":
        u = "X"
    if m45 == "v":
        v = "X"
    if m45 == "w":
        w = "X"
    if m45 == "x":
        x = "X"
    if m45 == "y":
        y = "X"
    if m45 == "z":
        z = "X"
    if m45 == "a1":
        a1 = "X"
    if m45 == "b1":
        b1 = "X"
    if m45 == "c1":
        c1 = "X"
    if m45 == "d1":
        d1 = "X"
    if m45 == "e1":
        e1 = "X"
    if m45 == "f1":
        f1 = "X"
    if m45 == "g1":
        g1 = "X"
    if m45 == "h1":
        h1 = "X"
    if m45 == "i1":
        i1 = "X"
    if m45 == "j1":
        j1 = "X"
    if m45 == "k1":
        k1 = "X"
    if m45 == "l1":
        l1 = "X"
    if m45 == "n1":
        n1 = "X"
    if m45 == "o1":
        o1 = "X"
    if m45 == "p1":
        p1 = "X"
    if m45 == "q1":
        q1 = "X"
    if m45 == "r1":
        r1 = "X"
    if m45 == "s1":
        s1 = "X"
    if m45 == "t1":
        t1 = "X"
    if m45 == "u1":
        u1 = "X"
    if m45 == "v1":
        v1 = "X"
    if m45 == "w1":
        w1 = "X"
    if m45 == "x1":
        x1 = "X"

    print("move 46")
    m46 = input()
    if m46 == "a":
        a = "O"
    if m46 == "b":
        b = "O"
    if m46 == "c":
        c = "O"
    if m46 == "d":
        d = "O"
    if m46 == "e":
        e = "O"
    if m46 == "f":
        f = "O"
    if m46 == "g":
        g = "O"
    if m46 == "h":
        h = "O"
    if m46 == "i":
        i = "O"
    if m46 == "j":
        j = "O"
    if m46 == "k":
        k = "O"
    if m46 == "l":
        l = "O"
    if m46 == "m":
        m = "O"
    if m46 == "n":
        n = "O"
    if m46 == "o":
        o = "O"
    if m46 == "p":
        p = "O"
    if m46 == "q":
        q = "O"
    if m46 == "r":
        r = "O"
    if m46 == "s":
        s = "O"
    if m46 == "t":
        t = "O"
    if m46 == "u":
        u = "O"
    if m46 == "v":
        v = "O"
    if m46 == "w":
        w = "O"
    if m46 == "x":
        x = "O"
    if m46 == "y":
        y = "O"
    if m46 == "z":
        z = "O"
    if m46 == "a1":
        a1 = "O"
    if m46 == "b1":
        b1 = "O"
    if m46 == "c1":
        c1 = "O"
    if m46 == "d1":
        d1 = "O"
    if m46 == "e1":
        e1 = "O"
    if m46 == "f1":
        f1 = "O"
    if m46 == "g1":
        g1 = "O"
    if m46 == "h1":
        h1 = "O"
    if m46 == "i1":
        i1 = "O"
    if m46 == "j1":
        j1 = "O"
    if m46 == "k1":
        k1 = "O"
    if m46 == "l1":
        l1 = "O"
    if m46 == "n1":
        n1 = "O"
    if m46 == "o1":
        o1 = "O"
    if m46 == "p1":
        p1 = "O"
    if m46 == "q1":
        q1 = "O"
    if m46 == "r1":
        r1 = "O"
    if m46 == "s1":
        s1 = "O"
    if m46 == "t1":
        t1 = "O"
    if m46 == "u1":
        u1 = "O"
    if m46 == "v1":
        v1 = "O"
    if m46 == "w1":
        w1 = "O"
    if m46 == "x1":
        x1 = "O"

    print("move 47")
    m47 = input()
    if m47 == "a":
        a = "X"
    if m47 == "b":
        b = "X"
    if m47 == "c":
        c = "X"
    if m47 == "d":
        d = "X"
    if m47 == "e":
        e = "X"
    if m47 == "f":
        f = "X"
    if m47 == "g":
        g = "X"
    if m47 == "h":
        h = "X"
    if m47 == "i":
        i = "X"
    if m47 == "j":
        j = "X"
    if m47 == "k":
        k = "X"
    if m47 == "l":
        l = "X"
    if m47 == "m":
        m = "X"
    if m47 == "n":
        n = "X"
    if m47 == "o":
        o = "X"
    if m47 == "p":
        p = "X"
    if m47 == "q":
        q = "X"
    if m47 == "r":
        r = "X"
    if m47 == "s":
        s = "X"
    if m47 == "t":
        t = "X"
    if m47 == "u":
        u = "X"
    if m47 == "v":
        v = "X"
    if m47 == "w":
        w = "X"
    if m47 == "x":
        x = "X"
    if m47 == "y":
        y = "X"
    if m47 == "z":
        z = "X"
    if m47 == "a1":
        a1 = "X"
    if m47 == "b1":
        b1 = "X"
    if m47 == "c1":
        c1 = "X"
    if m47 == "d1":
        d1 = "X"
    if m47 == "e1":
        e1 = "X"
    if m47 == "f1":
        f1 = "X"
    if m47 == "g1":
        g1 = "X"
    if m47 == "h1":
        h1 = "X"
    if m47 == "i1":
        i1 = "X"
    if m47 == "j1":
        j1 = "X"
    if m47 == "k1":
        k1 = "X"
    if m47 == "l1":
        l1 = "X"
    if m47 == "n1":
        n1 = "X"
    if m47 == "o1":
        o1 = "X"
    if m47 == "p1":
        p1 = "X"
    if m47 == "q1":
        q1 = "X"
    if m47 == "r1":
        r1 = "X"
    if m47 == "s1":
        s1 = "X"
    if m47 == "t1":
        t1 = "X"
    if m47 == "u1":
        u1 = "X"
    if m47 == "v1":
        v1 = "X"
    if m47 == "w1":
        w1 = "X"
    if m47 == "x1":
        x1 = "X"

    print("move 48")
    m48 = input()
    if m48 == "a":
        a = "O"
    if m48 == "b":
        b = "O"
    if m48 == "c":
        c = "O"
    if m48 == "d":
        d = "O"
    if m48 == "e":
        e = "O"
    if m48 == "f":
        f = "O"
    if m48 == "g":
        g = "O"
    if m48 == "h":
        h = "O"
    if m48 == "i":
        i = "O"
    if m48 == "j":
        j = "O"
    if m48 == "k":
        k = "O"
    if m48 == "l":
        l = "O"
    if m48 == "m":
        m = "O"
    if m48 == "n":
        n = "O"
    if m48 == "o":
        o = "O"
    if m48 == "p":
        p = "O"
    if m48 == "q":
        q = "O"
    if m48 == "r":
        r = "O"
    if m48 == "s":
        s = "O"
    if m48 == "t":
        t = "O"
    if m48 == "u":
        u = "O"
    if m48 == "v":
        v = "O"
    if m48 == "w":
        w = "O"
    if m48 == "x":
        x = "O"
    if m48 == "y":
        y = "O"
    if m48 == "z":
        z = "O"
    if m48 == "a1":
        a1 = "O"
    if m48 == "b1":
        b1 = "O"
    if m48 == "c1":
        c1 = "O"
    if m48 == "d1":
        d1 = "O"
    if m48 == "e1":
        e1 = "O"
    if m48 == "f1":
        f1 = "O"
    if m48 == "g1":
        g1 = "O"
    if m48 == "h1":
        h1 = "O"
    if m48 == "i1":
        i1 = "O"
    if m48 == "j1":
        j1 = "O"
    if m48 == "k1":
        k1 = "O"
    if m48 == "l1":
        l1 = "O"
    if m48 == "n1":
        n1 = "O"
    if m48 == "o1":
        o1 = "O"
    if m48 == "p1":
        p1 = "O"
    if m48 == "q1":
        q1 = "O"
    if m48 == "r1":
        r1 = "O"
    if m48 == "s1":
        s1 = "O"
    if m48 == "t1":
        t1 = "O"
    if m48 == "u1":
        u1 = "O"
    if m48 == "v1":
        v1 = "O"
    if m48 == "w1":
        w1 = "O"
    if m48 == "x1":
        x1 = "O"

    print("move 49")
    m49 = input()
    if m49 == "a":
        a = "X"
    if m49 == "b":
        b = "X"
    if m49 == "c":
        c = "X"
    if m49 == "d":
        d = "X"
    if m49 == "e":
        e = "X"
    if m49 == "f":
        f = "X"
    if m49 == "g":
        g = "X"
    if m49 == "h":
        h = "X"
    if m49 == "i":
        i = "X"
    if m49 == "j":
        j = "X"
    if m49 == "k":
        k = "X"
    if m49 == "l":
        l = "X"
    if m49 == "m":
        m = "X"
    if m49 == "n":
        n = "X"
    if m49 == "o":
        o = "X"
    if m49 == "p":
        p = "X"
    if m49 == "q":
        q = "X"
    if m49 == "r":
        r = "X"
    if m49 == "s":
        s = "X"
    if m49 == "t":
        t = "X"
    if m49 == "u":
        u = "X"
    if m49 == "v":
        v = "X"
    if m49 == "w":
        w = "X"
    if m49 == "x":
        x = "X"
    if m49 == "y":
        y = "X"
    if m49 == "z":
        z = "X"
    if m49 == "a1":
        a1 = "X"
    if m49 == "b1":
        b1 = "X"
    if m49 == "c1":
        c1 = "X"
    if m49 == "d1":
        d1 = "X"
    if m49 == "e1":
        e1 = "X"
    if m49 == "f1":
        f1 = "X"
    if m49 == "g1":
        g1 = "X"
    if m49 == "h1":
        h1 = "X"
    if m49 == "i1":
        i1 = "X"
    if m49 == "j1":
        j1 = "X"
    if m49 == "k1":
        k1 = "X"
    if m49 == "l1":
        l1 = "X"
    if m49 == "n1":
        n1 = "X"
    if m49 == "o1":
        o1 = "X"
    if m49 == "p1":
        p1 = "X"
    if m49 == "q1":
        q1 = "X"
    if m49 == "r1":
        r1 = "X"
    if m49 == "s1":
        s1 = "X"
    if m49 == "t1":
        t1 = "X"
    if m49 == "u1":
        u1 = "X"
    if m49 == "v1":
        v1 = "X"
    if m49 == "w1":
        w1 = "X"
    if m49 == "x1":
        x1 = "X"

    # Displays final board
    print("|---|---|---|---|---|---|---|")
    print("|", a, "|", b, "|", c, "|", d, "|", e, "|", f, "|", g, "|")
    print("|---|---|---|---|---|---|---|")
    print("|", h, "|", i, "|", j, "|", k, "|", l, "|", m, "|", n, "|")
    print("|---|---|---|---|---|---|---|")
    print("|", o, "|", p, "|", q, "|", r, "|", s, "|", t, "|", u, "|")
    print("|---|---|---|---|---|---|---|")
    print("|", v, "|", w, "|", x, "|", y, "|", z, "|", a1, "|", b1, "|")
    print("|---|---|---|---|---|---|---|")
    print("|", c1, "|", d1, "|", e1, "|", f1, "|", g1, "|", h1, "|", i1, "|")
    print("|---|---|---|---|---|---|---|")
    print("|", j1, "|", k1, "|", l1, "|", m1, "|", n1, "|", o1, "|", p1, "|")


myButton1 = Button(root, text="3x3", command=myClick1, fg="white", bg="black", padx=50, pady=3)
myButton1.pack()

myButton2 = Button(root, text="5x5", command=myClick2, fg="white", bg="black", padx=50, pady=3)
myButton2.pack()

myButton3 = Button(root, text="7x7", command=myClick3, fg="white", bg="black", padx=50, pady=3)
myButton3.pack()

root.mainloop()