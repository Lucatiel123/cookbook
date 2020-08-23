# 元素分解为N哥单独变量
p = (4, 5)
x, y = p
print(x)
print(y)

print('---------')
data = ['ACE', 1, 3, (2013, 9, 10)]
name, shares, price, date = data
print(name)
print(shares)
print(price)
print(date)

print('---------')

name, shares, price, (year, month, day) = data
print(year)
print(month)
print(day)


# _可以表示展位符号
print('---------')
shares, _, _, (year, month, day) = data
print(year)
print(month)
print(day)