
def num_of_rect(index_i, index_j, array):
    while array[index_i][index_j] == '#':
        index_j = index_j + 1
        if index_j == len(array[index_i]):
            break

    if index_j != len(array[index_i]):
        index_j = index_j - 1
    while array[index_i][index_j] == '#' :
        index_i = index_i + 1
        if index_i == len(array):
            break
    if index_i != len(array):
        index_i = index_i - 1
    s = [index_i, index_j]
    return s

cnt = 0
inputString = input()
length = len(inputString)
array = []
inputString = input()
while inputString != '-'*length:
    array.append(list(inputString))
    inputString = input()

coord = []
for i in range(len(array)):
    if '#' in array[i]:
        first_index = array[i].index('#')
        j = num_of_rect(i, first_index, array)
        if j not in coord:
            coord.append(j.copy())
        array[i].reverse()
        last_j_index = length - array[i].index('#')
        array[i].reverse()
        while j[1] != last_j_index:
            cnt = cnt + 1
            j[1] = j[1] + 1
            if array[i][j[1]] == '#':
                s = num_of_rect(i, j[1], array)
                if s not in coord:
                    coord.append(s.copy())
        j[1] = j[1] - cnt
        cnt = 0

print(len(coord))










