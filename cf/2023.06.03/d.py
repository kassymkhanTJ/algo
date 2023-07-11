import sys

mn = 1
mx = 10 ** 6 + 1
while mx - mn > 1:
    g = (mx + mn) // 2
    print(g)
    sys.stdout.flush()
    inp = input().strip()
    if inp == '<':
        mx = g
    else:
        mn = g
if inp == '<':
    g -= 1
print(f"! {g}")
sys.stdout.flush()