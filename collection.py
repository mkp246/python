t = ('norway', 4.5, 45)
print(t)
for i in t:
	print(i)
print("length :",len(t))
t += (32,'youth')
print(t)
print(t*2)

a =((220,33),(1133,456),(3432,543),('bla','2adm'),['hello', "me"])
print(a)
print(a[2][1])
h =(328)
print(type(h))
h= (328,)
print(type(h))
h =()
print(type(h))


def minmax(items):
	return min(items), max(items)


mx = minmax([43,88,32,69,89,21])
print(mx)
(low,up)= mx
print(low,up)

(a,(b,(c,d)))=(4,(3,(2,1)))
print(a,b,c,d)

a= 'john';b='jack'
print(a,b)
a,b = b,a
print(a,b)
print(tuple("carmichael"))
print(5 in (4,5,63))
print(6 not in (4,5,63))

