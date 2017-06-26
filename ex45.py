## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a animal:
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a animal
class Cat(Animal):

	def __init__(self,name):
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## Inherits 
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object.
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## Halibut is-a fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat. (Go figure)
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary's pet is Satan.
mary.pet = satan 

## Frank is-a employye with 120,000 salary 
frank = Employee("Frank", 120000)

## Rover is Frank's pet
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon

## Harry is a Halibut
harry = Halibut