s1 = "first " "second"
print(s1)
s2 = """this is 
a multiline \/ "''
string"""
print(s2)
k = 'a \\ is string'
print(k)
path = r'C:\Angular Training\practice\python'
print(path)
print(str(234))
print(str(234.423e43))
print(str(234)[2])
c = 'oslO'
print(c.capitalize())
print(c)
print('\xe5')
list1 = [1, 2, 3]
list2 =['car', 'cd', 7]

print(list1.append(True), list2)
print(list1)
print(list('character'))
print('===================')
d = {'alice': '88-88', 'bob': '234325', 'eve': '42423-4312'}
print(d['alice'])
d['alice']='65923'
print(d['alice'])

cities = ["london", "paris", "new yark" ,"oslo", "Henska"]
for city in cities:
	print(city)

for name in d:
	print(name, d[name])
