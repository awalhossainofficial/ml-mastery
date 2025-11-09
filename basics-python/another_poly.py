from mymodule import person1
import datetime
import platform

a = person1["age"]
x = datetime.datetime.now()

print(x,"hello", x.year, "str", x.strftime("%B"))

x = datetime.datetime(2020, 5, 17)
print(x,"hello")