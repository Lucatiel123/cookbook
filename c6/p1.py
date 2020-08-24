import csv

print("每行读取为列表")
with open('p1_file.txt') as f:
    f_csv = csv.reader(f)
    heading = next(f_csv)
    for row in f_csv:
        print(row)


print('-------------')
print("每行读取为元组")
from collections import namedtuple
with open('p1_file.txt') as f:
    f_csv = csv.reader(f)
    heading = next(f_csv)
    Row = namedtuple('Row', heading)
    print(Row)
    for r in f_csv:
        row = Row(*r)
        print(row)

print('-------------')
print("每行读取为字典")
with open('p1_file.txt') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)
