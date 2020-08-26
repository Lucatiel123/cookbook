# 遍历一个可迭代对象中所有元素，不使用for循环

with open('passwd','r', encoding='utf-8') as f:
    file = f.read()
    print(file)

print('---------------')

with open('passwd', 'r', encoding='utf-8') as f:
    line_number = 1
    try:
        while True:
            print('第 {} 行内容为: {}'.format(line_number, next(f)))
            line_number += 1
    except StopIteration:
        pass

print('----------------')
a = [1, 2, 3, 4, ]
it = iter(a)
'''
    相当于在函数内添加
    def __iter__(self)：
        return self`
'''
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
