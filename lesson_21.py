class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


dog1 = Dog('Шарик',2)
dog2 = Dog('Валерик',3)
dog3= Dog('Валерик',3)
print(hash(dog1))
print(hash(dog2))
print(hash(dog3))

print(dog2 == dog3)

data = {}

data[dog1] = '1'
data[dog2] = '2'
data[dog3] = '3'
print(data)

print(hash([1, 2, 3]))
