class Cat:
  species = 'mammal'
  oldest = 0
  def __init__(self, name, age):
      self.name = name
      self.age = age
  # def check_oldest(self):
  #   if (self.age > Cat.oldest):
  #     Cat.oldest = self.age
  @classmethod
  def add(cls,n,m):
    return n+m

pet_1= Cat('Miko','4')
pet_2= Cat('Chi','8')
pet_3= Cat('Toty','3')

def age_check(*args):
  print(max(args))


age_check(pet_1.age,pet_2.age,pet_3.age)
print(Cat.species)
print(Cat.add(1,2))