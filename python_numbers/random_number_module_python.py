import random
values = [6, 23, 21, 1000, 4556]

print(random.choice(values)) # choose a random element from values list
print(random.choice(values))
print(random.sample(values, 2)) # choose a sample of size 2 from values list

random.shuffle(values) # shuffle the values elements randomly
print(values)

print(random.randint(1, 10)) # get the random integer between 1 and 10
