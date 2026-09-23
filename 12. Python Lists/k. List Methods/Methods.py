#append()
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

#clear()
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#copy()
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

#count()
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

#extend()
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

#index()
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)

#insert()
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#pop()
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

#remove()
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#sort()
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)