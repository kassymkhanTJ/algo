from collections import deque

d = {}
k = int(input().strip())
expected = {
    "containsin": {")", "or", "and"},
    "contains": {")", "or"},
    "}": {")", "or", "containsin"},
    "and": {"("}
}
for _ in range(k):
    s = input().strip().replace(" ", "")
    l = []
    for i in range(len(s))
        if s[i] == '{':
            tmps = '{'
            while s[i] != '}':
                tmps += s[i]
                i += 1
            tmps += '}'
            l.append(tmps)
        elif s[i] == '[':
            tmps = '['
            while s[i] != ']':
                tmps += s[i]
                i += 1
            tmps += ']'
            l.append(tmps)
        elif s[i] == '(':
            tmps = '('
            while s[i] != ')':
                tmps += s[i]
                i += 1
            tmps += ')'
            l.append(tmps)
        else:

