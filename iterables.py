iterable = ['spring', 'summer', 'autumn', 'winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# print(next(iterator))


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterator empty")


print(first([1, 2, 3]))
print(first({132, 2, 3}))
try:
    print(first(set()))
except ValueError:
    pass

# use yield once to make generators == iterator

def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
for v in gen123():
    print(v)
h = gen123()
i = gen123()
print(h, i)
print( h is i)
def gen246():
    print('about to yield 2')
    yield 2
    print('about to yield 4')
    yield 4
    print('about to yield 6')
    yield 6
    print('about to return')

g = gen246()
next(g)
next(g)
next(g)
# next(g)
# next(g)


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter +=1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3,items):
        print(item)


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 6, 9, 6, 8, 7, 8, 10]
    for item in distinct(items):
        print(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


if __name__ =='__main__':
    run_take()
    run_distinct()
    run_pipeline()



