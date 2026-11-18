import random
username = ["aashish","pahari","Nikhil","kshtiz","asal"]
fake_name = random.choices(username, k = 2)
age = random.randint(1,100)
print(fake_name,age)