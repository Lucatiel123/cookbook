# 任意可迭代对象分解元素

*trailing, current = [10, 20, 30, 55, 17, 20]
print(trailing)
print(current)


print("------------")
records =[
    ('foo', 1, 2),
    ('foo', 3, 4),
    ('bar', 'hello')
]


def do_foo(x, y):
    print('foo', 'x', 'y')


def do_bar(s):
    print('bar','s')


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
    else:
        print('go out')


print("------------")
records = ('ACE', 1995, 123.11, (12, 18, 2012))
name, *_, (*_, year) = records
print(name)
print(year)

print("------------")
item = [1, 5, 3, 324, 23, 2324]
head, *tails = item
print(head)


def sum_(items):
    head ,*tails = items
    return head + sum(tails) if tails else head

print(sum_(item))