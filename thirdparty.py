#third party modules

'''
pip install modules_name
pip show(modules_name)
pip show faker
'''
# import faker
from faker import Faker
# print(dir(faker))
fake = Faker()

print(fake.name())
print(fake.email())



