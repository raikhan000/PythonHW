def mostPopular(arr):
    popular_index = 0
    cnt = 1
    for i in range(len(arr)):
        if arr[popular_index] == arr[i]:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            popular_index = i
            cnt = 1
    return arr[popular_index]

arr = []
while True:
    c = input()
    if c == '':
        break
    arr.append(c)

print(mostPopular(arr))

