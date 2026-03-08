coordinates = [(20,25.2), (22.5, 23.3), (18.4, 32.2)]
location = ["dhaka", "sylhel", "Pabna","Bogura"]

pairs = dict(zip(location, coordinates))

exact_location = {co_or:loc for co_or,loc in zip(coordinates,location)}

print(exact_location)