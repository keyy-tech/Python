## Datatypes

# String

# literal assignment
first = "Dave"
last = "Gray"

print(type(first))
print(type(last) == str)
print(isinstance(first,str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# type casting
decade = str(100)
print(type(decade))
print(type(100))
print(decade)

statement = "I like rock music from the "+ decade + "s."
print(statement)

# multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
          
          All good?
'''

print(multiline)

sentence = "I'm back \\ \n"

# string methods

name = 'Jude'
print(name.strip())
print(name.lstrip())
print(name.rstrip())