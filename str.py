lx = len('llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch')
print(lx)
print(("new"+"found"+"land").capitalize())
# using += for concat cause memory overuse in temps
# use join

print(';'.join(['hello','world']))
print(''.join(['high','way','man']))

part = "unforgetable".partition('forget')
print(part)
origin, _, destination = "Seattable-Boston".partition('-')
print('origin: {}, destination: {}'.format(origin, destination))
print("The age of {0} is {1}. {0}'s birthday is on {2}".format('jim', 24, 'october 31'))
# can omit numbering if used only once in order
# also keyword can be used if instead of number keyword params are used to format
print('Current position {lat} {lon}'.format(lat='60N', lon ='30E'))
pos = (65.3, 43.8, 99.9)
print("galactic Position x ={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos))
import math
print('Math constant : pi={math.pi:.3f}, e={math.e:.4f}'.format(math=math))
print('{c:.2f}'.format(c=32.76123478))
