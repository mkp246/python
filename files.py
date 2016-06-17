f = open('wasteland.txt', 'wt', encoding='utf-8')
print(f.write('What RE ROOTS THAT CLUTCH'))
print(f.write(', what branches grow\n'))
print(f.write('Out of this rubbish story'))
f.close()

f = open('wasteland.txt', 'rt', encoding='utf-8')
print(f.read(32))
print(f.read())
print(f.read())
f.seek(0)
print(f.read())
f.seek(0)
print(f.readline())
print("line 1 done")
print(f.readline())
print(f.readline())
f.seek(0)
l = f.readlines()
print(l)
f.close()

f = open('wasteland.txt', 'at', encoding='utf-8')
f.writelines([
    '\nA woman is like a tea bag - you can\'t tell how '\
    'strong she is until you put her in hot water',
    'For every good reason there is to lie, '\
    'there is a better reason to tell the truth\n',
    'Manners is the key thing. Say, for instance, '\
    'when you\'re walking down the street, you\'ve '\
    'got to tell everybody good morning. Everybody. '\
    'You can\'t pass pne person\n'
])

print('='*98)
import sys
f = open('wasteland.txt', 'rt', encoding='utf-8')
for line in f:
    sys.stdout.write(line) # print(line) # strip can be done to remove extra lines
f.close()


