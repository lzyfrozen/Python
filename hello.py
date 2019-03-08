import collections
d = collections.deque()
d.extend(['a', 'b', 'c', 'd', 'e'])
d.insert(2, 'z')
print(d)


def x():
    print('this is x')


x()