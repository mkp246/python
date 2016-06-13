s = "show how to index into sequences".split()
print(s)
print(s[4])
print(s[-1])
for i in range(- len(s), -1):
    print(s[i])
print(s[1:3])
print(s[1:-1])
print(s[3:])
print(s[:3])
full_slice = s[:]
print('id same: ', s is full_slice,' value same: ', s == full_slice)

print(s.copy()) #shallow copy eg poing to same contained obj ref
c = s.copy();c[1]='daddy'
print(list(s)) #shallow copy eg poing to same contained obj ref
print(list(c))
print([0]*11)
s = [[-1,+1]] *5
print(s)
s[3].append(7) # reference only copy nt the data+
print(s)
w = "the quick brown fox jumps over lazy dog".split()
try:
    i = w.index('foxd')
except ValueError:
    i = -1
print('index : {}'.format(i))
u = 'jackdaws love my big sphinx of quartz'.split()
print(u)
del u[3]
print(u)
u.remove('love')
print(u)
del u[u.index('my')]
print(u)
m = [2, 3]
n = [4, 5]
k = m + n
print(k)
k += [9, 4, 645]
print(k)
k.extend([32, 543, 54, 99]) # work for any iterable
print(k)
k.reverse()
print(k)
k.sort()
print(k)
k.sort(reverse=True)
print(k)
k.sort(reverse=False)
print(k)
# if don't want to modify use sorted(list) >> returns list
# or reversed(list) >> returns only iterator
print(type(reversed(k)))
print(list(reversed(k)))



