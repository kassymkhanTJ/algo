for _ in range(int(input())):
    a, b = list(map(int, input().strip().split(' ')))
    if a < b:
        print("<")
    elif a > b:
        print(">")
    else:
        print("=")

