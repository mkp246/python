words = "Why sometime I have believed as six impossible" \
        "things before breakfast".split()
print(words)
print(list(len(word) for word in words))
# exp(item) for item in list
# eg. eq. without comprehension
lengths =[]
for word in words:
    lengths.append(len(word))

print(lengths)
from math import factorial as fact
f = [len(str(fact(x))) for x in range(20)] # list has duplicate
print(f)
print(type(f))
f ={len(str(fact(x))) for x in range(20)} # no duplicate as set
print(f)
print(type(f))
from pprint import pprint as pp
country_to_cap = {'UK': 'London',
                  'Brazil': 'Brazilia',
                  'Morocco': 'Rabat',
                  'Sweden': 'Stockholm'
                  }
cap_to_country = {capital: country for country, capital in country_to_cap.items()}
pp(cap_to_country)
print(type(cap_to_country))
words = ['hi', 'hello', 'foxtrot', 'hotel'] # overwrites later entry with same keys
wd = {w[0]:w for w in words}
pp(wd)

import os, glob
file_sizes = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob('*.py')}
pp(file_sizes)

from  math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)+1)):
        if x%i == 0:
            return False
    return True
# filtering
primes = [x for x in range(101) if is_prime(x)]
print(primes)
prime_square_divisors = {x **2: (1, x, x**2) for x in range(101) if is_prime(x)}
pp(prime_square_divisors)


