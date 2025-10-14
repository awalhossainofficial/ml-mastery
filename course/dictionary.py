thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "numbers":[1,2,3,4,5],
  "colors":["red","blue","green"]
}
print(thisdict.items())

for key, vlaue in thisdict.items():
    print(key, vlaue)

keys = thisdict.keys() 
print(thisdict.pop("year"),"removing")
print("setDefault", thisdict.setdefault("year",2010),"adding", thisdict.items())