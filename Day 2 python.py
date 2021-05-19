#!/usr/bin/env python
# coding: utf-8

# This is beginning of Python basics programming
# 
# Comments can be used to explain Python code.
# 
# Comments can be used to make the code more readable.
# 
# Comments can be used to prevent execution when testing code.

# In[1]:


#first python program
print("hello, world")


# In[2]:


print(67+90)


# In[3]:


print("hi, this me hina", 56+90)


# multiline string
# 
# Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

# In[4]:


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


# Python Operators:
# 
# Operators are used to perform operations on variables and values.
# 
# In the example below, we use the + operator to add together two values:

# User Input
# Python allows for user input.
# 
# That means we are able to ask the user for input.
# 
# The method is a bit different in Python 3.6 than Python 2.7.
# 
# Python 3.6 uses the input() method.
# 
# Python 2.7 uses the raw_input() method.
# 
# The following example asks for the username, and when you entered the username, it gets printed on the screen:

# In[6]:


username = input("Enter username:")
print("Username is: " + username)


# Python divides the operators in the following groups:
# 
# Arithmetic operators
# 
# Assignment operators
# 
# Comparison operators
# 
# Logical operators
# 
# Identity operators
# 
# Membership operators
# 
# Bitwise operators

# In[7]:


45/2-90*65/11+145 * 1.3*24//12


# Python Assignment Operators
# 
# Assignment operators are used to assign values to variables:

# In[9]:



x = 6
x >>= 3 #right shift operator
print(x)


# Python Comparison Operators
# 
# Comparison operators are used to compare two values:

# In[11]:


x = 5
y = 5

print(x >= y)
print(x<=y)
print(x==y)
print(x>y)
print(x<y)

# returns True because five is greater, or equal, to 3


# Python Logical Operators
# 
# Logical operators are used to combine conditional statements:
# 
# and, or , not

# In[12]:


x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result


# Python Identity Operators
# 
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is, is not

# In[13]:


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


# Python Membership Operators
# 
# Membership operators are used to test if a sequence is presented in an object:

# In[14]:


x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

x= "We are late, let us go back"
print("late" in x)


# Variables: 
# Variables are containers for storing data values.

# In[16]:


x = 5
y = "John"
z=input("")
print(x)
print(y)
print(x,y)
print("This is a demo: "+z, x, y)


# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# In[17]:


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# Variable Names:
# 
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
# Rules for Python variables:
# 
# A variable name must start with a letter or the underscore character
# 
# A variable name cannot start with a number
# 
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# In[18]:


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Many Values to Multiple Variables:
# 
# Python allows you to assign values to multiple variables in one line

# In[19]:


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables:
# 
# And you can assign the same value to multiple variables in one line

# In[20]:


x = y = z = "Orange"
print(x)
print(y)
print(z)


# ### Random Number:
# 
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# In[1]:


import random

print(random.randrange(10000, 2555552222))


# ## input()
# 
# The input() function allows user input.
# 
# ### Syntax
# input(prompt)
# 
# A String, representing a default message before the input.

# In[2]:


x = input("Enter your name:")
print("Hello, " + x)


# In[ ]:


#WAP that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old


# In[ ]:


#WAP to get user input of 5 numbers to find the average of the number and calculate percentage.


# ### What is String in Python?
# A string is a sequence of characters.
# 
# A character is simply a symbol. For example, the English language has 26 characters.
# 
# Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0s and 1s.
# 
# This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encodings used.
# 
# In Python, a string is a sequence of Unicode characters. Unicode was introduced to include every character in all languages and bring uniformity in encoding. You can learn about Unicode from Python Unicode.

# In[3]:


# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


# #### Strings are Arrays:
# 
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# 
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# 
# Square brackets can be used to access elements of the string.

# In[4]:


a = "Hello, World!"
print(a[0:5])


# #### String Length:
# 
# To get the length of a string, use the len() function.

# In[5]:


a = "Hello, World!"
print(len(a))


# #### Check String:
# 
# To check if a certain phrase or character is present in a string, we can use the keyword in.

# In[6]:


txt = "The best things in life are free!"
print("free" in txt)


# #### Slicing:
# 
# You can return a range of characters by using the slice syntax.
# 
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# In[7]:


b = "Hello, World!"
print(b[2:8])


# #### Slice From the Start:
# 
# By leaving out the start index, the range will start at the first character:

# In[8]:


b = "Hello, World!"
print(b[ :6])


# #### Slice To the End:
# 
# By leaving out the end index, the range will go to the end:

# In[9]:


b = "Hello, World!"
print(b[2:])


# #### Negative Indexing:
# 
# Use negative indexes to start the slice from the end of the string:

# In[10]:


b = "Hello, World!"
print(b[-13:-5])


# #### String Concatenation:
# 
# To concatenate, or combine, two strings you can use the + operator.

# In[11]:


a = "Hello"
b = "World"
c = a + b
print(c)


# #### How to change or delete a string?
# 
# Strings are immutable. This means that elements of a string cannot be changed once they have been assigned. We can simply reassign different strings to the same name.

# #### Concatenation of Two or More Strings
# Joining of two or more strings into a single one is called concatenation.
# 
# The + operator does this in Python. Simply writing two string literals together also concatenates them.
# 
# The * operator can be used to repeat the string for a given number of times.

# In[12]:


# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)


# ### Common Python String Methods
# There are numerous methods available with the string object. The format() method that we mentioned above is one of them. Some of the commonly used methods are lower(), upper(), join(), split(), find(), replace() etc. Here is a complete list of all the built-in methods to work with strings in Python.

# In[13]:


"HINA".lower()


# In[14]:


'Happy New Year'.replace('Happy','Brilliant')


# In[ ]:




