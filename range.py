r = range(5)
print(r)
for i in r:
    print(i)
r = range(5, 10)
for i in r:
    print(i)
print(list(range(5, 15, 2)))
s = [0, 1, 4, 6, 10]
for i in range(len(s)):  # bad
    print(s[i])
for v in s:  # good
    print(v)
for p in enumerate(s):
    print('index = {}, value = {}'.format(p[0], p[1]))
for (i, v) in enumerate(s):
    print('index = {}, value = {}'.format(i, v))
