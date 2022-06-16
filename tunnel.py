def tunnel(start,end):
    been = {start}
    if end not in c or start not in c:
        return False
    while end not in c[start]:
        start_list = c[start]
        a = [c[i] for i in start_list]
        a = set().union(*a)
        m = a & been
        a = a - m
        if end in a:
            return True
        if a.issubset(been) :
            return False
        else:
            start = list(a)[0]
            been.add(start)
    return True

c = {}
i = input()
while ' ' in i:
    a = i.split()
    try:
        c[a[0]].add(a[1])
        c[a[1]].add(a[0])
    except KeyError:
        if a[0] not in c:
            c[a[0]] = set(a[1].split())
        if a[1] not in c:
            c[a[1]] = set(a[0].split())
    i = input()
start = i
end = input()
if tunnel(start,end):
    print("YES")
else:
    print("NO")
