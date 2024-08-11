#3
f = open('24_2.txt')
s = f.readline()
count = 0
for i in range(len(s) - 1):
    first = str(ord(s[i]))
    second = str(ord(s[i + 1]))
    what = first + second
    flag = 0
    for j in range(len(what) // 2):
        if what[j] != what[len(what) - 1 - j]:
            flag = 1
    if flag == 0:
        count += 1
print(count)
