p = {6, 23, 53, 8812, 423423}
print(p)
print(type(p))
print(type({}))
print(type(set()))
s = [2, 1, 34, 5, 2, 7, 2, 3, 8, 6, 9]
print(len(s))
t = set(s)
print(len(t))
for x in t:
    print(x)
t.add(54)
print(t)
t.add(54)  # no error but not added
t.update([32, 7, 9])  # for multiple add
print(t)
try:
    t.discard(98)  # no err if not found
    t.remove(98)  # key error in not found
except KeyError:
    print('not found')
# copy and new set are shallow copy
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}
print('blue or blond', blue_eyes.union(blond_hair))
print('blue and blond', blue_eyes.intersection(blond_hair))
print('not blue and blond', blond_hair.difference(blue_eyes)) # non communicative
print('either blue or blond not both', blond_hair.symmetric_difference(blue_eyes) )
print('hcn sub of blond :', smell_hcn.issubset(blond_hair))
print('ptc super of hcn :', taste_ptc.issuperset(smell_hcn))
print('ptc super of hcn :', taste_ptc.issuperset(smell_hcn))
print('o and b', o_blood.isdisjoint(b_blood))
