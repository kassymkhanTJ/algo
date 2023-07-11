for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    Set = set()
    for i in range(n - 1):
        Set.add(s[i: i + 2])
    print(len(Set))