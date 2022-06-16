def num_of_rect(array):
    num = 0
    for i in range(len(array) - 1):
        for j in range(len(array[i]) - 1):
            if array[i][j] == '#':
                if array[i][j + 1] == '.' and array[i + 1][j] == '.' and array[i + 1][j + 1] == '.':
                    num += 1
    return num

inputString = input()
length = len(inputString)
array = []
inputString = input()
while inputString != '-'*length:
    array.append(list(inputString))
    inputString = input()
array.append(['.' for elem in str] + ['.'])

print(num_of_rect(array))

