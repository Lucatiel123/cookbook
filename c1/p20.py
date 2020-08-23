# 多映射合并

from collections import ChainMap

a = {"x": 1, "y": 2}
b = {"z": 3, "y": 4}

# 重复键使用第一个
c = ChainMap(a, b)
print(c)
print(c["x"])
print(c["y"])
print(c["z"])
print(list(c.keys()))
print(list(c.values()))

print('---------')
merges = dict(b)
merges.update(a)
print(merges)


print('---------')
# update构建的新字典，原来字典改变不会反应到合并的字段
# ChainMap由于用的是原来的字典，所以修改还是会体现
print(c)
print(c["x"])
print(merges)
print(merges["x"])
a["x"] = 42
print(c)
print(c["x"])
print(merges)
print(merges["x"])