import re

with open('input.txt', 'r') as f, open('output.txt', 'w') as rf:
    n = int(f.readline().strip())
    plane = []
    for _ in range(n):
        plane.append(f.readline().strip())
    n = int(f.readline().strip())
    for _ in range(n):
        num, pos, wish = f.readline().strip().split(' ')
        num = int(num)
        if pos == 'left':
            if wish == 'aisle':
                s, r, seat = '(%s)(%s)(%s)' % (('.' * (3 - num)), ('\.' * num), '_...'), fr'\1{"X" * num}\3', 'ABC'[
                                                                                                              3 - num:]
            else:
                s, r, seat = '(%s)(%s)(%s)' % (('\.' * num), ('.' * (3 - num)), '_...'), fr'{"X" * num}\2\3', 'ABC'[
                                                                                                              0:num]
        else:
            if wish == 'aisle':
                s, r, seat = '(%s)(%s)(%s)' % ('..._', ('\.' * num), ('.' * (3 - num))), fr'\1{"X" * num}\3', 'DEF'[
                                                                                                              0:num]
            else:
                s, r, seat = '(%s)(%s)(%s)' % ('..._', ('.' * (3 - num)), ('\.' * num)), fr'\1\2{"X" * num}', 'DEF'[
                                                                                                              3 - num:]
        for i in range(len(plane)):
            s = re.compile(s)
            res = re.match(s, plane[i])
            if res:
                plane[i] = re.sub(s, r, plane[i])
                rf.write('Passengers can take seats: %s\n' % ' '.join(f'{i + 1}{seat_num}' for seat_num in seat))
                rf.write('\n'.join(plane))
                rf.write('\n')
                plane[i] = plane[i].replace('X', '#')
                break
        else:
            rf.write('Cannot fulfill passengers requirements\n')
s = """Passengers can take seats: 1B 1C
.XX_.#.
.##_...
.#._.##
..._...
Passengers can take seats: 2D 2E 2F
.##_.#.
.##_XXX
.#._.##
..._...
Passengers can take seats: 4A 4B
.##_.#.
.##_###
.#._.##
XX._...
Cannot fulfill passengers requirements
Passengers can take seats: 1F
.##_.#X
.##_###
.#._.##
##._...
Passengers can take seats: 4E 4F
.##_.##
.##_###
.#._.##
##._.XX
Cannot fulfill passengers requirements
"""
for s1, s2 in zip(open('output.txt', 'r'), s.split("\n")):
    print(s1.strip() == s2.strip())