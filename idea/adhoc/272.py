from sys import stdin

switch = 1
while True:
    try:
        line = input()
    except EOFError:
        break
    s = ""
    for c in line:
        if c == "\"":
            if switch:
                c = "``"
                switch = 0
            else:
                c = "''"
                switch = 1
        s += c
    print(s)
