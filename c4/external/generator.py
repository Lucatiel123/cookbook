def a():
    yield 1
    yield 2
    yield 3
    yield 4

v1 = a()
print(next(v1))
print(next(v1))
print(next(v1))
print(next(v1))
#print(next(v1))

def b():
    for i in range(5):
        yield i * i

v2 = b()
for i in v2:
    print(i)

'''
python中迭代器和生成器的区别
1、共同点
生成器是一种特殊的迭代器
2、不同点
a、语法上
生成器是通过函数的形式中调用 yield 或（）的形式创建的
迭代器可以通过 iter（） 内置函数创建
b、用法上
生成器在调用next（）函数或for循环中，所有过程被执行，且返回值
迭代器在调用next（）函数或for循环中，所有值被返回，没有其他过程或说动作。
'''