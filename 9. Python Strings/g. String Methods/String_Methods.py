#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "python is FUN!"
x = txt.capitalize()
print (x)

txt = "36 is my age."
x = txt.capitalize()
print (x)

#casefold()
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#center()
txt = "banana"
x = txt.center(20)
print(x)

txt = "banana"
x = txt.center(20, "O")
print(x)

#count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

#encode()
txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

#endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))
print(x)

#expandtabs()
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#find()
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))

#format()
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

#Formatting Types
txt = "We have {:<8} chickens."
print(txt.format(49))

txt = "We have {:>8} chickens."
print(txt.format(49))

txt = "We have {:^8} chickens."
print(txt.format(49))

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

txt = "The universe is {:,} years old."
print(txt.format(13800000000))

txt = "The universe is {:_} years old."
print(txt.format(13800000000))

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

txt = "We have {:d} chickens."
print(txt.format(0b101))

txt = "We have {:e} chickens."
print(txt.format(5))

txt = "We have {:E} chickens."
print(txt.format(5))

txt = "The price is {:.2f} dollars."
print(txt.format(45))

txt = "The price is {:f} dollars."
print(txt.format(45))

x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

txt = "The price is {:f} dollars."
print(txt.format(x))

txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

txt = "You scored {:%}"
print(txt.format(0.25))

txt = "You scored {:.0%}"
print(txt.format(0.25))

#index()
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))

#isalnum()
txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)

#isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company10"
x = txt.isalpha()
print(x)

#isascii()
txt = "Company123"
x = txt.isascii()
print(x)

#isdecimal()
txt = "1234"
x = txt.isdecimal()
print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

#isdigit()
txt = "50800"
x = txt.isdigit()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())

#isidentifier()
txt = "Demo"
x = txt.isidentifier()
print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

#islower()
txt = "hello world!"
x = txt.islower()
print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())

#isnumeric()
txt = "565543"
x = txt.isnumeric()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

#isprintable()
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

#isspace()
txt = "   "
x = txt.isspace()
print(x)

txt = "   s   "
x = txt.isspace()
print(x)

#istitle()
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

#isupper()
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper())
print(b.isupper())
print(c.isupper())

#join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

#ljust()
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.ljust(20, "O")
print(x)

#lower()
#lstrip()
#maketrans()
#partition()
#replace()
#rfind()
#rindex()
#rjust()
#rpartition()
#rsplit()
#rstrip()
#split()
#splitlines()
#startswith()
#strip()
#swapcase()
#title()
#translate()
#upper()
#zfill()
