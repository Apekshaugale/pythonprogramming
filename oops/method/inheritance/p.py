'''1. Class, Object & Namespace

Q1. Create a class Book with class variables title, author, price.
Access all three both via the class name and via an object.

class Book:
    title='Art of Being Alone'
    author='Ruvik'
    price=150
b=Book()
print(b.title)
print(b.author)
print(b.price)
o/p:
Art of Being Alone
Ruvik
150

Q2. Create a class Config with two class variables env = "dev"
and version = 1.0. Print Config.__dict__ and identify which entries
are your own variables vs Python's built-in ones.

class Config:
    env = "dev"
    version = 1.0
    print('The value')
print(Config.__dict__)


Q3. Create a class Movie with a docstring "Stores movie details" and
two class variables. Print the docstring using both .__doc__ and help().

class Movie :
# '''  '''Stores movie details''' '''
    name='hello'
    std=80
help(Movie)
print(Movie.__doc__)

o/p:
Help on class Movie in module __main__:

class Movie(builtins.object)
 |  Stores movie details
 |
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  name = 'hello'
 |
 |  std = 80

Stores movie details

