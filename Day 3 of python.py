#!/usr/bin/env python
# coding: utf-8

# ### Python Collections (Arrays):
# 
# There are four collection data types in the Python programming language:
# 
# List is a collection which is ordered and changeable. Allows duplicate members.
# 
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 
# Set is a collection which is unordered and unindexed. No duplicate members.
# 
# Dictionary is a collection which is unordered and changeable. No duplicate members.
# 
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
# 
# Access Items:
# 
# List items are indexed and you can access them by referring to the index number:

# ### List:
# Lists are used to store multiple items in a single variable.
# 
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# 
# Lists are created using square brackets:

# In[2]:


thislist = ["apple", "banana", "cherry"]
d= [10,56,78,34]
print(d)
print(type(thislist))


# ### List Items:
# List items are ordered, changeable, and allow duplicate values.
# 
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# 
# Ordered:
# 
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# 
# If you add new items to a list, the new items will be placed at the end of the list.
# 
# Changeable:
# 
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# 
# Allow Duplicates:
# 
# Since lists are indexed, lists can have items with the same value:

# In[3]:


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))


# #### List Length:
# 
# To determine how many items a list has, use the len() function:

# In[4]:


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# List Items - Data Types:
# 
# List items can be of any data type:

# In[5]:


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(type(list1))


# A list can contain different data types:

# In[6]:


list1 = ["abc", 34, True, 40, "male"]
print(list1)


# The list() Constructor:
# 
# It is also possible to use the list() constructor when creating a new list.

# In[7]:


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Negative Indexing:
# 
# Negative indexing means start from the end
# 
# -1 refers to the last item, -2 refers to the second last item etc.

# In[8]:


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


# Range of Indexes:
# 
# You can specify a range of indexes by specifying where to start and where to end the range.
# 
# When specifying a range, the return value will be a new list with the specified items.

# In[9]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# By leaving out the start value, the range will start at the first item:

# In[10]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# Change Item Value:
# 
# To change the value of a specific item, refer to the index number:

# In[11]:


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Change a Range of Item Values:
# 
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# In[12]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# Insert Items:
# 
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# 
# The insert() method inserts an item at the specified index:

# In[13]:


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Append Items:
# 
# To add an item to the end of the list, use the append() method:

# In[14]:


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Extend List:
# 
# To append elements from another list to the current list, use the extend() method.

# In[15]:


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove Specified Item:
# 
# The remove() method removes the specified item.

# In[16]:


thislist = ["apple", "banana", "cherry", "banana", "cherry", "apple"]

thislist.remove("banana")
print(thislist)
thislist.remove("banana")
print(thislist)


# Sort List Alphanumerically:
# 
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# In[17]:


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Luckily we can use built-in functions as key functions when sorting a list.
# 
# So if you want a case-insensitive sort function, use str.lower as a key function:

# In[18]:


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Copy a List:
# 
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# 
# There are ways to make a copy, one way is to use the built-in List method copy().

# In[19]:


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# ### Tuple:
# Tuples are used to store multiple items in a single variable.
# 
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# 
# A tuple is a collection which is ordered and unchangeable.
# 
# Tuples are written with round brackets.

# In[20]:


thistuple = ("apple", "banana", "cherry")
print(thistuple)


# Tuple Items:
# 
# Tuple items are ordered, unchangeable, and allow duplicate values.
# 
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# 
# Ordered:
# 
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# 
# Unchangeable:
# 
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# 
# Allow Duplicates:
# 
# Since tuple are indexed, tuples can have items with the same value:

# In[21]:


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# The tuple() Constructor:
# 
# It is also possible to use the tuple() constructor to make a tuple.

# In[22]:


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Access Tuple Items:
# 
# You can access tuple items by referring to the index number, inside square brackets:

# In[23]:


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# Change Tuple Values:
# 
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# 
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# In[24]:


x = ("apple", "banana", "cherry")
y = list(x)   #use list constructor
y[1:3] = ["kiwi", "watermelon"]
x = tuple(y)

print(x)


# Add Items:
# 
# Once a tuple is created, you cannot add items to it.
# 
# Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

# In[25]:


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


# Remove Items:
# 
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# In[26]:


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)


# Unpacking a Tuple:
# 
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# In[27]:


fruits = ("apple", "banana", "cherry")

print(fruits)


# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# In[29]:


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# map()
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# 
# Syntax
# map(function, iterables)
# 
# strip()
# The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
# 
# Syntax
# string.strip(characters)
# 
# split()
# The split() method splits a string into a list.
# 
# You can specify the separator, default separator is any whitespace.
# 
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
# 
# Syntax
# string.split(separator, maxsplit)

# In[30]:


a = list(map(int,input("\nEnter the numbers : ").strip().split()))
print(a)


# In[32]:


# number of elements
n = int(input("Enter number of elements to be be in list: "))
  
# Below line read inputs from user using map() function 
a = list(map(int,input("\nEnter the numbers of list: ").strip().split()))[ :n]
  
print("\nList is - ", a)
b= sum(a)
print(b)


# Set:
# Sets are used to store multiple items in a single variable.
# 
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# 
# A set is a collection which is both unordered and unindexed.
# 
# Sets are written with curly brackets.

# In[33]:


thisset = {"apple", "banana", "cherry"}
print(thisset)


# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# 
# Unordered
# 
# Unordered means that the items in a set do not have a defined order.
# 
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# 
# Unchangeable
# 
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# 
# Once a set is created, you cannot change its items, but you can add new items.
# Duplicates Not Allowed:
# 
# Sets cannot have two items with the same value.

# In[34]:


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# Add Items
# 
# Once a set is created, you cannot change its items, but you can add new items.
# 
# To add one item to a set use the add() method.

# In[35]:


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)


# Add Sets:
# 
# To add items from another set into the current set, use the update() method.

# In[36]:


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# Dictionary
# 
# Dictionaries are used to store data values in key:value pairs.
# 
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# 
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# 
# Dictionaries are written with curly brackets, and have keys and values:

# In[37]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# Dictionary Items
# 
# Dictionary items are ordered, changeable, and does not allow duplicates.
# 
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# In[38]:


#WAP to create a dictionary with key as name, age, place 
d= {"name": "abc", "age":56, "place":"delhi"}
print(d["age"])


# Ordered or Unordered?
# 
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# 
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# 
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
# 
# Changeable
# 
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# 
# Duplicates Not Allowed
# 
# Dictionaries cannot have two items with the same key:

# In[39]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# Get method

# In[40]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)


# There is also a method called get() that will give you the same result:

# In[41]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)


# Get Keys
# 
# The keys() method will return a list of all the keys in the dictionary.

# In[42]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)


# Get Values
# 
# The values() method will return a list of all the values in the dictionary.

# In[43]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)


# Get Items
# 
# The items() method will return each item in a dictionary, as tuples in a list.

# In[44]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)


# In[ ]:




