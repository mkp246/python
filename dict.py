urls = {'Google': 'http;//google.com',
        'Pluralsight': "http://pluralsight.com",
        "Sixty North": 'http://sixty-north.com',
        "Microsoft": "http://microsoft.com"
        }
print(urls)
urls['Google'] = 'http://facebook.com'
nameAndAges = [('alice', 32), ('bob', 10)]
d = dict(nameAndAges)
print(d)
# copy used as .copy or constructor of dict eg. dict()
g = dict(wheat=0x1232654, khaki=0x869732, crimson=0xde21ac)
print(g)
g.update(d)
print(g)

stocks = dict(GOOG=891, APPl=428, IBM=432)
stocks.update({'GOOG': '654'})
print(stocks)
for key in stocks:
    print("{key} => {value}".format(key=key, value=stocks[key]))
# element in dict for presence check or not in
try:
    del g['wheat']
    del g['wheat']  # TODO this will raise key error as already deleted
except KeyError:
    print('key not found in dictionary')
from pprint import pprint as pp
pp(g)
