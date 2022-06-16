def is_3square(n):
    T = {1, 2, 5, 10, 13, 25, 37, 58, 85, 130}
    while n > 0 and n % 4 == 0:

        n /= 4

    if n in T:
        return False
    if n % 8 == 7:
        return False
    return True

seq = list(eval(input()))
seq = set(seq)
cnt = 0
for i in seq:
    if is_3square(i):
        cnt = cnt + 1

print(cnt)



