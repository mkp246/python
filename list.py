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