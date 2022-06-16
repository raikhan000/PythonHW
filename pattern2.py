def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

inp = input()
s = input()
if '@' in s:
    flag = 1
    a = s.split('@')
    a = list(filter(('').__ne__, a))

    if len(a) == 0:
        print('0')
    if all([i in inp for i in a]) and len(inp) > len(s):
        count_missing_letters = []
        cnt = 0
        k = 0
        if s[0] != '@':
            k = 1
        for i in range(len(s)):
            if s[i] == '@':
                cnt = cnt + 1
            else:
                if cnt != 0:
                    count_missing_letters.append(cnt)
                cnt = 0
            k = k  + 1
        if len(a)> 1:
            flag2 = 0
            how_many_starts = inp.count(a[0])
            if how_many_starts > 2808:
                print(how_many_starts)
            n = 1
            r = 0
            k = 0

            for i in range(how_many_starts):

                if flag2 == 1:
                    break
                location_of_str1 = find_nth(inp, a[0], n)
                loc = location_of_str1 + len(a[0]) + count_missing_letters[0]
                if (s[0] == '@'):
                    r = 1
                    loc = location_of_str1 + len(a[0]) +count_missing_letters[1]

                for j in range(1,len(a)):
                    k = j + r
                    if inp[loc :loc + len(a[j])] == a[j]:
                        if k < len(count_missing_letters):
                            loc = loc + len(a[j]) + count_missing_letters[k]
                        flag2 = 1


                    else:
                        flag2 = 0
                        n = n + 1
                        break
            if flag2 == 1:
                if loc <= len(inp):
                    if s[0] == '@':
                        print(find_nth(inp, a[0], n) - count_missing_letters[0])
                    else:
                        print(find_nth(inp, a[0], n))
                else:
                    print('-1')


            if flag2 == 0:
                print('-1')

        elif len(a) == 1:
            if s[0] == '@':
                shift = len(count_missing_letters)
                if shift == 2:
                    if inp.find(a[0])+count_missing_letters[1] <= len(inp):
                        print(inp.find(a[0])-count_missing_letters[0])
                    else:
                        print('-1')
                else:
                    print(inp.find(a[0]) - count_missing_letters[0])
            else:
                if inp.find(a[0]) + count_missing_letters[0] <= len(inp):
                    print(inp.find(a[0]))
                else:
                    print('-1')

    else:
        print('-1')

elif s in inp:
    print(inp.find(s))
elif s not in inp:
    print('-1')
