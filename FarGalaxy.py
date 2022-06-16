
x = []
y = []
z = []
c = {}
i = input()
while ' ' in i:
    a = i.split()
    a[0] = float(a[0])
    a[1] = float(a[1])
    a[2] = float(a[2])
    c[tuple(a[:3])] = a[3]
    x.append(a[0])
    y.append(a[1])
    z.append(a[2])
    i = input()

x = sorted(x)
y = sorted(y)
z = sorted(z)

print(x)
print(y)
print(z)
name1 = ""
name2 = ""

for i in c:
    if (x[0] in i and y[0] in i) or (y[0] in i and z[0] in i) or (x[0] in i and z[0] in i):
        name1 = c[i]
    if (x[len(c) - 1] in i and y[len(c) - 1] in i) or (y[len(c) - 1] in i and z[len(c) - 1] in i) or (x[len(c) - 1] in i and z[len(c) - 1] in i):
        name2 = c[i]

if name1 < name2:
    print(name1 + ' ' + name2)
else:
    print(name2 + ' ' + name1)




