import math
import json

x = abs(-7.24)
y = pow(4,3)
z = math.sqrt(64)

a = math.ceil(1.4)
b = math.floor(2.8)
print(x,"pow", a, b)

x = '{"name":"Jhon", "age":30}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(x)