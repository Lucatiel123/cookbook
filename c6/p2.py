import json

data1 = {
    "name": "Alice",
    "shares": 100,
    "price": 532.5
}

print(json.dumps(data1))


data2 = {
    "name": "Kate",
    "shares": 95,
    "price": 111.5
}

with open('p2_json.txt', 'r') as f:
    print(json.load(f))


with open('p2_json.txt', 'w') as f:
    json.dump(data1, f)


print('-----------')
print(json.dumps(False))

data3 = {
    'a': True,
    'b': 'Hello',
    'c': None
}
print(json.dumps(data3))

data4 = '''
{
    "a": true,
    "b": "Hello",
    "c": null
}
'''
#data4 = '{"a": true, "b": "Hello", "c": null}'
#print(data4.replace('\n', '').replace(' ', ''))
print(json.loads(data4))

print("---------")
data5 = {"a":[1,2,3,4,5],"b":[2,3,4,5,6],"c":[{"k1":1,"k2":2,"k3":3}]}
from pprint import pprint
pprint(data5)