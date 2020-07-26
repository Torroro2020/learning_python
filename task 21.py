a = [int(i) for i in input().split()]
a.sort()
new_a = []
if len(a) > 1:
    for i in a:
        if a.count(i) > 1 and i not in new_a:
            new_a += [i]
    print(*new_a)
else:
    print()

