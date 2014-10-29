## Data types in python
#Immutables (numbers, strings, tuples, frozensets)
#None of the object types in the immutable category support in-place changes,
#though we can always run expressions to make new objects and assign their results
#to variables as needed.

#Mutables (lists, dictionaries, sets)
#Conversely, the mutable types can always be changed in-place with operations that
#do not create new objects. Although such objects can be copied, in-place changes
#support direct modification.


#Write myfile.py with the following contents:
title = "The Meaning of Life"

% python # Start Python
>>> import myfile # Run file; load module as a whole
>>> print(myfile.title) # Use its attribute names: '.' to qualify
The Meaning of Life

% python # Start Python
>>> from myfile import title # Run file; copy its names
>>> print(title) # Use name directly: no need to qualify
The Meaning of Life

# Define three attributes in a file threenames.py
a = 'dead' 
b = 'parrot' # Exported to other files
c = 'sketch'
print(a, b, c) # Also used in this file

# You can create a long variable by a prefix L or I
>>> var = 5L
>>> type(var)
<type 'long'>

# You can also create a complex variable
>>> var = 5+2j
>>> type(var)
<type 'complex'>
>>> var.real
5.0
>>> var.imag
2.0

# Returns a tuple that is (x//y, x%y)
>>> divmod(3,2) 
(1, 1)

% python threenames.py
dead parrot sketch

--------------------------------------
>>> exec(open('script1.py').read())
win32
4294967296
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!

#The exec call has an effect similar to an import, but it doesn’t technically import the
#module—by default, each time you call exec this way it runs the file anew, as though
#you had pasted it in at the place where exec is called. Because of that, exec does not
#require module reloads after file changes—it skips the normal module import logic.
#On the downside, because it works as if pasting code into the place where it is called,
#exec, like the from statement mentioned earlier, has the potential to silently overwrite
#variables you may currently be using. For example, our script1.py assigns to a variable
#named x. If that name is also being used in the place where exec is called, the name’s
#value is replaced:
>>> x = 999
>>> exec(open('script1.py').read()) # Code run in this namespace by default
win32
4294967296
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
>>> x # Its assignments can overwrite names here
'Spam!'
-------------------------

>>> import math
>>> math.pi
3.1415926535897931
>>> math.sqrt(85)
9.2195444572928871

>>> math.atan2
>>> import random
>>> random.random()
0.59268735266273953
>>> random.choice([1, 2, 3, 4])
1

##The del() command doesn't delete the value referenced by a variable, it is still
##managed by python's garbage collector. It deletes the variable's reference to the
##value.
>>> v1 = 5
>>> v2 = 5
>>> del(v1)     # v1 and v2 point to the same value here. Deleting v1 just deletes v1's reference. v2 is still 5.


>>> import keyword      # module on keywords
>>> for key in keyword.kwlist:
	print key

and
as
assert
break
class
continue
def
del
elif
else
except
exec
finally
for
from
global
if
import
in
is
lambda
not
or
pass
print
raise
return
try
while
with
yield


## STRINGS
##--------
#putting a comma retuns them in a tuple
>>> 'shrubbery', "shrubbery"   
('shrubbery', 'shrubbery')

#use appropriate quotes when needed to enclose strings
>>> 'knight"s', "knight's"    
('knight"s', "knight's")

# Implicit concatenation
>>> title = "Meaning " 'of' " Life"     
>>> title
'Meaning of Life'

#escape sequences to insert special byte codings
>>> 'knight\'s', "knight\"s"       
("knight's", 'knight"s')

# \n is end-of-line, \t is tab
>>> S = 'A\nB\tC'     
>>> len(S) # Each stands for just one character
5
>>> ord('\n') # \n is a byte with the binary value 10 in ASCII
10
>>> S = 'A\0B\0C' # \0, a binary zero byte, does not terminate string
>>> len(S)
5

#raw strings, which disbles escape sequences
>>> x = r'C:\new\text.dat'
>>> x
'C:\\new\\text.dat'
>>> print(x)
C:\new\text.dat

#If you need to end a raw string with a
#single backslash, you can use two and slice off the second
(r'1\nb\tc\\'[:-1])
#or just double up the backslashes in a normal string
('1\\nb\\tc\\')


##Writing multiline string block with triple quotes
>>> mantra = """Always look
... on the bright
... side of life."""
>>>
>>> mantra
'Always look\n on the bright\nside of life.'

>>> print(mantra)
Always look
on the bright
side of life.
##Triple quotes can also be used to disable parts of code
X = 1
"""
import os # Disable this code temporarily
print(os.getcwd())
"""
Y = 2

##Iteration
>>> for c in word: print c + ' '

h 
a 
c 
k 
e 
r

##Accessing string index and slicing
>>> S[1:3] # Slice of S from offsets 1 through 2 (not 3)
'tr'
>>> S[1:] # Everything past the first (1:len(S))
'pam'
>>> S # S itself hasn't changed
'Spam'
>>> S[0:3] # Everything but the last
'Spa'
>>> S[:3] # Same as S[0:3]
'Spa'
>>> S[:-1] # Everything but the last again, but simpler (0:-1)
'Spa'
>>> S[:] # All of S as a top-level copy (0:len(S))
'Spam'

##Slicing with a third argument
>>> S = 'abcdefghijklmnop'
>>> S[1:10:2]
'bdfhj'
>>> S[::2]
'acegikmo'

>>> S = 'hello'
>>> S[::-1]
'olleh'

>>> S = 'abcdefg'   
>>> S[5:1:-1]       ##Be aware that with a negative stride, the meaning
'fedc'              ##of the first two bounds is essentially reversed

##Also, you can use slice() to achieve same results
>>> 'spam'[1:3]
'pa'
>>> 'spam'[slice(1, 3)]
'pa'
>>> 'spam'[::-1]
'maps'
>>> 'spam'[slice(None, None, -1)]
'maps'

##slices can also be used to print or return in a special way
>>> print 'abcdef'[:-1]
abcde

##String conversion
>>> '42' + str(1)
'421'
>>> int('42') + 1
43
>>> repr(42)    ##convert anything inside to a string, even with quotes
'42'
>>> print (str('spam'), repr('spam'))   #repr() - string representation
('spam', "'spam'")
>>> str(3.1415), float("1.5")
('3.1415', 1.5)
>>> text = "1.234E-10"
>>> float(text)
1.2340000000000001e-010

##Character code conversions
>>> ord('s')
115
>>> chr(115)
's'
>>> S = '5'
>>> S = chr(ord(S) + 1)
>>> S
'6'
>>> S = chr(ord(S) + 1)
>>> S
'7'

##Changing Strings
>>> S = 'spam'
>>> S = S + 'SPAM!'
>>> S
'spamSPAM!'
--------------------------------------------------
>>> S = S[:4] + 'Burger' + S[-1]
>>> S
'spamBurger!'
--------------------------------------------------
>>> S = 'splot'
>>> S = S.replace('pl', 'pamal')
>>> S
'spamalot'
--------------------------------------------------
>>> 'aa$bb$cc$dd'.replace('$',' SIGN ')    #replace the string occurrence with the second argument
'aa SIGN bb SIGN cc SIGN dd'
---------------------------------------------------
>>> 'That is a {0} {1} bird!'.format(1, 'dead')  #format method in py2.6
'That is a 1 dead bird!'
>>> 'That is a %d %s bird!' % (1, 'dead')
'That is a 1 dead bird!'
---------------------------------------------------
>>> S = 'xxxxSPAMxxxxSPAMxxxx'      #replace the string occurence manually
>>> where = S.find('SPAM')           #find the offset of the first occurence of 'SPAM'
>>> where
4
>>> S = S[:where] + 'EGGS' + S[(where + 4):]    #then replace
>>> S
'xxxxEGGSxxxxSPAMxxxx'
----------------------------------------------------
>>> S = 'xxxxSPAMxxxxSPAMxxxx'          #or use the replace() method
>>> S = S.replace('SPAM','EGGS',1)
>>> S
'xxxxEGGSxxxxSPAMxxxx'
-----------------------------------------------
>>> S = 'spammy'
>>> S = list(S)         #the technique can be use to convert list <-> string
>>> S
['s', 'p', 'a', 'm', 'm', 'y']
>>> S = ''.join(S)      #join puts the strings in a list (or
                        #other iterable) together, with the delimiter
                        #between list items; in this case, it uses an
                        #empty string delimiter to convert from a list
                        #back to a string. More generally, any string
                        #delimiter and iterable of strings will do.
>>> S
'spammy'

>>> 'SPAM'.join(['eggs', 'sausage', 'ham', 'toast'])
'eggsSPAMsausageSPAMhamSPAMtoast'
----------------------------------
>>> line = 'aaa bbb ccc'
>>> line = line.split()    #split method chops up a string into a list of substrings
                           #around a delimiter string. We didn’t pass a delimiter in
                           #the prior example, so it defaults to whitespace.
>>> line
['aaa', 'bbb', 'ccc']

>>> line = 'bob,hacker,40'
>>> line.split(',')
['bob', 'hacker', '40']

#Other string methods
>>> line = "The knights who say Ni!\n"
>>> line.rstrip()
'The knights who say Ni!'
>>> line.upper()
'THE KNIGHTS WHO SAY NI!\n'
>>> line.isalpha()
False
>>> line.endswith('Ni!\n')
True
>>> line.startswith('The')
True

>>> line
'The knights who say Ni!\n'
>>> line.find('Ni') != −1 # Search via method call or expression
True
>>> 'Ni' in line
True
>>> sub = 'Ni!\n'
>>> line.endswith(sub) # End test via method call or slice
True
>>> line[-len(sub):] == sub
True

## string formatting
>>> '%s-----%s------%s' % ('SPAM', 45.335, [4,5,6])    #old formatting style
'SPAM-----45.335------[4, 5, 6]'
--------------------------------------------------
>>> template = '{0}, {1} and {2}'   #By position
>>> template.format('spam', 'ham', 'eggs')
'Spam, Eggs and Ham'
-------------------------------------------------------
>>> template = '{motto}, {pork} and {food}' # By keyword
>>> template.format(motto='spam', pork='ham', food='eggs')
'spam, ham and eggs'
-----------------------------------------------------
>>> template = '{motto}, {0} and {food}' # By both
>>> template.format('ham', motto='spam', food='eggs')
'spam, ham and eggs'
-------------------------------------------------------------------
>>> '{motto}, {0} and {food}'.format(42, motto=3.14, food = [1, 2])  #mixed
'3.14, 42 and [1, 2]'
-------------------------------------------------------------
>>> 'My {1[spam]} runs {0.platform}'.format(sys, {'spam':'laptop'})
'My laptop runs win32'
----------------------------------------------------------
>>> 'My {config} runs {sys.platform}'.format(sys=sys, config={'spam':'laptop'})
"My {'spam': 'laptop'} runs win32"
>>> 'My {config[spam]} runs {sys.platform}'.format(sys=sys, config={'spam':'laptop'})
'My laptop runs win32'

>>> somelist = list('SPAM')
>>> somelist
['S', 'P', 'A', 'M']
>>> 'first{0[0]}, second{0[2]} and third{0[2]}'.format(somelist)
'firstS, secondA and thirdA'
>>> 'first{0}, third{1}'.format(somelist[0], somelist[-1])
'firstS, thirdM'
>>> parts = somelist[0], somelist[-1], somelist[1:3] # [1:3] fails in fmt
>>> 'first={0}, last={1}, middle={2}'.format(*parts)
"first=S, last=M, middle=['P', 'A']"

#adding specific formatting
>>> '{0:10} = {1:10}'.format('spam', 123.345)
'spam       =    123.345'
>>> '{0:>10} = {1:<10}'.format('spam', 123.345)
'      spam = 123.345   '
>>> '{0:<10} = {1:<10}'.format('spam', 123.345)
'spam       = 123.345   '
>>> import sys
>>> '{0.platform:>10} = {1[item]:<10}'.format(sys, dict(item='laptop'))
'     win32 = laptop    '
#In the following {2:g} means the third argument formatted by default according
#to the “g” floating-point representation, {1:.2f} designates the “f” floating-point
#format with just 2 decimal digits, and {2:06.2f} adds a field with a width of
#6 characters and zero padding on the left.
>>> '{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159)
'3.141590e+00, 3.142e+00, 3.14159'
>>> '{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159)
'3.141590, 3.14, 003.14'

>>> '{0:X}, {1:o}, {2:b}'.format(255, 255, 255) # Hex, octal, binary
'FF, 377, 11111111'
>>> bin(255), int('11111111', 2), 0b11111111 # Other to/from binary
('0b11111111', 255, 255)
>>> hex(255), int('FF', 16), 0xFF # Other to/from hex
('0xff', 255, 255)
>>> oct(255), int('377', 8), 0o377, 0377 # Other to/from octal
('0377', 255, 255, 255)

>>> '{0:.2f}'.format(1 / 3.0) # Parameters hardcoded
'0.33'
>>> '%.2f' % (1 / 3.0)
'0.33'
>>> '{0:.{1}f}'.format(1 / 3.0, 4) # Take value from arguments
'0.3333'
>>> '%.*f' % (4, 1 / 3.0) # Ditto for expression
'0.3333'

>>> '{0:.2f}'.format(1.2345) # String method
'1.23'
>>> format(1.2345, '.2f') # Built-in function
'1.23'

#More extra features
>>> bin((2 ** 16) −1)
'0b1111111111111111'
>>> '{0:b}'.format((2 ** 16) −1)
'1111111111111111'
----------------------------
##Immutability
>>> S
'Spam'
>>> S[0] = 'z' # Immutable objects cannot be changed
#...error text omitted...
#TypeError: 'str' object does not support item assignment
>>> S = 'z' + S[1:] # But we can run expressions to make new objects
>>> S
'zpam'
##In terms of the core types, numbers, strings, and tuples are immutable;
##lists and dictionaries are not (they can be changed in-place freely).

------------------------------
>>> S.find('pa') # Find the offset of a substring
1
>>> S
'Spam'
>>> S.replace('pa', 'XYZ') # Replace occurrences of a substring with another
'SXYZm'
>>> S
'Spam'
>>> line = 'aaa,bbb,ccccc,dd'
>>> line.split(',') # Split on a delimiter into a list of substrings
['aaa', 'bbb', 'ccccc', 'dd']
>>> S = 'spam'
>>> S.upper() # Upper- and lowercase conversions
'SPAM'
>>> S.isalpha() # Content tests: isalpha, isdigit, etc.
True
>>> line = 'aaa,bbb,ccccc,dd\n'
>>> line = line.rstrip() # Remove whitespace characters on the right side
>>> line
'aaa,bbb,ccccc,dd'

>>> '%s, eggs, and %s' % ('spam', 'SPAM!') # Formatting expression (all)
'spam, eggs, and SPAM!'
>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!') # Formatting method (2.6, 3.0)
'spam, eggs, and SPAM!'

>>>dir(line)    #return the methods for that string object
>>>help(line.rstrip)   #provide help with the built in function rstrip



--------------------------------------------------


## LISTS
##-------
##Common list literals and operations
L = []                              #An empty list
L = [0, 1, 2, 3]                    #Four items: indexes 0..3
L = ['abc', ['def', 'ghi']]         #Nested sublists
L = list('spam')                    #List of an iterable’s items 
L = list(range(-4, 4))              #list of successive integers

L[i]             #Index, index of index, slice, length
L[i][j]
L[i:j]
len(L)

L1 + L2                  #Concatenate
L * 3                    #Repeat
for x in L: print(x)     #Iteration
3 in L                   #Membership

L.append(4)              #Methods: growing
L.extend([5,6,7])
L.insert(I, X)

L.index(1)              #Index of first 1 occurring in L
L.count(X)              #Total occurrences of X is L

L.sort()                 #Methods: sorting, reversing, etc.
L.reverse()

L.max()                 # max and min value in sequence L
L.min()

del L[k]                 #Methods, statement: shrinking
del L[i:j]
L.pop()
L.remove(2)
L[i:j] = []

L[i] = 1                 #Index assignment, slice assignment
L[i:j] = [4,5,6]

L = [x**2 for x in range(5)]          #List comprehensions and maps
>>>list(map(ord, 'spam'))
[115, 112, 97, 109]
---------------------------------------------------------------
>>> L = [123, 'spam', 1.23]           # A list of three different-type objects
>>> len(L)                            # Number of items in the list
3
-----------
>>> L[0]                              # Indexing by position
123
>>> L[:-1]                            # Slicing a list returns a new list
[123, 'spam']
>>> L + [4, 5, 6]                     # Concatenation makes a new list too, but it just prints it; doesn't change L here
[123, 'spam', 1.23, 4, 5, 6]
-------------------
>>> L.append('NI')                    # Growing: add object at end of list
>>> L
[123, 'spam', 1.23, 'NI']
-----------
>>> L.pop(2)                          # Shrinking: delete an item in the middle
1.23
>>> L                                 # "del L[2]" deletes from a list too
[123, 'spam', 'NI']
-------------------
>>> M = ['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']
---------------------
>>> L = ['abc', 'ABD', 'aBe']
>>> L.sort()                            #Sort with mixed case
>>> L
['ABD', 'aBe', 'abc']
>>> L = ['abc', 'ABD', 'aBe']
>>> L.sort(key = str.lower)             #normalize to lowercase
>>> L
['abc', 'ABD', 'aBe']
>>> L = ['abc', 'ABD', 'aBe']
>>> L.sort(key = str.lower, reverse=True)     #reverse sort order
>>> L
['aBe', 'ABD', 'abc']
--------------------------

#Be advised, that the sort() and append() method don't return a list, but they modify
#them entirely. So if you try to do L = L.append(), you will lose the reference to the
#list.

#To return a list while sorting, use the sorting() method.
>>> L = ['abc', 'ABD', 'aBe']
>>> L = sorted(L, key = str.lower, reverse=True)
>>> L
['aBe', 'ABD', 'abc']
>>> L = ['abc', 'ABD', 'aBe']
>>> L = sorted([x.lower() for x in L], reverse=True)
>>> L
['abe', 'abd', 'abc']
#Here you will notice that sorted() modifies the actual list, turning the
#elements to lowercase
-------------------------------
>>> res = [c*3 for c in 'spam']
>>> res
['sss', 'ppp', 'aaa', 'mmm']
------------------------
>>> res = []
>>> for c in 'spam':
	res.append(c*3)
>>> res
['sss', 'ppp', 'aaa', 'mmm']
-------------------------
>>> M
['aa', 'bb', 'cc']
>>> M.reverse()
>>> M
['cc', 'bb', 'aa']
--------------------------
>>> L = [1,2]
>>> L.extend([3,4,5])
>>> L
[1, 2, 3, 4, 5]
>>> L.pop()
5
>>> L
[1, 2, 3, 4]
>>> L.reverse()
>>> L
[4, 3, 2, 1]
>>> list(reversed(L))
[1, 2, 3, 4]
>>> reversed(L)
<listreverseiterator object at 0x00000000026F1240>
>>> L
[4, 3, 2, 1]
-----------------------------
>>> L = []
>>> L.append(1)
>>> L.append(2)
>>> L
[1, 2]
>>> L.pop()
2
>>> L
[1]
-----------------------------
>>> str([1,2,3,4]) + '34'
'[1, 2, 3, 4]34'
>>> [1, 2] + list('34')
[1, 2, '3', '4']

>>> list(map(abs, [-1, -2, 0, 1, 2]))   # map function abs() across sequence
[1, 2, 0, 1, 2]
--------------------------
>>> L = ['spam', 'eggs', 'ham']
>>> L.index('eggs')
1
>>> L.insert(1, 'leaf')
>>> L
['spam', 'leaf', 'eggs', 'ham']
>>> L.remove('eggs')
>>> L
['spam', 'leaf', 'ham']
>>> L.pop(0)
'spam'
>>> L
['leaf', 'ham']
>>> L.pop()
>>> L
['leaf']
----------------------
>>> L = ['spam', 'eggs', 'ham']
>>> del L[0]
>>> L
['eggs', 'ham']
>>> L = ['spam', 'eggs', 'ham']
>>> del L[1:]
>>> L
['spam']
>>> L = ['spam', 'eggs', 'ham']
>>> L[1:] = []
>>> L
['spam']
>>> L[0] = []
>>> L
[[]]
#list comprehensions (brief)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>>col1 = [row[1] for row in M]
>>>col1 = [2, 5, 8]

>>> [row[1] + 1 for row in M] # Add 1 to each item in column 2
[3, 6, 9]

>>> [row[1] for row in M if row[1] % 2 == 0] # Filter out odd items
[2, 8]

>>> diag = [M[i][i] for i in [0, 1, 2]] # Collect a diagonal from matrix
>>> diag
[1, 5, 9]

>>> doubles = [c * 2 for c in 'spam'] # Repeat characters in a string
>>> doubles
['ss', 'pp', 'aa', 'mm']

>>> G = (sum(row) for row in M)

## DICTIONARIES
##--------------

>>> D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}  #declaration
>>> D['food'] # Fetch value of key 'food'
'Spam'
>>> D['quantity'] += 1 # Add 1 to 'quantity' value
>>> D
{'food': 'Spam', 'color': 'pink', 'quantity': 5}
-------------------------------------
>>> D = {}
>>> D['name'] = 'Bob' # Create keys by assignment
>>> D['job'] = 'dev'
>>> D['age'] = 40
>>> D
{'age': 40, 'job': 'dev', 'name': 'Bob'}
>>> print(D['name'])
Bob

#Other ways to make dictionaries
>>> dict(name='mel', age=45) # dict keyword argument form. Requires all keys to be strings.
{'age': 45, 'name': 'mel'}

>>> dict([('age', 45),('name', 'mel')])   #dict key/value tuples form. Useful if you need to build up keys and values as sequences at runtime.
{'age': 45, 'name': 'mel'}

>>> dict.fromkeys(['name', 'age'],0)   #Useful for creating a dict from keys with a common default value
{'age': 0, 'name': 0}

>>> D = dict.fromkeys('spammer')
>>> D
{'a': None, 'e': None, 'm': None, 'p': None, 's': None, 'r': None}

>>> list(zip(['a','b','c'],[1,2,3]))   # Zip together keys and values. list() is only required in py3.0
[('a', 1), ('b', 2), ('c', 3)]
>>> dict(zip(['a','b','c'],[1,2,3]))
{'a': 1, 'c': 3, 'b': 2}

#Dictionary comprehensions

--------------------------------------------------------
>>> rec = {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}
>>> rec['name'] # 'name' is a nested dictionary
{'last': 'Smith', 'first': 'Bob'}
>>> rec['name']['last'] # Index the nested dictionary
'Smith'
>>> rec['job'] # 'job' is a nested list
['dev', 'mgr']
>>> rec['job'][-1] # Index the nested list
'mgr'
>>> rec['job'].append('janitor') # Expand Bob's job description in-place
>>> rec
{'age': 40.5, 'job': ['dev', 'mgr', 'janitor'], 'name': {'last': 'Smith', 'first': 'Bob'}}
--------------------------------------------------
>>> Ks = list(D.keys()) # Unordered keys list
>>> Ks # A list in 2.6, "view" in 3.0: use list()
['a', 'c', 'b']
--------------------------------------
>>> D = {'spam':2, 'ham':1, 'eggs':3}                  #Defining a dictionary
>>> D
{'eggs': 3, 'ham': 1, 'spam': 2}
>>> D['spam']                                          #query an element by its key
2
>>> len(D)
3
>>> 'ham' in D
True
>>> list(D.keys())                                #list() required in py3.0+
['eggs', 'ham', 'spam']
>>> D.keys()
['eggs', 'ham', 'spam']

>>> D
{'eggs': 3, 'ham': 1, 'spam': 2}
>>> D['ham'] = ['grill', 'bake', 'fry']         #updating an entry by key, with nested elements
>>> D
{'eggs': 3, 'ham': ['grill', 'bake', 'fry'], 'spam': 2}

>>> D['Brunch'] = 'Bacon'                       #adding a new element
>>> D
{'eggs': 3, 'Brunch': 'Bacon', 'ham': ['grill', 'bake', 'fry'], 'spam': 2}

>>> D.get('eggs')
3
>>> D.get('soda')
>>> print(D.get('soda'))
None
>>> D.get('soda', 66)                           #if the key 'soda' doesn't exist, print 66 instead of an error
66 

>>> D = {'eggs': 3, 'ham': 1, 'spam': 2}
>>> D2 = {'toast':4, 'muffin':5}
>>> D.update(D2)                        #concatenation. Any same keys on D will be overwritten.
>>> D
{'toast': 4, 'muffin': 5, 'eggs': 3, 'ham': 1, 'spam': 2}
>>> D.pop('muffin')                             #delete an existing key by pop(keyname)
5
>>> D
{'toast': 4, 'eggs': 3, 'ham': 1, 'spam': 2}
>>> del D['eggs']                               #deleting a key by name
>>> D
{'toast': 4, 'ham': 1, 'spam': 2}
##Printing using for loop
>>> for key in D:
	print(key, '=>', D[key])

	
('food', '=>', 'Spam')
('color', '=>', 'pink')
('name', '=>', 'Bob')
('quantity', '=>', 4)

##Printing using for loop
>>> for key in sorted(D):            #sort the keys
	print(key, '=>', D[key])

>>> language = 'Python'
>>> table = {'Python': 'Guido van Rossum', 'Perl': 'Larry Wall', 'Tcl': 'John Ousterhout' }
>>> table[language]
'Guido van Rossum'
>>> for lang in table:
	    '{0:<10} {1:>10}'.format(lang, table[lang])

	    
'Python     Guido van Rossum'
'Tcl        John Ousterhout'
'Perl       Larry Wall'
	
('color', '=>', 'pink')
('food', '=>', 'Spam')
('name', '=>', 'Bob')
('quantity', '=>', 4)

## Assigning new keys grows dictionaries
>>> D['e'] = 99 
>>> D
{'a': 1, 'c': 3, 'b': 2, 'e': 99}

##Trying to refer a non-existent key
>>>D['f']
KeyError: 'f'

##check if a key is non-existent
>>>'f' in D
False
>>>if not 'f' in D:
    print ('missing')

missing

##check if a key is existing using the get method
>>>value = D.get('x', 0)

##check if a key is existing using if
>>>value = D['x'] if 'x' in D else 0

##return values from a dictionary
>>> D = {'a': 1, 'c': 3, 'b': 2, 'e': 99}
>>> D.values()
[1, 3, 2, 99]
>>> 

##return a list with keys and their elements
>>> D.items()
[('a', 1), ('c', 3), ('b', 2), ('e', 99)]

##return keys from a dictionary using for
>>> for k in D.keys():         #instead of using D.Keys(), you can use just D
        print (k)
        
a
c
b
e

>>> F = D.keys()             #first return a list of keys and storing it.
>>> F
['toast', 'ham', 'spam']
>>> for g in sorted(F):
	print (g, D[g])       #printing the keys and their elements using for.

	
('ham', 1)
('spam', 2)
('toast', 4)

>>> for k in sorted(D):        #Another method for sorting
	print (k, D[k])

	
('a', 1)
('b', 2)
('c', 3)


##TUPLES
##-------

##Declaration
>>> T = (1, 2, 3, 4) # A 4-item tuple
(1, 2, 3, 4)

>>> T = 0, 'Ni', 1, 2, 3, 4
(0, 'Ni', 1, 2, 3, 4)

>>> T = tuple('spam')
('s', 'p', 'a', 'm')

>>> T = ('abc', 'def', ('efg', 'hij'))
('abc', 'def', ('efg', 'hij'))

##Returning the length
>>> len(T) 
4

## Concatenation
>> T + (5, 6) 
(1, 2, 3, 4, 5, 6)

## Indexing, slicing, and more
>>> T[0] 
1

##Return the index for 4, which is at offset 3
>>> T.index(4)
3

##Occurrences of element 4 in the tuple
>>> T.count(4) # 4 appears once
1

##Iteration, membership
>>> for x in T:
	print (ord(x) * 2)
>>> 's' in T

##Some operations fpr example on lists, don't work for tuples. In that case,
##you have to convert a tuple to list and then back to tuple.
>>> T = ('cc', 'aa', 'dd', 'bb')
>>> tmp = list(T) # Make a list from a tuple's items
>>> tmp.sort() # Sort the list
>>> tmp
['aa', 'bb', 'cc', 'dd']
>>> T = tuple(tmp) # Make a tuple from the list's items
>>> T
('aa', 'bb', 'cc', 'dd')
>>> sorted(T) # Or use the sorted built-in
['aa', 'bb', 'cc', 'dd']

##sample comprehension
>>> [x + 20 for x in T]
[16, 17, 18, 19, 20, 21, 22, 23, 24]

##count the number of a given element
>>> T.count(3)
1

##note that the elements inside a tuple are immutable. A list inside a tuple, for instance, can be changed as usual 
>>> T = (1, 2, [3, 4], 5, 6)
>>> T
(1, 2, [3, 4], 5, 6)
>>> T[0] = -1
...error...
>>> T[2][1] = -3
>>> T
(1, 2, [3, -3], 5, 6)

## FILES
##-------
output = open(r'C:\spam', 'w')   #Create output file ('w' means write)
input = open('data', 'r')  #Create input file ('r' means read)
input = open('data')  #Same as prior line ('r' is the default)
#Adding a + opens the file for both input and output (i.e., you can both read and
#write to the same file object, often in conjunction with seek operations to reposition
#in the file).
aString = input.read()  #Read entire file into a single string
aString = input.read(N)  #Read up to next N characters (or bytes) into a string
aString = input.readline()  #Read next line (including \n newline) into a string
aList = input.readlines()  #Read entire file into list of line strings (with \n)
output.write(aString)  #Write a string of characters (or bytes) into file
output.writelines(aList)  #Write all line strings in a list into file
output.close()  #Manual close (done for you when file is collected)
output.flush()  #Flush output buffer to disk without closing
anyFile.seek(N)  #Change file position to offset N for next operation
for line in open('data'): use line  #File iterators read line by line


#Some things to note about file operations:

#The best to read from a file is not to read, but to use an iterator which automatically
#reads one line at a time in a for loop, list comprehension or other iteration context.

#File content is in strings. It is necessry to convert objects to strings when writing
#to a file. When reading, the input data is in string, which has to be converted again
#as desired.

#It's not necessary to close a file after an operation. Also, python closes any open files
#after the program is terminated. On the other hand, including manual close calls can’t hurt and
#is usually a good idea in larger systems. Also, strictly speaking, this auto-close-oncollection
#feature of files is not part of the language definition, and it may change
#over time. Consequently, manually issuing file close method calls is a good habit
#to form.

#File output is buffered by default, which means that text you write may not be transferred
#from memory to disk immediately—closing a file, or running its flush method,
#forces the buffered data to disk. You can avoid buffering with extra open arguments,
#but it may impede performance. Python files are also random-access on a byte offset
#basis—their seek method allows your scripts to jump around to read and write at
#specific locations.

#file operations
>>> myfile = open('myfile.txt', 'w') # Open for text output: create/empty
>>> myfile.write('hello text file\n') # Write a line of text: string
>>> myfile.write('goodbye text file\n')
>>> myfile.close() # Flush output buffers to disk
>>> myfile = open('myfile.txt') # Open for text input: 'r' is default, 'rb' is for reading binary files
>>> myfile.readline() # Read the lines back
'hello text file\n'
>>> myfile.readline()
'goodbye text file\n'
>>> myfile.readline() # Empty string: end of file
#write methods don’t add the end-of-line, \n character for us, so we must include it to properly
#terminate our lines (otherwise the next write will simply extend the current line in the
#file)

>>> open('myfile.txt').read() # Read all at once into string
'hello text file\ngoodbye text file\n'

>>> print(open('myfile.txt').read()) # User-friendly display
hello text file
goodbye text file

>>> for line in open('myfile.txt'): # Use file iterators, not reads
... print(line)
...
hello text file
goodbye text file

#Storing and parsing python object in files
>>> X, Y, Z = 43, 44, 45 # Native Python objects
>>> S = 'Spam' # Must be strings to store in file
>>> D = {'a': 1, 'b': 2}
>>> L = [1, 2, 3]
>>>
>>> F = open('datafile.txt', 'w') # Create output file
>>> F.write(S + '\n') # Terminate lines with \n
>>> F.write('%s,%s,%s\n' % (X, Y, Z)) # Convert numbers to strings using string expression
>>> F.write('{0}, {1}, {2}'.format(X, Y, Z))  ## OR using format() method
>>> F.write(str(L) + '$' + str(D) + '\n') # Convert and separate with $
>>> F.close()

>>> chars = open('datafile.txt', 'r').read() # Raw string display
>>> chars
"Spam\n43,44,45\n[1, 2, 3]${'a': 1, 'b': 2}\n"
>>> print(chars) # User-friendly display

Spam
43,44,45
[1, 2, 3]${'a': 1, 'b': 2}

>>> parts = open('myFile1.txt', 'r')   #Open the file again, this time, read the first line only
>>> pars = parts.readline()
>>> pars
'43, 44, 45\n'
>>> pars.rstrip()
'43, 44, 45'
>>> pars
'43, 44, 45\n'
>>> pars = pars.rstrip()
>>> pars
'43, 44, 45'
>>> pars = pars.split(',')
>>> pars
['43', ' 44', ' 45']
>>> pars = [int(P) for P in pars]
>>> pars
[43, 44, 45]

>>> line = F.readline()            #to convert the stored dictionary and the list
>>> line
"[1, 2, 3]${'a': 1, 'b': 2}\n"
>>> parts = line.split('$')                      # Split (parse) on $
>>> parts
['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
>>> eval(parts[0])                               # Convert to any object type
[1, 2, 3]
>>> objects = [eval(P) for P in parts]          # Do same for all in list
>>> objects
[[1, 2, 3], {'a': 1, 'b': 2}]

##Writing and reading files using pickle
#Write
>>> D = {'a': 1, 'b': 2}
>>> F = open('datafile.pk', 'wb')
>>> import pickle        #can also use cPickle, which is an optimized version of pickle
>>> pickle.dump(D, F)    #Pickle any object to file
>>> F.close()            #Flush output buffer

#Read
>>> F = open('datafile.pk', 'rb')
>>> import pickle
>>> Z = pickle.load(F)
>>> Z
{'a': 1, 'b': 2}

>>> open('data.pk', 'rb').read()        #bytes in a binary file, read as normal
"(dp0\nS'a'\np1\nI1\nsS'b'\np2\nI2\ns."

#Python’s standard library includes a tool to help to deal with packed binary
#data—the struct module - knows how to both compose and parse packed binary data.
#In a sense, this is another dataconversion tool that interprets strings in files
#as binary data.

>>> F = open('data.bin', 'wb') # Open binary output file
>>> import struct
>>> data = struct.pack('>i4sh', 7, 'spam', 8) # Make packed binary data
>>> data
b'\x00\x00\x00\x07spam\x00\x08'
>>> F.write(data)              # Write byte string
>>> F.close()

>>> F = open('data.bin', 'rb')
>>> data = F.read()             # Get packed binary data
>>> data
b'\x00\x00\x00\x07spam\x00\x08'
>>> values = struct.unpack('>i4sh', data) # Convert to Python objects
>>> values
(7, 'spam', 8)

## There are additional file-like tools in the Python toolset. Also available, to name
## a few, are:

#Standard streams
#Preopened file objects in the sys module, such as sys.stdout

#Descriptor files in the os module
#Integer file handles that support lower-level tools such as file locking

#Sockets, pipes, and FIFOs
#File-like objects used to synchronize processes or communicate over networks

#Access-by-key files known as “shelves”
#Used to store unaltered Python objects directly, by key

#Shell command streams
#Tools such as os.popen and subprocess.Popen that support spawning shell commands
#and reading and writing to their standard streams

## Numeric Types
##---------------

##Declaration
>>> a = 3 # Name created
>>> b = 4

>>> a + 1, a – 1 # Addition (3 + 1), subtraction (3 - 1)
(4, 2)
>>> b * 3, b / 2 # Multiplication (4 * 3), division (4 / 2)
(12, 2.0)
>>> a % 2, b ** 2 # Modulus (remainder), power (4 ** 2)
(1, 16)
>>> 2 + 4.0, 2.0 ** b # Mixed-type conversions
(6.0, 16.0)
##Technically, the results being echoed back here are tuples of two values because the
##lines typed at the prompt contain two expressions separated by commas.


##Ways to display bits than using print or automatic echoes
>>> num = 1 / 3.0
>>> num # Echoes
0.33333333333333331
>>> print(num) # print rounds
0.333333333333
>>> '%e' % num # String formatting expression
'3.333333e-001'
>>> '%4.2f' % num # Alternative floating-point format
'0.33'
>>> '{0:4.2f}'.format(num) # String formatting method (Python 2.6 and 3.0)
'0.33'


##str and repr
##Technically, the difference between default interactive echoes and print corresponds
##to the difference between the built-in repr and str functions:
>>> num = 1 / 3
>>> repr(num) # Used by echoes: as-code form
'0.33333333333333331'
>>> str(num) # Used by print: user-friendly form
'0.333333333333'


##Doing Comparisons
>>> X = 2
>>> Y = 4
>>> Z = 6

>>> X < Y < Z # Chained comparisons: range tests
True
>>> X < Y and Y < Z
True


##Divisions
>>> 10 / 4        ##Classic Division, also known as true division in py3.0
2
>>> 10 // 4       ##Floor Division
2
>>> 10 / 4.0
2.5
>>> 10 // 4.0
2.0

X = Y // Z # Always truncates, always an int result for ints
X = Y / float(Z) # Guarantees float division with remainder


##Floor and Truncation

>>>import math
>>> math.floor(2.5)    #for positive values, floor and trunce is the same
2
>>> math.trunc(2.5)
2
>>> math.floor(-2.5)   #for negative values, the results differ
-3
>>> math.trunc(-2.5)
-2


##Notation and numeric literals
##-----------------------------

>>> 0o1, 0o20, 0o377        ##input in octal, but echoes in decimal by default
(1, 16, 255)
>>> 0o1, hex(0o20), bin(0o377)   ##use functions to echo in desired format, and use oct for octal
(1, '0x10', '0b11111111')
>>> int('64'), int('100', 8), int('40', 16), int('1000000', 2)  ##to echo in int from a specific base, you can supply an optional second argument
(64, 64, 64, 64)
>>> int('0x40', 16), int('0b1000000', 2) # Literals okay too; here 0b as binary, 0o as octal, 0x as hex
(64, 64)
>>> eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000')
(64, 64, 64, 64)
>>> '%o, %x, %X' % (64, 64, 255)
'100, 40, FF'


## Some math functions
##--------------------

>>> import math

# Common constants
>>> math.pi, math.e 
(3.1415926535897931, 2.7182818284590451)

# Sine, tangent, cosine
>>> math.sin(2 * math.pi / 180) 
0.034899496702500969

# Square root
>>> math.sqrt(144), math.sqrt(2) 
(12.0, 1.4142135623730951)

# Exponentiation (power)
>>> pow(2, 4), 2 ** 4 
(16, 16)

# Absolute value, summation
>>> abs(-42.0), sum((1, 2, 3, 4)) 
(42.0, 10)

# Minimum, maximum
>>> min(3, 1, 2, 4), max(3, 1, 2, 4) 
(1, 4)


## Decimal Type
##--------------

>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')

>>> Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')
Decimal('0.00')

>>> import decimal
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.1428571428571428571428571429')

##Changing precision
>>> import decimal
>>> decimal.getcontext().prec = 4
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.1429')

##Changing precision temporarily
>>> import decimal
>>> with decimal.localcontext() as ctx:
        ctx.prec = 4
        decimal.Decimal('1.00') / decimal.Decimal(str(3.00))

Decimal('0.33')

        
## Fraction Type
##---------------
>>> from fractions import Fraction
>>> x = Fraction(1, 3)
>>> y = Fraction(4 ,6)
>>> print x
1/3

##Operations
>>> x + y
Fraction(1, 1)
>>> x * y
Fraction(2, 9)

##Fractions from floating points
>>> Fraction('.25')
Fraction(1, 4)
>>> Fraction('.25') + Fraction('1.25')
Fraction(3, 2)


## Float <-> Fraction conversion
##------------------------------
>>> from fractions import Fraction
>>> f = 2.5
>>> f.as_integer_ratio()           ##float to fraction
(5, 2)
>>> z = Fraction(*f.as_integer_ratio())    ##float to fraction 
>>> z
Fraction(5, 2)
>>> float(z)       ##fraction to float
2.5
>>> Fraction.from_float(1.75)            ##float value to fraction
Fraction(7, 4)
>>> Fraction(*(1.75).as_integer_ratio())    ##float value to fraction
Fraction(7, 4)


## Sets
##------

##declaration
>>> x = set('abcde')
>>> y = set('bdxyz')

##Set operations
>>> 'e' in x    # Membership
True
>>> x – y   # Difference
set(['a', 'c', 'e'])
>>> x | y   # Union
set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])
>>> x & y   # Intersection
set(['b', 'd'])
>>> x ^ y   # Symmetric difference (XOR) # Who is in one but not both?
set(['a', 'c', 'e', 'y', 'x', 'z'])
>>> x > y, x < y    # Superset, subset
(False, False)

##Alternate set operations
>>> z = x.intersection(y) # Same as x & y
>>> z
set(['b', 'd'])

>>> z.add('SPAM') # Insert one item
>>> z
set(['b', 'd', 'SPAM'])

>>> z.update(set(['X', 'Y'])) # Merge: in-place union
>>> z
set(['Y', 'X', 'b', 'd', 'SPAM'])

>>> z.remove('b') # Delete one item
>>> z
set(['Y', 'X', 'd', 'SPAM'])

>>> S = set([1, 2, 3])
>>> S | set([3, 4]) # Expressions require both to be sets
set([1, 2, 3, 4])

>>> S | [3, 4]
TypeError: unsupported operand type(s) for |: 'set' and 'list'

>>> S.union([3, 4]) # But their methods allow any iterable
set([1, 2, 3, 4])

>>> S.intersection((1, 3, 5))
set([1, 3])

>>> S.issubset(range(-5, 5))
True

>>> for item in set('abc'): print(item * 3)
...
aaa
bbb
ccc


## Types are Dynamic
##-------------------

#In python, types are determined automatically by object(s) assigned to variables.
#So types are determined by objects, not variables. Also, if variables are
#assigned in the following way:

#Variables with single values, such as strings or integers.
>>> a = 3
>>> b = a
>>> a
3
>>> a = 'ko'
>>> b
3
>>> a
'ko'
>>> b
3

##with lists. Here, L1 isn't changed, but only a component of the object that it is linked to.
>>> L1 = [2, 3, 4]      # A mutable object
>>> L2 = L1         # Make a reference to the same object
>>> L1[0] = 24      # An in-place change
>>> L1          # L1 is different
[24, 3, 4]
>>> L2      # But so is L2!
[24, 3, 4]


##To make a copy of a variable with list to another variable
>>> L1 = [2, 3, 4]
>>> L2 = L1[:]    #Make a copy of L1
>>> L1[0] = 24

>>> L1
[24, 3, 4]
>>> L2
[2, 3, 4]


##To make a copy using the copy module
import copy
X = copy.copy(Y) # Make top-level "shallow" copy of any object Y
X = copy.deepcopy(Y) # Make deep copy of any object Y: copy all nested parts


##Reference and equality
##----------------------
>>> L = [1, 2, 3]
>>> M = L # M and L reference the same object
>>> L == M # Same value
True
>>> L is M # Same object
True

>>> L = [1, 2, 3]
>>> M = [1, 2, 3] # M and L reference different objects
>>> L == M # Same values
True
>>> L is M # Different objects
False

#Python caches small integers and values in menory for later use, so
>>> X = 42
>>> Y = 42 # Should be two different objects
>>> X == Y
True
>>> X is Y # Same object anyhow: caching at work!
True


#To get the number of references for a value in a memory
>>> import sys
>>> sys.getrefcount(1) # 837 pointers to this shared piece of memory
837



## Properties of types in python, commonalities
##----------------------------------------------

## Object Classifications

#Object type     Category        Mutable?

#Numbers (all)   Numeric         No
#Strings         Sequence        No
#Lists           Sequence        Yes
#Dictionaries    Mapping         Yes
#Tuples          Sequence        No
#Files           Extension       N/A
#Sets            Set             Yes
#frozenset       Set             No
#bytearray (3.0) Sequence        Yes

# Lists, dictionaries, and tuples can hold any kind of object.
# Lists, dictionaries, and tuples can be arbitrarily nested.
# Lists and dictionaries can dynamically grow and shrink.

#In sequence objects, there can be nested objects as deep as you'd like them to be:
>>> L = ['abc', [(1, 2), ([3, 1], 4)], 5]   
>>> L[0]
'abc'                     #string object within a list
>>> L[1]
[(1, 2), ([3, 1], 4)]             #tuples and nested list within a list
>>> L[1][0]
(1, 2)
>>> L[1][0][1]
2
>>> L[1][1]
([3, 1], 4)
>>> L[1][1][0]                    #accessing by the appropriate index
[3, 1]
>>> L[1][1][0][1]
1


## Reference and copy objects.

>>> X = [1, 2, 3]
>>> L = ['a', X, 'b']              #embed X as an object
>>> D = {'x':X, 'y':2}             #embed X as a value for a key

>>> D['y']
2
>>> D['y'] is X[1]
True                                #caching at work!

>>> X                               #echo the variables
[1, 2, 3]
>>> L
['a', [1, 2, 3], 'b']
>>> D
{'y': 2, 'x': [1, 2, 3]}

>>> X[0] = -1                        #Now, change X
>>> X
[-1, 2, 3]
>>> L
['a', [-1, 2, 3], 'b']
>>> D
{'y': 2, 'x': [-1, 2, 3]}            #changes all the references

#If copies are to be instead of references
>>> L = [1, 2, 3]                  #first declare the original variables
>>> D = {'a':1, 'b':2}
# Slice expressions with empty limits (L[:]) copy sequences.
# The dictionary and set copy method (X.copy()) copies a dictionary or set.
# Some built-in functions, such as list, make copies (list(L)).
# The copy standard library module makes full copies.
>>> A = L[:]           #Use the slice expression to copy a list or use list(L), instead of A = L; which creates a reference              
>>> B = D.copy()       #Use the copy() method to copy a dictionary. Also use the same method for sets; instead of B = D

>>> A                   #The copied values
[1, 2, 3]
>>> B
{'a': 1, 'b': 2}

>>> A[1] = 'Ni'          #Now change A and B
>>> B['c'] = 'spam'

>>> A                    #A and B have changed
[1, 'Ni', 3]
>>> B
{'a': 1, 'c': 'spam', 'b': 2}

>>> L                     #L and D are unchanged
[1, 2, 3]
>>> D
{'a': 1, 'b': 2}

  #Previous example
>>> X = [1, 2, 3]

>>> L = ['a', X[:], 'b']      #make a copy of the list X as an element
>>> L
['a', [1, 2, 3], 'b']

>>> D = {'x':X[:], 'b':2}     #ditto
>>> D
{'x': [1, 2, 3], 'b': 2}

>>> X[1] = -1                 #change an element of original X
>>> L                         #L and D are unchanged
['a', [1, 2, 3], 'b']
>>> D
{'x': [1, 2, 3], 'b': 2}
#Be advised, that the slice copy and the copy() method only perform a shallow copy. They
#don't copy nested objects. For that use deepcopy() from copy module
#import copy
#X = copy.deepcopy(Y)

## Comparisons, equality and truth

#Similar objects can be compared for their values
>>> L1 = [1, ('a', 3)] # Same value, unique objects
>>> L2 = [1, ('a', 3)]
>>> L1 == L2, L1 is L2 # Equivalent? Same object?
(True, False)

>>> S1 = 'spam'
>>> S2 = 'spam'
>>> S1 == S2, S1 is S2
(True, True)              #python chaches smaller values for optimization

>>> S1 = 'a longer string'
>>> S2 = 'a longer string'
>>> S1 == S2, S1 is S2
(True, False)              #caching is disabled for larger values

#Relative magnitude comparisons are also applied recursively to nested data structures
>>> L1 = [1, ('a', 3)]
>>> L2 = [1, ('a', 2)]
>>> L1 < L2, L1 == L2, L1 > L2 # Less, equal, greater: tuple of results
(False, False, True)
#The result of the last line is really a tuple of three objects—the results of
#the three expressions typed (an example of a tuple without its enclosing parentheses).

## In general, Python compares types as follows:

#Numbers are compared by relative magnitude.

#Strings are compared lexicographically, character by character ('abc' < 'ab')

#Lists and tuples are compared by comparing each component from left to right.

#Dictionaries compare as equal if their sorted (key, value) lists are equal. Relative
#magnitude comparisons are not supported for dictionaries in Python 3.0, but they
#work in 2.6 and earlier as though comparing sorted (key, value) lists.
#eg:
>>> D1 = {'a':1, 'b':2}
>>> D2 = {'a':1, 'b':3}
>>> D1 == D2
False
>>> D1 < D2
True
#Nonnumeric mixed-type comparisons (e.g., 1 < 'spam') are errors in Python 3.0.
#They are allowed in Python 2.6, but use a fixed but arbitrary ordering rule. By
#proxy, this also applies to sorts, which use comparisons internally: nonnumeric
#mixed-type collections cannot be sorted in 3.0.



## The meaning of True and False and the None object

#Each object is either true or false, as follows:
# Numbers are true if nonzero.
# Other objects are true if nonempty.

# Object          Value

# "spam"          True
# ""              False
# []              False
# {}              False
# 1               True
# 0.0             False
# None            False


#None, is always considered to be false. None is the only value of a special data
#type in Python and typically serves as an empty placeholder.

#To preallocate a 100-item list such that you can add to any of the 100 offsets,
#you can fill it with None objects:
>>> L = [None] * 100
>>>
>>> L
[None, None, None, None, None, None, None, ... ]

#This doesn’t limit the size of the list (it can still grow and shrink later), but simply
#presets an initial size to allow for future index assignments. You could initialize a list
#with zeros the same way.

## The bool type
# When used explicitly in truth test code, the words True and False are equivalent
# to 1 and 0, but they make the programmer’s intent clearer.

# Results of Boolean tests run interactively print as the words True and False, instead
# of as 1 and 0, to make the type of result clearer.

#Python also provides a bool builtin function that can be used to test the Boolean value of an object
>>> bool(1)
True
>>> bool('spam')
True
>>> bool({})
False


## Checking for type objects
#Each core type has a new built-in name added to support type customization through
#object-oriented subclassing: dict, list, str, tuple, int, float, complex, bytes, type,
#set, and more.

#The types standard library module provides additional type names for types that are not
#available as built-ins(e.g., the type of a function) this module also includes synonyms
#for built-in type names it is possible to do type tests with the isinstance function.
#For example, all of the following type tests are true:

type([1]) == type([]) # Type of another list
type([1]) == list # List type name
isinstance([1], list) # List or customization thereof
import types # types has names for other types
def f(): pass
type(f) == types.FunctionType

#Because types can be subclassed in Python, the isinstance technique is generally
#recommended

#Repetition
>>> L = [4, 5, 6]
>>> X = L * 4 # Like [4, 5, 6] + [4, 5, 6] + ...
>>> Y = [L] * 4 # [L] + [L] + ... = [L, L,...]

>>> X
[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
>>> Y
[[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]

>>> L[1] = 0 # Impacts Y but not X
>>> X
[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
>>> Y
[[4, 0, 6], [4, 0, 6], [4, 0, 6], [4, 0, 6]]

#Cyclic data structures
>>> L = ['grail'] # Append reference to same object
>>> L.append(L) # Generates cycle in object: [...]
>>> L
['grail', [...]]

#Changing immutable data structures
T = (1, 2, 3)
T[2] = 4 # Error!

T = T[:2] + (4,) # OK: (1, 2, 4)   #keep everything up to offset 1, add 4 to offset 2

#For and while loops intro
#-------------------------

##Simple while with print
>>> while(x>0):
	print 'spam!'*x
	x -= 1

	
spam!spam!spam!spam!
spam!spam!spam!
spam!spam!
spam!


##Simple for with print
>>> for c in 'spam':
print(c.upper())

S
P
A
M

##Modifying a list with for
>>> squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
>>> squares
[1, 4, 9, 16, 25]

##Appending an empty list with for
>>> squares = []
>>> for x in [1, 2, 3, 4, 5]: # This is what a list comprehension does
squares.append(x ** 2) # Both run the iteration protocol internally
#checking
>>> squares
[1, 4, 9, 16, 25]



PART II EXERCISES
-----------------
1.
>>> 2**16  #exponent 16
65536

>>> 2/5, 2/5.0  #return a tuple with a pair of results of classic divisions
(2/5, 2//5.0)

>>> "spam" + "eggs"   #string concatenation
'spameggs'
>>> S = "ham"   #Assigning 'ham' string literal to a variable S
>>> "eggs" + S  #Concatenation of string literal with S
>>> S * 5     #return a string with repetition of S five times
>>> S[:0]   #empty string
>>> "green %s and %s" % ("eggs", S)   #string expression, echoes: 'green eggs and ham'
>>> 'green {0} and {1}'.format('eggs', S)    #string format method, echoes: 'green eggs and ham'
>>> ('x',)[0]    #tuple of single element, echoes the value at index 0
'x'
>>> ('x', 'y')[1]     #tuple of two elements, echoes the value at index 1
'y'
>>> L = [1,2,3] + [4,5,6]  #concatenation of lists
>>> L, L[:], L[:0], L[-2], L[-2:]     #returns a tuple of lists
([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [], 5, [5, 6])
>>> ([1,2,3]+[4,5,6])[2:4]
[3, 4]
>>> [L[2], L[3]]
[3, 4]
>>> L.reverse();L     #reverse L and then echo L
[6, 5, 4, 3, 2, 1]
>>> L.sort();L      #sort L and then echo L
[1, 2, 3, 4, 5, 6]
>>> L.index(4)      #echoes the index value of first occurrence of 4 in L
3
>>> {'a':1, 'b':2}['b']    #echoes the value of the key b
2
>>> D = {'x':1, 'y':2, 'z':3}    #creates a dictionary D with the entries
>>> D['w'] = 0                  #Add another key with value 0
>>> D['x'] + D['w']     #echo the result of the expression
1
>>> D[(1, 2, 3)] = 4            #Add a tuple as a key with value 4
>>> list(D.keys()), list(D.values()), (1,2,3) in D     
(['y', 'x', 'z', 'w', (1, 2, 3)], [2, 1, 3, 0, 4], True)
>>> [[]], ["",[],(),{},None]
([[]], ['', [], (), {}, None])

2.
a. Out of bound error
b. python scales the slicing indices, so it returns the full list
c. L[3:1] = ['?']
L
[0, 1, 2, 3, '?', 4]

3.
>>> L = [0, 1, 2, 3]
>>> L[2] = []
>>> L
[0, 1, [], 3]
>>> L[2:3] = []
>>> L
[0, 1, 3]
>>> delL[0]

4.
>>> X = 'spam'
>>> Y = 'eggs'
>>> X, Y = Y, X      #assignments- objects on the right are the assigned values for the objects on the left. The assignment is also basad on the position indicated by commas.
>>> X, Y
('eggs', 'spam')

5.
>>> D = {}
>>> D[1] = 'a'
>>> D[2] = 'b'
>>> D[(1, 2, 3)] = 'c'
>>> D
{1: 'a', 2: 'b', (1, 2, 3): 'c'}    #just simple dictionary assignments and out of bounds retrival

6.
>>> D = {'a':1, 'b':2, 'c':3}
>>> D['a']
1
>>> D['d']
Traceback (innermost last):
File "<stdin>", line 1, in ?
KeyError: d
>>> D['d'] = 4
>>> D
{'b': 2, 'd': 4, 'a': 1, 'c': 3}
>>>
>>> L = [0, 1]
>>> L[2]
Traceback (innermost last):
File "<stdin>", line 1, in ?
IndexError: list index out of range
>>> L[2] = 3
Traceback (innermost last):
File "<stdin>", line 1, in ?
IndexError: list assignment index out of range

7.
a. The overloaded '+' operator doesn't work on mixed types.
b. The concatenation '+' doesn't won dictionaries, as they're not iterable or sequencies.
c. The append method works only for lists. The keys methods works only on dictionaries.
d. Slicing and concatenation always return the same type of object as they are processed.

8.
S = "spam"
S[0][0][0][0][0] gives 's'
If S = ['s', 'p', 'a', 'm']
S[0][0][0][0][0] gives 's' too, but only if the elements are strings.

9.
>>> S = "spam"
>>> S = S[0] + 'l' + S[2:]
>>> S
'slam'
>>> S = S[0] + 'l' + S[2] + S[3]
>>> S
'slam'

10.
Ds = {'name':('first', 'middle', 'last'), 'age':'?', 'job':'?'}
Ds['name'][1]
'middle'

11.
file = open('myfile.txt', 'w')
file.write('Hello file World\n')
#alternative method
#import pickle
#pickle.dump('Hello World\n', file)
file.close()
file = open('myfile.txt', 'r')
data = file.readline()
data = data.rstrip()
data
#alternative method
#import pickle
#data = pickle.load(file)
#data


## Introducing Python Statements
##-------------------------------

#Statement rule special cases

a = 1; b = 2; print(a + b) # Three statements on one line

mlist = [111,     #to continue a list literal
         222,
         333]

X =(A + B +       #inserting a left parenthesis allows you to drop down to the
    C + D)        #next line and continue your statement

if (A == 1 and    #simply wrap it in parentheses to continue it on the next line
B == 2 and
C == 3):
print('spam' * 3)

if x > y: print(x)     #works only for single-line if statements, single-line loops, and so on

>>> while True:                             #Simple interactive loop
        data = raw_input("Enter code: ")
        if data == 'stop': break
        print (data.upper())

>>> while True:                             #only works if the input are digits
        reply = input('Enter text:')
        if reply == 'stop': break
        print(int(reply) ** 2)
    print('Bye')


>>> 
while True:                                 #With string methods to check the input
        data = raw_input('Enter Text:')
        if data == 'stop': break
        elif not data.isdigit():
                print(data.upper()*4)
        else: print(int(data) ** 2)
print('Bye')


>>>                                          #Inserting more conditions
while True:
        data = raw_input('Enter Text:')
        if data == 'stop': break
        elif not data.isdigit():
                print(data.upper() * 4)
        else:
                num = int(data)
                if num < 20:
                        print('low value')
                else:
                        print(num ** 2)
print('Bye')


>>>                                          
while True:                                     #using exception handlers
        data = raw_input('Enter Text:')
        if data == 'stop': break
        try:
                num = int(data)
        except:
                print(data.upper()*4)
        else:
                print(num ** 2)
print('Bye')



## Assignments, Expression and Prints
##------------------------------------

spam = 'spam
spam, ham = 'spam', 'ham'
[spam, ham] = ['yum', 'YUM']
a, b, c, d = 'spam'
spam = ham = 'lunch'
spams += 42

##Sequence assignments

>>> nudge = 1
>>> wink = 2
>>> A, B = nudge, wink                # tuple assignment
>>> A, B                              # Like A = nudge; B = wink
(1, 2)
>>> [C, D] = [nudge, wink]            # List assignment
>>> C, D
(1, 2)

>>> [a, b, c] = (1, 2, 3)             # Assign tuple of values to list of names
>>> a, c
(1, 3)
>>> (a, b, c) = "ABC"                 # Assign string of characters to tuple
>>> a, c
('A', 'C')

>>> string = 'SPAM'
>>> a, b, c, d = string               # Same number on both sides
>>> a, d
('S', 'M')
>>> a, b, c = string                  # Error - too many values to unpack 
 
>>> a, b, c = string[0], string[1], string[2:]        # Index and slice
>>> a, b, c
('S', 'P', 'AM')

>>> a, (b, c) = list(string[:2]), list(string[2:])         # Slice and concatenate, to return a combined list, which is assigned to the sequence
>>> a, b, c
(['s', 'p'], 'a', 'm')

>>> (a, b), c = string[:2], string[2:]                # nested sequences
>>> a, b, c
('S', 'P', 'AM')

>>> ((a, b), c) = ('SP', 'AM')           # Paired by shape and position
>>> a, b, c
('S', 'P', 'AM')

>>> seq
[1, 2, 3, 4]

>>> a, b = seq[0], seq[1:]              # First, rest
>>> a, b
(1, [2, 3, 4])

>>> a, b = seq[:-1], seq[-1]            # Rest, last
>>> a, b
([1, 2, 3], 4)


# The assignment technique also works for loops, which we'll see more in detail

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ...       # Simple tuple assignment

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ... # Nested tuple assignment

# Sequence-unpacking assignments using range() to assign integer series
>>> red, green, blue = range(3)
>>> red, blue
(0, 2)
>>> range(3) # returns a list
[0, 1, 2]

# Assignment by using a while loop, tuple assignment at work is for splitting a sequence into
# its front and the rest in loops like this
>>> while L:
... front, L = L[0], L[1:]         # See next section for 3.0 alternative
... print(front, L)
...
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []

# The tuple assignment in the loop here could be coded as the following two lines instead,
# but it’s often more convenient to string them together:
... front = L[0]
... L = L[1:]

# Notice that this code is using the list as a sort of stack data structure, which can often
# also be achieved with the append and pop methods of list objects; here, front =
# L.pop(0) would have much the same effect as the tuple assignment statement, but it
# would be an in-place change. We’ll learn more about while loops, and other (often
# better) ways to step through a sequence with for loops


## Multiple Target assignments

>>> a = b = c = 'spam'
>>> a, b, c
('spam', 'spam', 'spam')

>>> c = 'spam'      # equivalent to the previous step
>>> b = c
>>> a = b

# When using variables as counters, initialize them to 0 first

>>> a = b = 0
>>> b = b + 1
>>> a, b
(0, 1)

# Similarly, when we have to careful when assigning an empty mutable object to multiple variables

>>> a = b = []
>>> b.append(42)
>>> a, b
([42], [42])

>>> a = []     # Assign individually
>>> b = []
>>> b.append(42)
>>> a, b
([], [42])

## Augmented assignments

X = X + Y   # can be written as 
X += Y      # Newer augmented form

X += Y    X &= Y    X -= Y    X |= Y

X *= Y    X ^= Y    X /= Y    X >>= Y

X %= Y   X <<= Y   X **= Y    X //= Y

>>> S = "spam"
>>> S += "SPAM"       # Implied augmented concatenation for strings
>>> S
'spamSPAM'

>>> L = [1, 2]
>>> L = L + [3]          # Concatenate: slower
>>> L
[1, 2, 3]
>>> L.append(4)          # Faster, but in-place
>>> L
[1, 2, 3, 4]

>>> L = L + [5, 6]
>>> L
[1, 2, 3, 4, 5, 6]
>>> L.extend([7, 8])
>>> L
[1, 2, 3, 4, 5, 6, 7, 8]
>>> L += [9 ,10]             # Mapped to L.extend()
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# the += is an in-place change for lists; thus, it is not exactly like + concatenation,
# which always makes a new object

>>> L = [1, 2]
>>> M = L               # L and M reference the same object
>>> L = L + [3, 4]      # Concatenation makes a new object
>>> L, M                # Changes L but not M
([1, 2, 3, 4], [1, 2])

>>> L = [1, 2]
>>> M = L
>>> L += [3, 4]         # But += really means extend
>>> L, M                # M sees the in-place change too!
([1, 2, 3, 4], [1, 2, 3, 4])

## Variable Name Rules

# Syntax: (underscore or letter) + (any number of letters, digits, or underscores)
      # _spam, spam, and Spam_1 are legal names, but 1_Spam, spam$, and @#! are not.
# Case matters: SPAM is not the same as spam
# Reserved words are off-limits

# Other Naming Conventions
      # Names that begin with a single underscore (_X) are not imported by a from module import * statement
      # Names that have two leading and trailing underscores (__X__) are system-defined
      # Names that begin with two underscores and do not end with two more (__X) are localized (“mangled”) to enclosing classes
      # The name that is just a single underscore (_) retains the result of the last expression when working interactively.


## Print statements, stream redirection

print x, y    #Print objects’ textual forms to sys.stdout; add a space between the items
              # and an end-of-line at the end

print x, y,   # Same, but don’t add end-of-line at end of text

print >> afile, x, y    # Send text to myfile.write, not to sys.stdout.write

>>> print x, y
a b
>>> print x, y; print x, y    # with EOL after the first print
a b
a b
>>> print x, y,; print x, y   # with no EOL after the first print
a b a b

# Stream redirection
>>> print(x, y)               # print x, y

>>> import sys
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')  # equivalent, which happens internally

>>> import sys
temp = sys.stdout                               # save for restoring stream direction later
sys.stdout = open('log.txt', 'a')               # redirects print to a file
print(x, y, x)                                  # shows up in log.txt
print('spam')                                   # print again goes to the file, log.txt
print(1, 2, 3)
sys.stdout.close()                              # flush output to disk
sys.stdout = temp                               # restore original stream direction

>>> print('back here')
back here                                       # print shows up again
>>> print(open('log.txt')).read()
spam
1 2 3
>>> open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n')     # Send to file manually



## if Tests and Syntax Rules
## --------------------------

>>> x = 'killer rabbit'    # standard if, else if (elif) else condition branching
>>> if x == 'roger':
... print("how's jessica?")
... elif x == 'bugs':
... print("what's up doc?")
... else:
... print('Run away! Run away!')
...
Run away! Run away!


>>> choice = 'ham'          # choice style based construction using a dictionary
>>> print({'spam':1.25,
	'ham':1.99,
       'eggs':0.99,
       'bacon':1.10}[choice])
1.99


>>> choice = 'ham'          # choice style based construction using if-elif-else
if choice == 'spam':
	print(1.25)
elif choice == 'ham':
	print(1.99)
elif choice == 'eggs':
	print(0.99)
elif choice == 'bacon':
	print(1.10)
else:
	print('None')

1.99


>>> branch = {'spam': 1.25,       # emulating choice by using the get() method
... 'ham': 1.99,
... 'eggs': 0.99}
>>> print(branch.get('spam', 'Bad choice'))
1.25
>>> print(branch.get('bacon', 'Bad choice'))
Bad choice



>>> choice = 'ham'                 # emulating choice by using if, in, else branching
>>> if choice in branch:
        print(branch[choice])
else:
        print('Error')


1.99


# Indentation of code, simple example
>>> x = 'SPAM'
if 'rubbery' in 'shrubbery':       
	print(x * 8)
	x += 'NI'
	if x.endswith('NI'):
		x *= 2
		print(x)

		
SPAMSPAMSPAMSPAMSPAMSPAMSPAMSPAM
SPAMNISPAMNI


>>>
L = ["Good",
"Bad",
"Ugly"]                         # Open pairs may span lines

>>>
if (a == b and c == d and
d == e and e == f):
print('new')                    # But parentheses usually do too
		
>>>
x = 1; y = 2; print(x)          # More than one simple statement

# triple quoted comments and line breaks
>>> S = """
aaa
bbb
ccc
"""
>>> S
'\naaa\nbbb\nccc\n'
>>> S = ('aaa'
     'bbb'
     'ccc')
>>> S
'aaabbbccc'               # here, the strings are concatenated

# Truth Tests

>>> 2 < 3, 3 < 2          # Magnitude comparison return Tru or False as results
(True, False)

# or Operations for Truth
>>> 2 or 3, 3 or 2        # objects from left to right are evaluated and the first one that is true is returned. Here, both are true, so the left one is returned. Return left operand if true
(2, 3)

>>> [] or 3               # Else, return right operand (true or false). Here 3 in non-zero and is true
3

>>> [] or {}              # Return left operand if false. Here the first [] returns false, so it returns the second entry
{}

>>> {} or []              # Likewise
[]

# and Operations for Truth
>>> 2 and 3, 3 and 2       # Return left operand if false
(3, 2)                     # Else, return right operand (true or false)
>>> [] and {}
[]
>>> 3 and []
[]

# Here, both operands are true in the first line, so Python evaluates both sides and returns
# the object on the right. In the second test, the left operand is false ([]), so Python stops
# and returns it as the test result. In the last test, the left side is true (3), so Python evaluates
# and returns the object on the right (which happens to be a false []).

# The if/else Ternary Expression

>>>
if X:
        A = Y
else:
        A = Z

        
>>>
A = Y if X else Z       # Same effect as the code above, short-circuit equivalent

>>> A = 't' if 'spam' else 'f'     # Other examples
>>> A
't'
>>> A = 't' if '' else 'f'
>>> A
'f'

>>> A = [Z, Y][bool(X)]     # Here, A = Y
>>> ['f', 't'][bool('')]    # '' is empty, so bool returns 0
'f'
>>> ['f', 't'][bool('spam')]
't'
 

# More Boolean examples

>>> X = A or B or C or None         # sets X to the first nonempty object among A, B anc C, or to None if all of them are empty
>>> A = B = C = 0
>>> A
0
>>> X = A or B or C or None
>>> X
>>> print (X)
None

>>> X = A or default            # sets X to A if A is true or nonempty, or to default otherwise


if f1() or f2(): ...

# Here, if f1 returns a true (or nonempty) value, Python will never run f2. To guarantee
# that both functions will be run, call them before the or:

tmp1, tmp2 = f1(), f2()
if tmp1 or tmp2: ...

# This can be used to emulate the if/else statement behaviour

A = ((X and Y) or Z)

# This works, but there is a catch—you have to be able to assume that Y will be Boolean
# true. If that is the case, the effect is the same: the and runs first and returns Y if X is true;
# if it’s not, the or simply returns Z. In other words, we get “if X then Y else Z.”


## while and for Loops
## -------------------

>>> while True:
... print('Type Ctrl-C to stop me!')            # example of an infinite loop using while


>>> x = 'spam'
>>> while x:                                    # while x is not empty, print x
	print(x + ' '),                         # remove EOL after a print line with (,). 
	x = x[1:]

spam  pam  am  m 



>>> a = 0; b = 10
>>> while a < b:                                 # One way to code counter loops
	print(str(a) + ' '),
	a += 1

0  1  2  3  4  5  6  7  8  9


# break, continue, pass and Loop else

# break
# Jumps out of the closest enclosing loop (past the entire loop statement)

# continue
# Jumps to the top of the closest enclosing loop (to the loop’s header line)

# pass
# Does nothing at all: it’s an empty statement placeholder

# Loop else block
# Runs if and only if the loop is exited normally (i.e., without hitting a break)

# while Example:
while <test1>:
        <statements1>
        if <test2>: break               # Exit loop now, skip else
        if <test3>: continue            # Go to top of loop now, to test1
else:
        <statements2>                   # Run if we didn't hit a 'break'
        

while True:
        pass                            # Just an empty placeholder, that is used when the syntax requires
                                        # a statement, but you have nothing useful to say
                                        
# continue Example
x = 10
while x:
        x = x - 1
        if x % 2 != 0: continue
        print(str(x)+ ' '),
        
8  6  4  2  0


# break Example
>>> while True:
	name = raw_input('Enter name: ')
	if name == 'stop': break                     # breaks out of while Loop
	age = raw_input('Enter age: ')
	print('Hello', name, '=>', int(age) ** 2)


# using a simple Loop construct to check for a prime. Breaks when a factor is found
y = int(raw_input('Enter num: '))         
x = y // 2 # For some y > 1
while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break # Skip else
    x -= 1
else: # Normal exit
    print(y, 'is prime')


# More on the loop else

found = False
while x and not found:
        if match(x[0]):
                print('Ni')
                found = True
                break
        else:
                x = x[1:]               # slice off and repeat
        if not found:
                print('not found')


while x:                                # concise, without the found flag
        if match(x[0]):
                print('Ni')
                break
        x = x[1:]
else:
        print('Not found')


# for Loops

for <target> in <object>:               # Assign object items to target
        <statements>
        if <test>: break                # Exit loop now, skip else
        if <test>: continue             # Go to top of loop now
else:
        <statements>                    # If we didn't hit a 'break'

                
# Example:

>>> for x in ['spam', 'eggs', 'ham']:
            print(str(x) + ' '),

spam  eggs  ham


# another Example
>>> sum = 0
>>> for x in [1, 2, 3, 4]:
        sum += x

>>> sum
10
        
# other examples
>>> prod = 1
>>> for item in [1, 2, 3, 4]: prod *= item
...
>>> prod
24              
-------------------------------------
>>> S = 'lumberjack'                    # using a string
>>> T = ('and', "I'm", 'okay')
>>> for x in S:
        print(x + ' '),

l  u  m  b  e  r  j  a  c  k
-------------------------------------
>>> for x in T:                         # using a tuple
        print(x + ''),

and I'm okay

-------------------------------------
>>> T = [(1, 2), (3, 4), (5, 6)]
>>> for (a, b) in T:                    # using another tuple
        print(a, b)


(1, 2)                  # Here, the first time through the loop is like writing (a,b) = (1,2), the second time is
(3, 4)                  # like writing (a,b) = (3,4), and so on
(5, 6)
-------------------------------------
>>> D = {'a':1, 'b':2, 'c':3}
>>> for key in D:
        print(key, '=>', D[key])

('a', '=>', 1)
('c', '=>', 3)
('b', '=>', 2)
-------------------------------------
>>> D.items()
[('a', 1), ('c', 3), ('b', 2)]
>>> for((key, value) in D.items()):
        print(key, '=>', value)

('a', '=>', 1)
('c', '=>', 3)
('b', '=>', 2)
-------------------------------------
>>> T
[(1, 2)(3, 4)(5, 6)]

>>> for both in T:
        a, b = both
        print(a, b)

(1, 2)
(3, 4)
(5, 6)

-------------------------------------
>>> ((a, b), c) = ((1, 2), 3) # Nested sequences work too
>>> a, b, c
(1, 2, 3)

#nested structures may be automatically unpacked this way in a for

>>> for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)

(1, 2, 3)
(4, 5, 6)

>>> for ((a, b), c) in [([1, 2], 3),['XY', 6]]: print(a, b, c)

(1, 2, 3)                             # Likewise
('X', 'Y', 6)
-------------------------------------
items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for key in test:
        for item in items:
                if item == key:
                        print(key, 'was found')
                        break
                else:
                        print(key, 'not found')

((4, 5), 'not found')
((4, 5), 'not found')
((4, 5), 'was found')
(3.1400000000000001, 'not found')
(3.1400000000000001, 'not found')
(3.1400000000000001, 'not found')
(3.1400000000000001, 'not found')
--------------------------------------------------------
>>> for key in tests: # For all keys
        if key in items: # Let Python check for a match
            print(key, "was found")
        else:
            print(key, "not found!")

(4, 5) was found
3.14 not found!                        
--------------------------------------------------------
# using for in set like list construction, using intersection
>>>
res = []                           
seq1 = 'spam'
seq2 = 'scam'
for x in seq1:
        if x in seq2:
                res.append(x)
print(res)

['s', 'a', 'm']
--------------------------------------------------------
# using loops to read files

File = open('test.txt', 'r')
print(file.read())

File = open('test.txt', 'r')
while True:
        char = File.read(1)       # read by character
        if not char: break
        print(char)

for char in open('test.txt', 'r').read():
        print(char)

File = open('test.txt')
while True:
        line = File.readline()     # read by lines
        if not Line: break
        print(str(Line) + ''),     # Line already has a \n

chunk = open('file.txt', 'r')
while True:
        chunk = File.read(10)      # read by 10-byte chunks
        if not chunk: break
        print(str(chunk) + ''),
        
for line in open('test.txt', 'r').readlines():     # this loads the file into memory all at once into a line string list, may not work for very large files
        print(str(line) + ''),

for line in open('text.txt', 'r'):         # uses an iterator to read one line at each loop iteration, more useful for reading large files
        print(str(line) + ''),

# using range()
>>> range(5), range(2, 5), range(0, 10, 2)
([0, 1, 2, 3, 4, 5], [2, 3, 4], [0, 2, 6, 8])     # skips the upper limit

>>> range(-5, 5)
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

>>> range(-5, 5, -1)

--------------------------------
for i in range(3):                # range to generate the appropriate number of integers
        print(i, 'Pythons')
        
(0, 'Pythons')
(1, 'Pythons')
(2, 'Pythons')

-----------------------------------
X = 'spam'                         # A simple iteration
for item in X: print(item + ''),

s p a m
-------------------------------
X = 'spam'
i = 0                     
while i < len(X):                   # while loop iteration
        print(X[i] + ''),
        i += 1

s p a m
--------------------------------
X = 'spam'                                # above technique using for
for i in range(len(X)): print(X[i] + ''),

s p a m
-------------------------------

>>> S = 'abcdefghijk'                   # using range to skip items while iterating
>>> range(0, len(S), 2)
[0, 2, 4, 6, 8]

>>> for i in range(0, len(S), 2):
        print(S[i] + ''),

a c e g i k

-------------------------------
>>> S = 'abcdefghijk'                # using slice to skip items in the sequence. advantage to using range here instead is that it does not copy the string and does not create a list, saves memory
>>> for i in S[::2]:
        print (i + ''),

a c e g i k
------------------------------
>>> L = [1, 2, 3, 4, 5]              # using range with for to change a list, by adding 1 to each element
>>> for i in range(len(L)):
        L[i] += 1
>>> L
[2, 3, 4, 5, 6]
----------------------------
>>> L = [1, 2, 3, 4, 5]              # using while to change a list, by adding 1 to each element
>>> while i < len(L):
        L[i] += 1
        i += 1
>>> L
[2, 3, 4, 5, 6]
----------------------------
[x+1 for x in L]                # using list comprehension to achieve simiar result as above, but this won't be an in-place change
        
----------------------------

# using zip function with for

>>> T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)   
>>> T3
(7, 8, 9)
>>> list(zip(T1, T2, T3))             # zip combines sequences by returning a list of tuples.
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

>>> S1 = 'abc'
>>> S2 = 'xyz123'
>>>
>>> list(zip(S1, S2))                  # zip truncates result tuples at the length of the shortest sequence when the argument lengths differ.
[('a', 'x'), ('b', 'y'), ('c', 'z')]

>>> L1 = [1, 2, 3, 4]
>>> L2 = [5, 6, 7, 8]
>>> zip(L1, L2)          
[(1, 5), (2, 6), (3, 7), (4, 8)]
>>> for (a, b) in zip(L1, L2):
        print(a, b, '--', a+b)

(1, 5, '--', 6)
(2, 6, '--', 8)
(3, 7, '--', 10)
(4, 8, '--', 12)

# using map function with for

>>> S1 = 'abc'
>>> S2 = 'xyz123'
>>> map(None, S1, S2)
[('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None,'3')]
# map takes a function and one or more sequence arguments and collects
# the results of calling the function with parallel items taken from the sequence(s).

>>> map(ord, 'spam')
[115, 112, 97, 109]

>>> res = []        
>>> for c in 'spam': res.append(ord(c))       # using a for to achieve same result as the map() above
>>> res
[115, 112, 97, 109]

# dictionary construction with zip

>>> D1 = {'spam':1, 'eggs':3, 'toast':5}
>>> D1 = {}
>>> D1['spam'] = 1
>>> D1['eggs'] = 3
>>> D1['toast'] = 5

>>> keys = ['spam', 'eggs', 'toast']
>>> val = [1, 3, 5]
>>> D1 = {}                                        # creating an empty dictionary first
>>> for (k, v) in zip(keys, val): D1[k] = v        # filling in with keys and subsequent values

>>> D1
{'toast': 5, 'eggs': 3, 'spam': 1}

>> D2 = dict(zip(keys, vals))               # if you have to skip the for loop to create D2


# using enumerate to generate both offsets and items

>>> S = 'spam'
>>> offset = 0
>>> for i in S:
        print(i, 'appears at offset', offset)
        offset += 1

('s', 'appears at offset', 0)
('p', 'appears at offset', 1)
('a', 'appears at offset', 2)
('m', 'appears at offset', 3)

# The enumerate function returns a generator object—a kind of object that supports the
# iteration protocol that we will study in the next chapter and will discuss in more detail
# in the next part of the book. In short, it has a __next__ method called by the next builtin
# function, which returns an (index, value) tuple each time through the loop.

>>> S = 'spam'
>>> for (offset, item) in enumerate(S):           # returns a tuple of of (index, value)
        print(item,' is at offset ', offset)        

('s', ' is at offset ', 0)
('p', ' is at offset ', 1)
('a', ' is at offset ', 2)
('m', ' is at offset ', 3)

>>> E = enumerate(S)
>>> E
<enumerate object at 0x0000000002764B88>
>>> next(E)
(0, 's')
>>> next(E)
(1, 'p')
>>> next(E)
(2, 'a')

>>> [c * i for (i, c) in enumerate(S)]        # list comprehension using enumeration
['', 'p', 'aa', 'mmm']



## Iterations and Comprehensions - Part 1
## --------------------------------------

# File iterators

# using standard readline() to read one line at a time
>>> f = open('script1.py')      # Read a 4-line script file in this directory
>>> f.readline()                # readline loads one line on each call
'import sys\n'
>>> f.readline()
'print(sys.path)\n'
>>> f.readline()
'x = 2\n'
>>> f.readline()
'print(2 ** 33)\n'
>>> f.readline()                # Returns empty string at end-of-file
''

# using the __next__ method, iteration protocol
>>> f = open('text.txt', 'r')
>>> f.__next__()
'import sys\n'
>>> f.__next__()
'print(sys.path)\n'
>>> f.__next__()
'x = 2\n'
>>> f.__next__()
'print(2 ** 33)\n'
>>> f.__next__()                # __next__ raises a built-in StopIteration exception at end-of-file instead of returning an empty string
Traceback (most recent call last):
...more exception text omitted...
StopIteration

# the __next__ method is similar to next(), either form may be used. next() is simpler to use
>>> f = open('test.txt', 'r')
>>> next(f)
'import sys\n'
>>> next(f)
'print(sys.path)\n'

# Another method which can be used here is to obtain the iterator from the iterable object
# by passing it to the iter built-in function. The object returned by iter has the required next method
>>> L = [1, 2, 3, 4]      
>>> I = iter(L)                      # obtain an iterator object
>>> I.next()                         # call next to advance to the next item
1
>>> I.next()
2
>>> I.next()
3
>>> I.next()
4
>>> I.next()
error
StopIteration

# There's not need for obtaining an iterator object for files, since file object is its own
# iterator. They have their own __next__ method, so you can use that.
>>> f = open('test.txt', 'r')
>>> f is iter(f)
True
>>> f.__next__()        # may not work under py2.6, use next() instead
'import sys\n'

# Lists on the other hand, are not their own iterators since they support multiple open i
# iterations. We must call the iter to start iterating
>>> L = [1, 2, 3]
>>> L is iter(L)
False
>>> L.__next__()
AttributeError: 'list' object has no attribute '__next__'

>>> I = iter(L)
>>> I.__next__()
1
>>> next(I)
2
---------------------------------------
>>> L = [1, 2, 3]
>>> I = iter(L)
>>> while True:                 # using an iterator in a while loop
        try:
                X = I.next()    #or next(I)
        except StopIteration:
                break
        print(X ** 2),

1 4 9
------------------------------------------

# using line with for loop to read a line at a time
>>> for line in open('test.txt', 'r'):
        print(line.upper()),                 # removes the EOL at the end of each line

# using lines with readlines() to read a file
>>> for line in open('test.txt', 'r').readlines():
        print(line.upper()),                # be advised, that the readlines() reads entire file to memory at once, poor for memory usage and large files

# using line with while to read a file line by line. This method is not suitable for performance
>>> f = open('test.txt', 'r')
>>> while True:
        line = f.readline()
        if not line: break
        print(line.upper()),


# Other built in type Iterators

>>> D = {'a':1, 'b':2, 'c':3}
>>> for key in D.keys():           # using a for and D.keys() to iterate
        print(key, D[key])

('a', 1)
('c', 3)
('b', 2)

>>> I = iter(D)
>>> next(I)
'a'
>>> next(I)
'c'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
StopIteration


# iterator protocol for os.popen, a tool for reading the output of shell commands
>>> import os
>>> P = os.popen('dir')
>>> P.__next__()       # In py2.6, next(P) can be used as well
' Volume in drive C has no label.\n'
>>> next(f)
' Volume Serial Number is E0AB-FAC6\n'
>>> next(f)
'\n'
>>> next(f)
' Directory of C:\\Python26\n'

# Iterator with enumeration

>>> E = enumerate('spam')
>>> E
<enumerate object at 0x00000000028065E8>
>>> E is iter(E)
True
>>> next(E)
(0, 's')
>>> next(E)
(1, 'p')
>>> next(E)
(2, 'a')
>>> next(E)
(3, 'm')



# List Comprehensions

>>> L = [1, 2, 3, 4, 5]
>>> for i in range(len(L)):
        L[i] += 10
>>> L                          # in-place assignment
[11, 12, 13, 14, 15]

>>> L = [1, 2, 3, 4, 5]
>>> [x + 10 for x in L]
[11, 12, 13, 14, 15]            # not an in-place assignment

>>> f = open('test.txt', 'r')
>>> lines = f.readlines()
>>> lines
['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n']
# now using list comphrehension to remove the EOL from each item in list. Faster than a similar a for statement.
>>> lines = [line.rstrip() for line in lines]                      
>>> lines
['import sys', 'print(sys.path)', 'x = 2', 'print(2 ** 33)']

# it is possible to run any string operation on a file’s lines as we iterate
>>> [line.upper() for line in open('test.txt', 'r')]
['IMPORT SYS\n', 'PRINT(SYS.PATH)\n', 'X = 2\n', 'PRINT(2 ** 33)\n']

>>> [line.rstrip() for line in open('test.txt', 'r')]
['IMPORT SYS', 'PRINT(SYS.PATH)', 'X = 2', 'PRINT(2 ** 33)']

>>> [line.split() for line in open('test.txt', 'r')]
[['import', 'sys'], ['print(sys.path)'], ['x', '=', '2'], ['print(2', '**','33)']]

>>> [line.replace(' ', !) for line in open('test.txt', 'r')]
['import!sys\n', 'print(sys.path)\n', 'x!=!2\n', 'print(2!**!33)\n']

>>> [('sys' in line, line[0]) for line in open('test.txt', 'r')]   # check for the content
[(True, 'i'), (True, 'p'), (False, 'x'), (False, 'p')]

>>> 'y = 2\n' in open('test.txt', 'r')
False
>>> 'x = 2\n' in open('test.txt', 'r')
True

# we can also include if filter clauses in list comprehensions

>>> lines = [line.rstrip() for line in open('test.txt') if line[0] == 'p']
>>> lines
['print(sys.path)', 'print(2 ** 33)']

>>> res = []                       # similar technique in a for, but it is slower to execute
>>> for line in open('test.txt'):
        if line[0] == 'p':
                res.append(line.rstrip())
        
# list comprehension can be used to process two sequences and collect each element from both sequences to add them up
>>> [ x + y for x in 'abc' for y in 'lmn']
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']

>>> res = []                # similar technique in for, slower to run
>>> for x in 'abc':
        for y in 'lmn':
                res.append(x + y)

>>> S1 = 'SPAM'
>>> S2 = 'SCAM'
>>> intersect(S1, S2)              # True Intersection
['S', 'A', 'M']
>>> [x for x in S1 if x in S2]     # True intersection using list comprehension
['S', 'A', 'M']

# other built-ins that process iterables

>>> map(str.upper, open('test.txt', 'r'))
['IMPORT SYS\n', 'PRINT(SYS.PATH)\n', 'X = 2\n', 'PRINT(2 ** 33)\n']

>>> sorted(open('test.txt'))
['import sys\n', 'print(2 ** 33)\n', 'print(sys.path)\n', 'x = 2\n']

>>> zip(open('test.txt'), open('test.txt'))
[('import sys\n', 'import sys\n'), ('print(sys.path)\n', 'print(sys.path)\n'),
 ('x = 2\n', 'x = 2\n'), ('print(2 ** 33)\n', 'print(2 ** 33)\n')]

>>> enumerate(open('test.txt'))
[(0, 'import sys\n'), (1, 'print(sys.path)\n'), (2, 'x = 2\n'),
(3, 'print(2 ** 33)\n')]

>>> filter(bool, open('test.txt'))  # return those items for which the function(item) is true
['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n']

>>> import functools, operator   
>>> functools.reduce(operator.add, open('test.txt'))
'import sys\nprint(sys.path)\nx = 2\nprint(2 ** 33)\n'
# Apply a function of two arguments cumulatively to the items of a sequence,
# from left to right, so as to reduce the sequence to a single value. operator.add simply adds two values

# Many of the tools in python's built-in toolset process on iterables. They process from left to right,
# and defined to use the iteration protocol

>>> sum([3, 2, 4, 1, 5, 0])     # returns the sum of elements in the iterable
15
>>> any(['spam', '', 'ni'])     # Return True if bool(x) is True for any x in the iterable.
True
>>> all(['spam', '', 'ni'])     # Return True if bool(x) is True for all values x in the iterable.
False
>>> max([3, 2, 5, 1, 4])        # returns the max value in the iterable
5
>>> min([3, 2, 5, 1, 4])        # returns the min value in the iterable
11

# These built-ins can be applied to files too

>>> max(open('test.txt'))
'x = 2\n'

>>> min(open('test.txt'))
'import sys\n'

>>> tuple(open('test.txt'))
('import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n')

>>> set(open('test.txt'))
{'print(sys.path)\n', 'x = 2\n', 'print(2 ** 33)\n', 'import sys\n'}

>>> '&&'.join(open('test.txt', 'r'))        # returns a string
'import sys\n&&print(sys.path)\n&&x = 2\n&&print(2 ** 33)\n'

>>> a, b, c, d = open('test.txt')
>>> a, d
('import sys\n', 'print(2 ** 33)\n')

# It is also worth mentioning that *arg in function calls to unpack arguments can be used on iterables as well

>>> def f(a, b, c, d): print(a, b, c, d, sep='&')   # py3.0 print syntax

>>> f(1, 2, 3, 4)
1&2&3&4
>>> f(*[1, 2, 3, 4])               # unpack into arguments
1&2&3&4

>>> f(*open('test.txt'))           # iterates by lines too!
import sys
&print(sys.path)
&x = 2
&print(2 ** 33)

>>> X = (1, 2)
>>> Y = (3, 4)
>>> zip(X, Y)
[(1, 3), (2, 4)]
>>> A, B = zip(*zip(X, Y))
>>> A
(1, 2)
>>> B
(3, 4)



## The Documentation Interlude
## ---------------------------

# comments                    In-file documentation
The dir function              Lists of attributes available in objects
Docstrings: __doc__           In-file documentation attached to objects
PyDoc: The help function      Interactive help for objects
PyDoc: HTML reports           Module documentation in a browser
The standard manual set       Official language and library descriptions
Web resources                 Online tutorials, examples, and so on
Published books               Commercially available reference texts

# dir Function
>>> import sys
>>> dir(sys)
>>> dir(str)
>>> dir(list)
>>> dir(L)           # where L is a list


# Docstrings:__doc__
"""
Module Documentation
Words Go Here
"""
spam = 40
def square(x):
        """
        function documentation
        can we have your liver then?
        """
        return x ** 2 # square
class Employee:
        "class documentation"
        pass
print(square(4))
print(square.__doc__)

# The comments are retained for inspection in the __doc__ attribute, when the file is imported.
# We simply import the file and print their __doc__ attribute.

>>> import os
>>> print(os.__doc__)
OS routines for Mac, NT, or Posix depending on what system we're on.

This exports:
  - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
  - os.path is one of the modules posixpath, or ntpath
  - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
  - os.curdir is a string representing the current directory ('.' or ':')
  - os.pardir is a string representing the parent directory ('..' or '::')
  - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
  - os.extsep is the extension separator ('.' or '/')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)
  ...and more...

>>> print(os.name.__doc__)        # Built-in modules have attached descriptions in their __doc__ atributes as well.
str(object) -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
  

# PyDoc - The help Function

>>> import sys
>>> help(sys)                   # Reports the docstrins for the module and its attributes as well
>>> help(sys.getrefcount)



## FUNCTIONS
## ----------

## Scopes

# Name references have scopes at four levels: local, then enclosing functions (if any),
# then global, then built-in.

# Name assignments create or change local names by default.

# global and nonlocal(py3.0) declarations map assigned names to enclosing module and
# function scopes.

# Therefore, when searching for a scope for a name, python searches in the following order, also
# known as the LEGB rule:
        # the Local (L) scope, then the local scopes of any enclosing (E) defs, and lambdas,
        # then the global (G) scope and then built-in (B) scope - it stops at the first place
        # the name is found. If not, it reports an error. Therefore, names must be assigned
        # before they can be used.

        # When you assign a name in a function (instead of just referring to it in an expression),
        # Python always creates or changes the name in the local scope, unless it’s
        # declared to be global or nonlocal in that function.

        # When you assign a name outside any function (i.e., at the top level of a module
        # file, or at the interactive prompt), the local scope is the same as the global scope—
        # the module’s namespace.

        
# Global scope
X = 99                          # X and func assigned in module: global

def func(Y):                    # Y and Z assigned in function: locals
        # Local scope
        Z = X + Y               # X is a global
        return Z

func(1)                         # func in module: result=100

# built-in scope
>>> import __builtin__
>>> dir(__builtin__)     # The names in this list define built-in scope for Python.



# overriding or hiding scopes

# The LEGB lookup procedure takes the first occurrence of a name that it finds, names
# in the local scope may override variables of the same name in both the global and
# built-in scopes, and global names may override builtins.
# A function can, for instance, create a local variable called open by assigning to it:
        
def hider():
        open = 'spam'   # Local variable, hides built-in

        open('data.txt')   # This won't open a file now in this scope

# This will hide the built-in function called open that lives in the built-in (outer)
# scope.


# Functions can similarly hide global variable of the same name with locals:

X = 88                   # Global X

def func():
        X = 99          # Local X: Hides Global

func()
print(X)                # Prints 88: unchanged

# The assignment within the function creates a local X that is a completely different
# variable from the global X in the module outside the function. Because of this, there is
# no way to change a name outside a function without adding a global (or nonlocal)
# declaration to the def





# Breaking the Python universe in py2.6

# The names True and False are just variables in the built in scope and are not reserved, it
# is possible to reassign then with a statement like True = False in a scope in which it appears.
# All the other scopes still find the originals in the built-in scope.

# You can however say __builtin__.True = False, to reset True to False for the entire python proces.




# The global statement

# global allows us to change names that live outsode a def at the top level of a module file.

X = 88                       # Global X

def func():
        global X
        X = 99               # Global X: outside def

        func()
        print(X)             # Prints 99
# Another example:
 y, z = 1, 2                 # Global variables in a module
 def all_global():
         global x            # declare globals assigned     
         x = y + z   # no need to declare y, z: LEGB rule


# Minimize global varibles - It is a good workflow where it is required to use minimun amount of
# global variables. If a global variable is modified inside a function, then its value is time-dependent,
# meaning it is hard to know the exact value till the function is called. So, you have to trace the flow
# of control through the entire program. There are other reasons too. And there are times when global
# variables in a function may be useful. pg.416, p1-4. 


# Minimize cross-file changes altogether, but include an interface, such as a
# function with an argument to change cross-linked variables.

# first.py
X = 99

# second.py
import first
print(first.X)
first.X = 88      # Don't do this


# first.py
X = 99

def setX(new):
        global X
        X = new
        return X

# second.py
import first
var = first.setX(88)



# Other ways to access globals

#thismod.py
var = 99           # Global variable == module.attribute, i.e thismod.var

def local():
        var = 0                 # declare and change local var

>>> from thismod import var     # in this case, the var is imported from thismod module, and is made global in this scope
>>> var
99
>>> def local():
        global var              # by LEGB, python accesses the var from the global scope, which was imported using from
        print var
>>> local()
99

def glob1():
        global var          # declare global (normal)
        var += 1            # change global var

def glob2():
        var = 0             # change local var
        import thismod      # import myself
        thismod.var += 1    # change global var

def glob3():
        var = 0             # change local var
        import sys          # import system table
        glob = sys.modules['thismod']      # get module object (or use __name__) or thismod.__name__
        glob.var += 1                     # change global var

def test():
        print(var)                                  # var is 99
        local(); glob1(); glob2(); glob3()
        print(var)                                  # var is 102



# Scopes and nested functions

# Nested Scope:
# A reference (X) looks for the name X first in the current local scope (function); then
# in the local scopes of any lexically enclosing functions in your source code, from
# inner to outer; then in the current global scope (the module file); and finally in the
# built-in scope (the module builtins). global declarations make the search begin
# in the global (module file) scope instead.

# Examples:
>>>
X = 99                          # Global scope name: not used

>>>
def f1():
        X = 88                  # enclosing def local
        def f2():               # IN earlier versions of python, you had to use def f2(X=X), which means the argument X will default to the value of X in the enclosing scope
                print(X)        # reference made in nested def
        f2()                    # This is necessary statement for execution of f2() when f1() is called insid
f1()                            # prints 88: enclosing def local

--------------------------------------------
>>>                             # Another method, by using factory or closure function
def f1():
        X = 88
        def f2():               
                print(X)        # Remembers X in enclosing def scope
        return f2               # return f2, but don't call it

>>> action  = f1()              # Make, return function
>>> action()                    # Call it now, prints 88
88
--------------------------------------------
# Therefore, a factory function consists of an outer function that simply generates
# and returns a nested function, without calling it. If we call the outer function:

>>> def maker(N):                
        def action(X):
                return X ** N
        return action
        
>>> f = maker(2)                   # Pass 2 to N in function maker()
>>> f
<function action at 0x0000000002A60F98>
>>> f(3)                           # Pass 3 to returned nested function action(). N remembers 2: so 3 ** 2
9
>>> f(4)                           # 4 ** 2
16

# Now, in order to avoid using nested functions, you can do this:
>>> def f1():
        X = 88
        f2(X)                  # pass along instead of nesting
>>> def f2(X):
        print(X)

>>> f1
88


# Nested Scopes and lambdas 
# lambda is an expression that generates a new function to be called later,
# much like a def statement. Because it is an expression, it can be used in places like
# a list or a dictionary.

>>> def f1():
	X = 88
	action = (lambda N: X ** N)          # X remembered from enclosing def
	return action

>>> x = f1()              # The calling syntax is same as with nested defs
>>> print(x(3))                  
681472

# There's one exception to the 2.6 scope rule where default arguments has to be used. If a lambda
# or def defined within a function is nested inside a loop, and the nested function
# references an enclosing scope variable that is changed by the loop, all functions
# generated within the loop will have the same value - the value that the referenced
# variable had in the last loop iteration.

>>> def makeActions():                  
        acts = []
        for i in range(5):
                acts.append(lambda N: i * N)    # This creates a list of 5 functions
        return acts

>>> acts
[<function <lambda> at 0x0000000002A6C048>, <function <lambda> at 0x0000000002A6C358>,
 <function <lambda> at 0x0000000002A6C438>, <function <lambda> at 0x0000000002A6C4A8>,
 <function <lambda> at 0x0000000002A6C518>]

>>> acts[0]
<function <lambda> at 0x0000000002A6C048>

>>> acts[0](2)                
8
>>> acts[1](2)
8
>>> acts[2](2)
8
>>> acts[3](2)
8
>>> acts[4](2)                      # doesn't work with X ** N
8

# So here, the default argument has to be used.
# This is the one case where we still have to explicitly retain enclosing scope values with
# default arguments, rather than enclosing scope references. That is, to make this sort of
# code work, we must pass in the current value of the enclosing scope’s variable with a
# default. Because defaults are evaluated when the nested function is created (not when
# it’s later called), each remembers its own value for i:

>>> def makeActions():
        acts = []
        for i in range(5):
                acts.append(lambda X, i = i: X * i)
        return acts

>>> acts = makeActions()
>>> acts
[<function <lambda> at 0x0000000002A6C3C8>, <function <lambda> at 0x0000000002A6C198>,
 <function <lambda> at 0x0000000002A6C208>, <function <lambda> at 0x0000000002A6C278>,
 <function <lambda> at 0x0000000002A6C2E8>]
>>> acts[0](2)
0
>>> acts[1](2)
2
>>> acts[2](2)
4
>>> acts[3](2)
6
>>> acts[4](2)                         # Now it works.
8


# Arbitrary scope nesting
>>> def f1():
        X = 99
        def f2():
                def f3():
                        def f4():
                                print(X)    # Found in f1's local scope
                        f4()
                f3()
        f2()

>>> f1()
99
# But, it is better if you minimize the use of nested functions. Just use a flat function.


# nonlocal alternative in Python 2.6
# Although it is convenient to use make a reference variable nonlocal inside an enclosing scope, in py2.6,
# if you have to change the variable in a nested function, declare it global
>>>
def f1():
        global Y                  # Y has to be made global
        Y = 99
        def f2(num):
                global Y          # if a referenced variable has to be assigned, it has to be made global in the scope
                print(num, Y)
                Y += 1            # referenced variable assigned
                print(num, Y)
        return f2
        
>>> f = f1()
>>> f(4)
(4, 99)
(4, 100)
# This works in this case, but it requires global declarations in both functions.


# other nonlocal alternative in Python 2.6. The code explained in the book is
# expected to increment with each f() call, but it does change 'start' anyway.

def f1(start):
        def nested(label):
		state = start
		state += 1
                print(label, state)
        return nested

>>> f = f1(0)
>>> f('spam')
('spam', 1)

                
## Functions and arguments
## ------------------------

>>> def f(a):      # a is assigned to (references) passed object
        a = 99     # changes local variables only

>>> b = 88
>>> f(b)           # a and b both reference 88 initially
>>> print(b)       # b is not changed
88
# Therefore, assigning to argument names inside a function does not affect the caller.


>>> def changer(a, b):       # a, b arguments assigned references to objects
        a = 2                # Changes local name's value only
        b[0] = 'spam'        # Changes shared object in-place

>>> X = 1
>>> L = [2, 1]               # Caller
>>> changer(X, L)            # Pass immutable and mutable objects
>>> X, L                     # X is unchanged, L is different
(1, ['spam', 2])

# So it is important to know that, changing a mutable object argument in a function
# may impact the caller. In other words,
    # Immutable arguments are effectively passed “by value.”
    # Mutable arguments such as lists and dicts are effectively passed “by pointer.”

# Since passing a mutable object to a function argument has this effect, it is better to
# pass a copy or copy input inside the function if we never want to change passed-in
# objects:

>>> X = 1
>>> L = [1, 2]
>>> changer(X, L[:])     # pass a copy, so that the object referenced to L doesn't change

# Likewise,

def changer(a, b):
        b = b[:]         # copy input inside def so that it doesn't impact caller
        a = 2
        b[0] = 'spam'    # changes the copy only

def changer(a, b):
	from copy import copy
	b = copy(b)               # could also use the copy module
	a = 2
	b[0] = 'spam'
	print a, b

# To really prevent any change here, you can pass the list as a tuple here. But it
# imposes more restrictions than it should, we lose the ability for any list specific
# methods:

>>> L = [1, 2]
>>> changer(X, tuple(L))     # Pass a tuple, so changes are errors

# Returning parameters
>>> def multiple(x, y):
        x = 2               # changes local names only
        y = [3, 4]          # doesn't change the object L is referenced to. Might change L if it is assigned.
        return x, y

>>> X = 1
>>> L = [1, 2]
>>> multiple(X, L)
(2, [3, 4])                 # returns a tuple
>>> X, L
(1, [1, 2])                 # X and L unchanged
>>> X, L = multiple(X, L)   # Now assign results to caller's names       
>>> X, L
(2, [3, 4])                 # X and L changed


# Special Argument Matching modes

# Python checks for function arguments in the following order:
        # In a function call, arguments must appear in this order: any positional arguments
        # (value), followed by a combination of any keyword arguments (name=value) and the
        # *sequence form, followed by the **dict form.
        
        # In a function header, arguments must appear in this order: any normal arguments (name),
        # followed by any default arguments (name=value), followed by the *name form if present
        # followed by the **name form.
---------------------------------------------
>>> def f(a, b, c):              # create arguments
        print a, b, c

>>> f(1, 2, 3)                   # pass arguments by matching position in calling
1 2 3
---------------------------------------------
>>> def f(a, b, c):              
        print a, b, c
>>> f(c=3, b=2, a=1)             # pass arguments by matching name, not position. For this you have to
1 2 3                            # know the name of function arguments

>>> f(1, c=3, b=2)               # can also match arguments by position and name at the same time
1 2 3
# In this case, using and calling a function with more meaningful names, such as
# func(name='Bob', age=40, job='dev') would make more sense.
----------------------------------------------
>>> def f(a, b=2, c=3):          # defining a function with default arguments
        print a, b, c

>>> f(1)                         # value for just the first argument is passed, other use the default value
1 2 3
>>> f(a=1)                       # argument is passed by matching name. Others use default.
1 2 3
>>> f(1, 4)                      # values for the first two arguments are passed by position. The last uses default.
1 4 3
>>> f(1, 4, 5)                   # value for all arguments are passed. No defaults are used.
1 4 5
>>> f(1, c=6)                    # value for the first argument is passed by position. One is passed by match by name. The other uses default.
1 2 6
----------------------------------------------
# Collecting arguments
>>> def f(*args):                # when this function is called, python collects all the positional arguments
        print args               # into a new tuple and assigns the variable args to that tuple.
>>> f()
()
>>> f(1)
(1,)
>>> f(1, 2, 3, 4)
(1, 2, 3, 4)

>>> def f(**args):               # ** works only for keyword arguments. It collects them into a dictionary
        print agrs
>>> f()
{}
>>> f(a=1, b=2)
{'a':1, 'b':2}

# It is also possible to combine * and ** with normal arguments to implement widely flexible call signatures.
>>> def f(a, *pargs, **kargs):
        print a, pargs, kargs
>>> f(1, 2, 3)
1 (2, 3) {}
>>> f(1, 2, 3, x=1, y=2)
1 (2, 3) {'y': 2, 'x': 1}

# However, this functionality can be exactly reversed. *name can be used to unpack a collection of
# arguments, rather then building a collection of arguments.
>>> def f(a, b, c, d):
        print a, b, c, d

>>> args = (1, 2)
>>> args += (3, 4)
>>> args
(1, 2, 3, 4)
>>> f(*args)
1 2 3 4

# Similarly, we can use ** to unpack a dict of keys/value into separate keyword arguments.
>>> def f(a, b, c, d):
        print a, b, c, d
        
>>> args = {'a':1, 'b':2, 'c':3}
>>> args['d'] = 4
>>> f(**args)
1 2 3 4

# We can also combine normal, positional and keyword arguments in very flexible ways.
>>> f(*(1, 2), **{'d':4, 'c':3})
1 2 3 4
>>> f(1, *(2, 3), **{'d':4})
1 2 3 4
>>> f(1, c=3, *(2,), **{'d':4})
1 2 3 4
>>> f(1, *(2,), c=3, **{'d':4})
1 2 3 4

# keep in mind that the * accepts any iterable object, not just tuples or other bjects, but files as well.
# So, f(*open('fname')) unpacks its lines into individual arguments. The * acceptance of iterable objects
# is only true while calling function. The same form in a def header always collects extra aguments
# in a tuple.


# There is also a technique where you might not be sure how many arguments a function def might contain,
# which you want to call. So, you can set up an if logic statement to select from a list of functions
# and argument lists, and any of them generically:

if <test>:
        action, arg = function1, (1,)       # action had the address of function1, and arg is assigned
                                            # with a tuple of single element
else:
        action, arg = function2, (1, 2, 3)

action(*arg)                                # So, action with the referenced function is executed with
                                            # the arg with assigned tuple, which is unpacked and passed
                                            

# You can pass function as an argument, and then return it as well
>>> def tracer(func, *args, **kargs):     # In def, the first argument is for passing a function 
        print('calling:', func.__name__)
        return func(*args, **kargs)       # returns a function call with passed arguments

>>> def func(a, b, c, d):                 # executes this function when returning the function call
        return a + b + c + d

>>> print(tracer(func, 1, 2, c=3, d=4))   # So, in all, arguments are collected by the tracer and then
('calling:', 'func')                      # propagated with the returning function call(varargs)


# Older call method to unpack sequences and dictionaries using apply(), which is redundant in 3.0
>>> func(*pargs, **kargs)    # Newer call syntax: func(*sequence, **dict)

>>> apply(func, pargs, kargs)    # Defunct built-in: apply(func, sequence, dict)

>>> def echo(*args, **kargs):
        print(args, kargs)

>>> echo(1, 2, a=3, b=4)         # Newer call syntax
(1, 2) {'a': 3, 'b': 4}

# with the older apply() method, you have to assign the items first
>>> args = (1, 2)                          # create and assign items first
>>> kargs = {'a':3, 'b':4}          

>>> apply(echo, args, kargs)               # use the apply() method. Notice the name of the function at the beginning
(1, 2){'a':3, 'b':4}

>>> echo(*args, **kargs)                   # you can also use them normally
(1, 2){'a':3, 'b':4}

>>> echo(0, c=5, *args, **kargs)           # normal, keyword, *sequence, **dictionary
(0, 1, 2) {'a': 3, 'c': 5, 'b': 4}
# here, the newer call syntax can also be used to pass additonal arguments without having to mannually extend
# argument sequences or dictionaries.


# Here's an example to use special argument cases to find the minimun value from a passed sequence

>>> def min1(*args):                       # uses a for loop to find the minimum value. Here, we pass a sequence
        res = args[0]                      # as an argument, which is collected as a tuple.
        for arg in args[1:]:
                if arg < res:
                        res = arg
        return res

>>> min1(4, 3, 2, 8, 3, 5, 6, 1, 3, 4)
1

>>> def min2(*args):
        tmp = list(args)
        tmp.sort()                                 # In-place tim-sort sorting
        return tmp[0]

>>> min2(4, 3, 2, 8, 3, 5, 6, 1, 3, 4)
1
>>> min2("bb", "aa")
'aa'
>>> min2([2,2], [1,1], [3,3])
[1, 1]


# Some generalised set functions
>>> def intersect(*args):                     # intersection, find common values
	res = []
	for x in args[0]:
		for other in args[1:]:
			if x not in other: break
		else:                              # this else works with the for loop, it is executed when the for loop is not interrupted by a break, if all the items in the sequence have been visited.
                        res.append(x)
	return res

>>> s1, s2, s3 = "SPAM", "SCAM", "SLAM"
>>> intersect(s1, s2)
['S', 'A', 'M']
>>> intersect(s1, s2, s3)
['S', 'A', 'M']


>>> def union(*args):
        res = []
        for x in args:
                for ch in x:
                        if ch not in res:
                                res.append(ch)
        return res
>>> union(s1, s2, s3)
['S', 'P', 'A', 'M', 'C', 'L']



# Using 3.0 print functionality in 2.6

# import the 3.0 print module
>>> from __future__ import print_function

# Or, you can make a custom print function file

# print30.py
"""
Emulate most of the print function in 3.0 for use in 2.X
call signature: print(*args, sep=' ', end='\n', file=None)
"""
import sys
def print30(*args, **kargs):
        sep = kargs.get('sep', ' ')
        end = kargs.get('end', '\n')
        File = kargs.get('file', sys.stdout)
        output = ''
        first = True
        for arg in args:
                output += ('' if first else sep) + str(arg)
                first = False
        File.write(output + end)
# Here, the sys.stdout attribute is used to emulate the final print.
>>> from print30 import print30
>>> print30(1, 2, 3)
1 2 3
>>> print30(1, 2, 3, sep=' ')
1 2 3
>>> print30(1, 2, 3, sep='  ')
1  2  3
>>> print30(1, 2, 3, sep='....')
1....2....3
>>> print30(1, [2], (3,), sep='.....')
1.....[2].....(3,)
>>> print30(1, [2], (3,), sep='.....', end = '')
1.....[2].....(3,)
>>> print30(7, 8, 9)
7 8 9
>>> print(7, 8, 9)                      # Comparison
(7, 8, 9)

>>> print30(99, name='Bob')             # Notice here it doesn't recognize the unexpected keyword
99

# So, we have to change the print30 code to include a TypeError

import sys
def print30(*args, **kargs):
        sep = kargs.pop('sep', ' ')  # pops and returns the dictionary entry from kargs
        end = kargs.pop('end', '\n')
        File = kargs.pop('file', sys.stdout)
        if kargs:                              # if kargs not empty raise type error
                raise TypeError('extra keywords: %s' % kargs)
        output = ''
        first = True
        for arg in args:
                output += ('' if first else sep) + str(arg)
                first = False
        file.write(output + end)

## ------------------------
## Advanced Function Topics
## ------------------------

# Some general rules about function design
# Some terms are used here, for instance, how to decompose a task into purposeful functions
#(known as cohesion) and how your functions should communicate (called coupling).

# Coupling: use arguments for inputs and return for outputs.
# Coupling: use global variables only when truly necessary.
# Coupling: don’t change mutable arguments unless the caller expects it.
# Cohesion: each function should have a single, unified purpose.
# Size: each function should be relatively small.
# Coupling: avoid changing variables in another module file directly.

-------------------------------------------------------------------------------
# Recursion and functions

# Summation(simple example)
>>> def mysum(L):                # expects a list as an input argument
        if not L:
                return 0
        else:
                return L[0] + mysum(L[1:])

>>> mysum([1, 2, 3, 4, 5])
15

#Alternative ways to code the summation

# ternary expression. This will accept empty lists, but it wouldn't work on string argument, eg 'spam'
>>> def mysum(L):
        return 0 if not L else L[0] + mysum(L[1:])
# works on any type, also single argument strings. Doesn't work on an empty list.
>>> def mysum(L):
        return L[0] if len(L) == 1 else L[0] + mysum(L[1:])
# works on open files too, others do not because they index.
>>> def mysum(L):
        first, *rest = L
        return first if not rest else first + mysum(rest)   # py3.0 ext seq assign

# In recursion, it is also possible to call another function which calls back the original function.
>>> def mysum(L):
        if not L: return 0
        return nonempty(L)
>>> def nonempty(L):
        return L[0] + mysum(L[1:])

# It is not necessary to use recursion for summation, it might be an overkill in terms of execution
>>> L = [1, 2, 3, 4, 5]
sum = 0
while L:
        sum += L[0]
        L = L[1:]

>>> L = [1, 2, 3, 4, 5]
sum = 0
for x in L:
        sum += x

# Handling summation of arbitrary structures with recursion, where looping statements won't work.
>>> def sumtree(L):
        sum = 0
        for x in L:
                if not isinstance(x, list):
                        sum += x
                else:
                        sum += sumtree(x)
        return sum

>>> L = [1, [2, [3, 4], 5], 6, [7, 8]]          # arbitrary nested sublists
>>> sumtree(L)
36

--------------------------------------------------------------------------------
# Indirect function calls

# Since the function name in a def statement is simply a reference to the function object,
# it is possible to assign other names to the function and execute.

>>> def echo(message):             # name echo assigned to function object
        print message
>>> echo('Direct call')            # call function by its original name
Direct Call
>>> x = echo                       # now x references the function too
>>> x('Indirect call')             # now call the function through x
Indirect call

>>> def indirect(func, arg):       # functions may also be passed as an argument, and called inside another function
        func(arg)
>>> indirect(echo, 'Argument call')
Argument call

# It is also possible to insert functions onto data structures, as though they were integers
# and strings.
>>> schedule = [(echo, 'Spam'), (echo, 'Ham')]
>>> for (func, arg) in schedule:
        func(arg)
Spam
Ham

# As seen before, functions can be created and returned elsewhere:
>>> def make(label):
        def echo(message):
                print(label + ':' + message)
        return echo
>>> F = make('Spam')
>>> F('Ham')
Spam:Ham

----------------------------------------------------------------------------------
# Function Introspection

#Since functions are objects, we can process functions with normal objects tools
>>> def func(a):
        b = 'Spam'
        return b * a
>>> func(8)
'SpamSpamSpamSpamSpamSpamSpamSpam'

# We can inspect the attributes of a function:
>>> func.__name__              # name of the function
'func'
>>> dir(func)      # gives a list of function attributes
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
 '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__',
 '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict',
 'func_doc', 'func_globals', 'func_name']
        
>>> func.__code__
<code object func at 0000000002A7E7B0, file "<pyshell#395>", line 1>
>>> dir(func.__code__)         # gives a list of function properties
['__class__', '__cmp__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars',
 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_lnotab',
 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']

>>> func.__code__.co_varnames
('a', 'b')
>>> func.__code__.co_argcount
1
# Here's it is also possible to attach arbitrary user-defined attributes to them as well
>>> func.count = 0
>>> func.count += 1
>>> func.count
1
>>> func.handles = 'Button-Press'
>>> func.handles
'Button-Press'
>>> dir(func)
['__annotations__', '__call__', '__class__', '__closure__', '__code__',
...more omitted...
'__str__', '__subclasshook__', 'count', 'handles']


# Anonymous functions - Lambdas
# Lambdas are expressions which creates a function to be called later, but it returns the function instead
# of assigning it to a name. That's why lambdas are sometimes known as anonymous functions.

# for instance:
>>> def func(x, y, z): return x + y + z
>>> func(2, 3, 4)
9
# can be defined in lambda as:
>>> f = lambda x, y, z: x + y + z
>>> f(2, 3, 4)
9

# function argument types on def works for lambdas too
>>> x = (lambda a='fee', b='fie', c='foe': a + b + c)
>>> x('wee')
'weefiefoe'


# lambdas also follow the LEGB scope to lookup names, if they are nested.

>>> def knights():
         title = 'Sir'
         action = (lambda x: title + ' ' + x)
         return action
        
>>> act = knights()
>>> act('Robin')
'Sir Robin'
-----------------------------------------
>>> def action(x):
        return (lambda y: x + y)
>>> act = action(6)
>>> act
<function <lambda> at 0x0000000002A6C668>
>>> act(4)
10
------------------------------------------
>>> action = (lambda x: (lambda y: x + y))      # nesting a lambda inside another
>>> act = action(6)
>>> act
<function <lambda> at 0x00000000030B57B8>
>>> act(4)
10
-------------------------------------------
>>> ((lambda x: (lambda y: x + y))(6))(4)       # since the expression returns a function which is an object,
10                                              # they can be called by passing arguments in this way



# lambdas can also be included in lists or dictionaries, where actions are needed to be performed on demand
>>> L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]   # Inline function definition
>>> for f in L:        # these generated functions can be called iteratively
        print(f(2))

4
8
16
>>> L[0](2)            # or through an index
4

# you can also insert lambdas into dictionaries, where the keys attain the reference to the generated
# function through lambdas
>>> key = 'got'
>>> D = {'already':(lambda: 2 + 2), 'got':(lambda: 2 * 4), 'one':(lambda: 2 ** 6)}
>>> D[key]()
8

# It is also possible to integrate considerable logic into lambda expressions to code many statements:
>>> lower = (lambda x, y: x if x < y else y)  # expression evaluting the lower input argument
>>> lower('bb', 'aa')
'aa'
>>> lower('aa', 'bb')
'aa'

>>> import sys
>>> showall = lambda x: (map(sys.stdout.write, x))
>>> t = showall(['spam\n', 'toast\n'])
spam
toast
>>> showall = (lambda x: [sys.stdout.write(line) for line in x])
>>> t = showall(['bright\n', 'side'])
bright
side


# mapping functions over sequences to perform exponent of an input integer
>>> L = [1, 2, 3, 4, 5]
>>> updated = []
>>> for x in L:                     # using for loop
        updated.append(x ** 2)
>>> updated
[1, 4, 9, 16, 25]
------------------------------------------------------------------
>>> def inc(x):                     # using the same technique with a def function
        return x ** 2
>>> map(inc, L)
[1, 4, 9, 16, 25]
------------------------------------------------------------------
>>> def mymap(func, seq):           # using a def with a for loop to execute the technique
        res = []
        for x in seq:
                res.append(func(x))
        return res
>>> res = mymap(inc, L)
>>> res
[1, 4, 9, 16, 25]
------------------------------------------------------------------
>>> L = [1, 2, 3, 4, 5]
>>> map((lambda x: x ** 2), L)      # Now, mapping lambda over the list
[1, 4, 9, 16, 25]
----------------------------------------------------------
>>> pow(3, 2)                       # pow function with exponent 2
9
>>> map(pow, [2, 2, 2, 2, 2], [1, 2, 3, 4, 5])            # mapping pow function with lists
[2, 4, 8, 16, 32]
--------------------------------------------------

# Other function tools: filter and reduce

# filter(function or None, sequence) -> list, tuple, or string
    
    # Return those items of sequence for which function(item) is true.  If
    # function is None, return the items that are true.  If sequence is a tuple
    # or string, return the same type, else return a list.

# This filter function consists of a lambda which evalutes into a boolean which is applied with the list
# generated by the range function.
>>> filter((lambda x: x > 0), range(-5, 6))  
[1, 2, 3, 4, 5]

# Now, the reduce function applies a function of two arguments cumulatively to the items of a sequence,
# from left to right, so as to reduce the sequence to a single value.

# Here, we use a lambda expression with two arguments to input the first two values from the sequence.
# Then, it uses the result as the next first argument and then the third value from the sequence as the
# second argument and then evalutes the expression again and so on.

>>> L = [1, 2, 3, 4, 5]
>>> reduce((lambda x, y: x + y), L)
15

# Similarly, if we code our own reduce function

>>> def myreduce(function, sequence):
        tally = sequence[0]
        sequence = sequence[1:]
        for value in sequence:
                tally = function(tally, value)
        return tally

>>> myreduce((lambda x, y: x + y), L)
15
                

## --------------------------------------
## ITERATIONS AND COMPREHENSIONS - PART 2
## --------------------------------------

# As we've seen earlier, comprehension are useful when we wish to apply an arbitrary expression to a sequence.
>>> [ord(x) for x in 'spam']
[115, 112, 97, 109]

>>> [x ** 2 for x in range(9)]
[0, 1, 4, 9, 16, 25, 36, 49, 64]

# Their behavior is also similar to that of a map() function.
>>> >>> map((lambda x: x ** 2), range(9))
[0, 1, 4, 9, 16, 25, 36, 49, 64]

# Now, if we add tests and nested loops: filter
>>> [x for x in range(9) if x % 2 == 0]            # a simple comprehension with a test
[0, 2, 4, 6, 8]

>>> filter((lambda x: x % 2 == 0), range(9))       # same test technique using a filter()
[0, 2, 4, 6, 8]

# Now if we do the follwing in a list comprehension:
>>> [x ** 2 for x in range(9) if x % 2 == 0]
[0, 4, 16, 36, 64]

# But if we have to find the exponent of the list values with the filter, we have to combine map and filter
>>> map((lambda x: x ** 2), (filter((lambda x: x % 2 == 0), range(9))))
[0, 4, 16, 36, 64]

# When for loops are nested, they can be written normally and with a list comprehension:
>>> res = []
>>> for x in [1, 2, 3, 4]:                           # using for loops
        for y in [10, 20, 30, 40]:
                res.append(x + y)
>>> res
[11, 21, 31, 41, 12, 22, 32, 42, 13, 23, 33, 43, 14, 24, 34, 44]

>>> res = [ x + y for x in [1, 2, 3, 4] for y in [10, 20, 30, 40]]  # using list comprehension
>>> res
[11, 21, 31, 41, 12, 22, 32, 42, 13, 23, 33, 43, 14, 24, 34, 44]

# List comprehension with attached if on a nested for clause
>>> [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]

>>> res = []            # same result with for and if clauses
>>> for x in range(5):
        for y in range(5):
                if x % 2 == 0:
			if y % 2 == 1:
				res.append((x, y))
>>> res
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]


# List comprehensions and matrices
>>> M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
>>> N = [[2, 2, 2],
         [3, 3, 3],
         [4, 4, 4]]

>>> M[1]
[4, 5, 6]
>>> M[1][2]
6

>>> [col[1] for col in M]             # for printing the second column in matrix M; since col traverses through a row in each itertion, it collects the second item in each iteration.
[2, 5, 8]
>>> [M[row][1] for row in [0, 1, 2]]  # print second column by indexing through the matrix
[2, 5, 8]
>>> [M[i][i] for i in range(len(M))]  # for printing the diagonal elements of the matrix
[1, 5, 9]

>>> [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
[2, 4, 6, 12, 15, 18, 28, 32, 36]

>>> [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]  # since row iteration is for outer loop
[[2, 4, 6], [12, 15, 18], [28, 32, 36]]

# Same result with for loops. First a temporary list is created for each row element, which is appended to
# the final list, which is the constructed matrix
>>> res = []
>>> for row in range(3):
        tmp = []
        for col in range(3):
                tmp.append(M[row][col] * N[row][col])
        res.append(tmp)
>>> res
[[2, 4, 6], [12, 15, 18], [28, 32, 36]]        
       
# using list comprehension with file operations
>>> open('myfile').readlines()    # it opens a file and reads all the lines as items into a list

>>> [line.rstrip() for line in open('myfile').readlines()]   # removes the return character at the end of each line

>>> [line.rstrip() for line in open('myfile')]  # reads line by line

>>> map((lambda line: line.rstrip()), open('myfile'))   # using a map()

>>> Lt = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]
>>> [age for (name, age, job) in Lt]
[35, 40]
>>> map((lambda row: row[1]), Lt)
[35, 40]
>>> map((lambda (name, age, job): age), Lt)  # only in 2.6. map() can unpack tuple on its argument.


# Generators

# They are like normal functions, which are written to send back a value and later be resumed, picking up
# where they left off. Generator functions automatically suspend and resume their execution and state around
# the point of value generation.

# When we create a generator function, an iterator is automatically assigned to it.

>>> def gensquares(N):
        for i in range(N):
                yield i ** 2    # resume here later
# Since the function has an iterator, we can use it with a for clause                
>>> for i in gensquares(8):
        print30(i, end = ' : ')
        >>> for i in gensquares(8):
        print30(i, end = ' : ')
     
0 : 1 : 4 : 9 : 16 : 25 : 36 : 49 :
        
# Also, we can iterate an assigned caller using the next() method
>>> y = gensquares(8)
>>> next(y)
0
>>> next(y)
1
>>> next(y)
4
>>> next(y)
9
>>> next(y)
16
>>> next(y)
25
>>> next(y)
36

>>> for x in [n ** 2 for n in range(5)]:
        print30(x, end = ' : ')

0 : 1 : 4 : 9 : 16 :

>>> for x in (map((lambda n: n ** 2), range(5))):
        print30(x, end = ' : ')

0 : 1 : 4 : 9 : 16 :

# using send() with generator function calls. The send method advances to the next item in the series of
# results, but also provides a way for the caller to communicate with the generator, to affect its operation.
# The expression must be enclosed in parentheses unless it’s the only item on the right side of the
# assignment statement. For example, X = yield Y is OK, as is X = (yield Y) + 42.

# When this extra protocol is used, values are sent into a generator G by calling
# G.send(value). The generator’s code is then resumed, and the yield expression in the
# generator returns the value passed to send.
>>> def gen():
        for i in range(5):
                X = yield i     # yield is an expression 
                print(X)

>>> G = gen()
>>> next(G)                          # Must call next() first, to start generator
0
>>> G.send(77)                       # Advance, and send value to yield expression
77
1
>>> G.send(88)
88
2
>>> next(G)                          # next() and X.__next__() send None
None
3

# The send method can be used, for example, to code a generator that its caller can terminate
# by sending a termination code, or redirect by passing a new position. In addition,
# generators also support a throw(type) method to raise an exception inside
# the generator at the latest yield, and a close method that raises a special Generator
# Exit exception inside the generator to terminate the iteration. See manuals for details.


# Generator comprehensions or generator expressions

>>> (x ** 2 for x in range(5))
<generator object <genexpr> at 0x0000000002B23E58>

>>> list(x ** 2 for x in range(5))           # list comprehension equivalence
[0, 1, 4, 9, 16]
                
>>> G = (x ** 2 for x in range(5))
>>> next(G)
0
>>> next(G)
1
>>> next(G)
4
>>> next(G)
9
>>> next(G)
16
>>> next(G)
...error...
StopIteration

>>> sum(x ** 2 for x in range(4))    # apply built-in function    # this example doesn't work in py2.6
14

>>> sorted(x ** 2 for x in range(4))
[0, 1, 4, 9]

>>> sorted((x ** 2 for x in range(4)), reverse = True)
[9, 4, 1, 0]

>>> import math
>>> map(math.sqrt, (x ** 2 for x in range(4)))
[0.0, 1.0, 2.0, 3.0]

# Generator functions versus Generator expressions
>>> G = (c * 4 for c in 'spam')
>>> G
<generator object <genexpr> at 0x0000000002B23B40>
>>> list(G)                                              # force generator to produce all results
['ssss', 'pppp', 'aaaa', 'mmmm']

>>> def timesfour(S):
        for c in S:
                yield c * 4

>>> G = timesfour('spam')
>>> G
<generator object timesfour at 0x0000000002B23750>
>>> list(G)                                  # iterate automatically, forcing generator to produce all results
['ssss', 'pppp', 'aaaa', 'mmmm']
# both generator expressions and functions support manual iteration thorught next() and automatic iteration
# as shown above. Make sure that for a manual iteration, once a iterator has been exhausted at StopIteration,
# a new iterator has to be assigned

# Generators are single iterator objects, meaning both generator functions and expressions are their own
# iterators, meaning, a generator's iterator is the generator itself. Moreover once any iteration runs to
# completion, all are exhausted. We have to make a new generator to start again.

>>> G = (c * 4 for c in 'SPAM')
>>> iter(G) is G
True
>>> next(G)
StopIteration
# similarly, any new iter assigned to G or directly to the expression now will be exhausted too
>>> I1 = iter(G)   
>>> next(I1)
StopIteration
>>> Gd = (c * 4 for c in 'SPAM')
>>> next(Gd)
StopIteration
# to see if an iterator has been exhausted, use the list command to check:
>>> list(G)
[]                  # returns empty stack
>>> list(Gd)
[]
#Now to create a new iterator, we have to start over again by creating a new iterator:
>>> newG = iter(c * 4 for c in 'SPAM')
>>> next(newG)
'SSSS'
>>> next(newG)
'PPPP'
>>> next(newG)
'AAAA'
>>> next(newG)
'MMMM'
# It also holds true for generator functions, where at a time, they only have a single iterator:
>>> def timesfour(S):
        for c in S:
                yield c * 4

>>> G = timesfour('SPAM')
>>> G
<generator object timesfour at 0x0000000002B23AF8>
>>> iter(G) is G
True
>>> I1, I2 = iter(G), iter(G)
>>> next(I1)
'SSSS'
>>> next(I2)
'PPPP'
>>> next(I1)
'AAAA'
# As you can see, at a time, only one itertor is at work. This is not like an iterator which may be assigned
# to a list, which is not its own iterator, and hence can be assigned with multiple iterators at once, which
# reflect their in-place changes in active iterators:
>>> L = [1, 2, 3, 4, 5]
>>> I1, I2 = iter(L), iter(L)
>>> I1.next()
1
>>> I1.next()
2
>>> I2.next()
1
>>> del L[2:]
>>> I1.next()
StopIteration

# Emulating zip and map with iteration tools. zip pairs items, truncates at shortest. map passes items or
# paired items to a function, truncates.
>>> S1 = 'abc'
>>> S2 = 'xyz123'
>>> list(zip(S1, S2))          # zip returns a tuple, so we have to convert it to a list
[('a', 'x'), ('b', 'y'), ('c', 'z')]            # it also truncates to the length of the shorter sequence

>>> list(zip([-2, -1, 0, 1, 2]))       # Single sequence: 1-ary tuples
[(-2,), (-1,), (0,), (1,), (2,)]
 
>>> list(zip([1, 2, 3], [1, 2, 3, 4, 5]))       # N-sequences: N-ary tuples
[(1, 1), (2, 2), (3, 3)]

>>> map(abs, [−2, −1, 0, 1, 2]))           # Single sequence: 1-ary function
[2, 1, 0, 1, 2]

# Creating a custom map function
>>> def mymap(func, *args):
        res = []
        for arg in zip(*args):                       # here, the *args unpacks the tuple of lists into individual lists, 
                res.append(func(*arg))               # or a tuple of single elements into individual elements.
        return res

>>> def mymap_p(func, *args):                        # same technique using list comprehension
        return [func(*arg) for arg in zip(*args)]

>>> def mymap_g(func, *args):                        # using function generator        
        for arg in zip(*args):
                yield func(*arg)

>>> def mymap_p_g(func, *args):                      # using expression generator
        return (func(*arg) for arg in zip(*args))
                

>>> mymap(pow, [1, 2, 3],[2, 3, 4, 5])  
[1, 8, 81]
>>> mymap(abs, [-2, -1, 0, 1, 2])
[2, 1, 0, 1, 2]

# Writing custom zip functions. Here, the input argument is comprehended into a list, or a list of lists, depending upon
# the input argument. Then it goes through a while all loop, where 'all' check if all the contents of the list are true,
# or non-empty, till then the loop continues. This helps if two lists are of unequal sizes. Then, the pop argument deletes
# and returns the first item from each of the lists. Each of these n-items are collected into a tuple and appended to a list.

>>> def myzip(*args):
        args = [list(arg) for arg in args]
        res = []
        while all(args):
                res.append(tuple(arg.pop(0) for arg in args))
        return res

>>> myzip([1, 2, 3, 4], [4, 5, 6])
[(1, 4), (2, 5), (3, 6)]

>>> def myzip_p(*args):                       # same technique, but with support for padding
        pad = None
        args = [list(arg) for arg in args]
        res = []
        while any(args):                      # returns True if any items in the iterable are nonempty
                res.append(tuple((arg.pop(0) if arg else pad) for args in args))
        return res

>>> myzip_p([1, 2, 3, 4, 5],[2, 3, 4])
[(1, 2),(2, 3),(3, 4),(4, None),(5, None)]

>>> def myzip_g(*args):                       # using function generator
        args = [list(arg) for arg in args]
        while all(args):
                yield tuple(arg.pop(0) for arg in args)

>>> def myzip_p_g(*args):                     # using function generator with padding. In py3.X, use (*args, pad=None)
        pad = None
        args = [list(arg) for arg in args]
        while all(args):
                yield tuple((arg.pop(0) if arg else pad) for arg in args)

# In the following implementations using a list comprehension to return the final list of zipped data,
# the arg simply indexes and returns each positional value from each input list for the tuple.
>>> def myzip_lmin(*args):                    # using the min length of the input arguments for implementation
        min_len = min(len(arg) for arg in args)
        return [tuple(arg[i] for arg in args) for i in range(min_len)]

>>> myzip_lmin([1, 2, 3, 4, 5],[2, 4, 6])
[(1, 2), (2, 4), (3, 6)]

>>> def myzip_lmax(*args):                    # using the max length of the input arguments for implementation with padding
        pad = None
        max_len = max(len(arg) for arg in args)
        return [tuple((arg[i] if len(arg) > i else pad) for arg in args) for i in range(max_len)]

>>> myzip_lmax([1, 2, 3, 4, 5],[2, 4, 6])
[(1, 2), (2, 4), (3, 6), (4, None), (5, None)]

# Now, we will create a custom zip function using an iterable object and a generator. Here, first we create a sequence of
# iterable objects by mapping iter to each item on the input sequence. Then we create a while loop which
# returns the iteration using next on each iterator, until one of the iterators is exhausted. Each loop
# yields a generator object. 

>>> >>> def myzip_iter(*args):
	res = []
        iters = map(iter, args)          # use list(map()) in py3.0. 3.0 map returns a one-shot iterable object instead of a list as in 2.6.
        while iters:
                tmp = [next(itr) for itr in iters]
		yield tuple(tmp)

>>> gen = myzip_iter([1, 2, 3, 4, 5, 6], [2, 4, 6, 8])
>>> gen
<generator object myzip_iter at 0x0000000002B73F30>
>>> list(gen)
[(1, 2), (2, 4), (3, 6), (4, 8)]


# Using the Timing Module
# Here, we will test the relative speeds of different function types with various list construction techniques.

import sys, time
reps = 1000
repslist = range(reps)

def mytimer(func, *args, **kargs):
        start = time.clock()                # assigns the current time to start
        for i in repslist:                  # we could do range(reps) here, but it will charge the time. In py3.0, range() is an iterator, so this is not required.
                ret = func(*args, **kargs)
        elapsed = time.clock() - start      # difference in time    
        return (elapsed, ret)

def forLoop():
        res = []
        for x in repslist:
                res.append(abs(x))
        return res

def listComp():
        return [abs(x) for x in repslist]

def mapCall():
        return (map(abs, repslist))

def genExpr():
        return list(abs(x) for x in repslist)     # the list forces to produce all results at once

def genFunc():
        def gen():
                for x in repslist:
                        yield abs(x)
        return list(gen())

print sys.version
for f_test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = mytimer(f_test)
        print '-' * 33
        print ('{0:<9}: {1:.5f} => [{2}...{3}]'.format(f_test.__name__, elapsed, result[0], result[-1]))
      # print ('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))


2.6.4 (r264:75708, Oct 26 2009, 07:36:50) [MSC v.1500 64 bit (AMD64)]
---------------------------------
forLoop  : 0.22293 => [0...999]
---------------------------------
listComp : 0.11569 => [0...999]
---------------------------------
mapCall  : 0.07805 => [0...999]
---------------------------------
genExpr  : 0.14382 => [0...999]
---------------------------------
genFunc  : 0.14694 => [0...999]

# We can see here that list comprehension is faster than an expression generator. The map function being the fastest here.
# If we use an addition on x for calculation instead of a simple method as abs(), watch what happens:
......
def forLoop():
        res = []
        for x in repslist:
                res.append(x + 10)
        return res

def listComp():
        return [x + 10 for x in repslist]

def mapCall():
        return (map((lambda x: x + 10), repslist))

def genExpr():
        return list(x + 10 for x in repslist)     # the list forces to produce all results at once

def genFunc():
        def gen():
                for x in repslist:
                        yield x + 10
        return list(gen())
.........

2.6.4 (r264:75708, Oct 26 2009, 07:36:50) [MSC v.1500 64 bit (AMD64)]
---------------------------------
forLoop  : 0.20770 => [10...1009]
---------------------------------
listComp : 0.07538 => [10...1009]
---------------------------------
mapCall  : 0.17127 => [10...1009]
---------------------------------
genExpr  : 0.11042 => [10...1009]
---------------------------------
genFunc  : 0.10070 => [10...1009]

# Here, the list comprehension turns out to be faster than the map() method.

# Timing method alternatives:
        # It is best to use time.clock() to get current time on windows, but on unix systems, time.time() is better.
        # If you want optimum results, it is best to run a test number of times.

"""
timer(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3)
_reps times, and returns total time for all runs, with final result;

best(spam, 1, 2, a=3, b=4, _reps=50) runs best-of-N timer to filter out
any system load variation, and returns best time among _reps tests
"""
import time, sys
if sys.platform[:3] == 'win':
        timefunc = time.clock                           # Use time.clock on Windows
else:
        timefunc = time.time                            # Better resolution on some Unix platforms
        
def trace(*args): pass # Or: print args

def timer(func, *pargs, **kargs):
        _reps = kargs.pop('_reps', 1000)                        # Passed-in or default reps
        trace(func, pargs, kargs, _reps)
        repslist = range(_reps)                                 # Hoist range out for 2.6 lists
        start = timefunc()
        for i in repslist:
                ret = func(*pargs, **kargs)
        elapsed = timefunc() - start
        return (elapsed, ret)

def best(func, *pargs, **kargs):
        _reps = kargs.pop('_reps', 50)
        best = 2 ** 32
        for i in range(_reps):
                (time, ret) = timer(func, *pargs, _reps=1, **kargs)
                if time < best: best = time
        return (best, ret)

reps = 10000
repslist = range(reps)

def forLoop():
        res = []
        for x in repslist:
                res.append(x + 10)
        return res

def listComp():
        return [x + 10 for x in repslist]

def mapCall():
        return (map((lambda x: x + 10), repslist))

def genExpr():
        return list(x + 10 for x in repslist)                   # the list forces to produce all results at once

def genFunc():
        def gen():
                for x in repslist:
                        yield x + 10
        return list(gen())

print(sys.version)
for tester in (mytimer.timer, mytimer.best):
        print('<%s>' % tester.__name__)
        for test in (forLoop, listComp, mapCall, genExpr, genFunc):
                elapsed, result = tester(test)
                print ('-' * 35)
                print ('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

3.0.1 (r301:69561, Feb 13 2009, 20:04:18) [MSC v.1500 32 bit (Intel)]
<timer>
-----------------------------------
forLoop : 2.35371 => [10...10009]
-----------------------------------
listComp : 1.29640 => [10...10009]
-----------------------------------
mapCall : 3.16556 => [10...10009]
-----------------------------------
genExpr : 1.97440 => [10...10009]
-----------------------------------
genFunc : 1.95072 => [10...10009]
<best>
-----------------------------------
forLoop : 0.00193 => [10...10009]
-----------------------------------
listComp : 0.00124 => [10...10009]
-----------------------------------
mapCall : 0.00268 => [10...10009]
-----------------------------------
genExpr : 0.00164 => [10...10009]
-----------------------------------
genFunc : 0.00165 => [10...10009]
        


# There are alternative ways to time code. There's timeit module in standard library, which automates timing of code and other
# things, there's profile module which contains complete source code profiler tool for large development projects.


# Common Function pitfalls:

        # Local names are detected statically - a name that isn't assigned in a function is looked up in the enclosing module.

        >>> X = 99
        >>> def selector():     # X is used but not assigned
                print(X)        # X found in global scope

        >>> selector()
        99

        >>> def selector():     # Will return an error. Since X is eventually assigned in the def, it will be treated local.
                print(X)       
                X = 88

        >>> selector()
        ...error...
        'X' referenced before assignment

        >>> def selector():
                global X        # Since X is declared global here, it takes the value of 99      
                print(X)        # prints 99
                X = 88          # changes X to 88

        >>> selector()
        99

        >>> X = 99
        >>> def selector():
                import __main__           # Import enclosing module
                print(__main__.X)         # Qualify to get to global version of name
                X = 88                    # Unqualified X classified as local        
                print(X)                  # Prints local version of name

        >>> selector()
        99
        88

        # Defaults and Mutable objects. Since defaults are evaluated when a def statemet is run, it lets you save values from
        # the enclosing scope, if needed. But because a default retains an object between calls, you have to be careful about
        # changing mutable defaults.

        >>> def saver(x=[]):
                x.append(1)
                print x

        >>> saver()
        [1]
        >>> saver()
        [1, 1]
        >>> saver()
        [1, 1, 1]
        >>> saver()
        [1, 1, 1, 1]
        >>> saver()
        [1, 1, 1, 1, 1]
        >>> saver([2])
        [2, 1]
        >>> saver([2])
        [2, 1]
        >>> saver()
        [1, 1, 1, 1, 1, 1]

        # Here, the default value has a separate reference which x refers to when there's no argument, but it also changes
        # each time with execution of def. When a value is passed, the def refers to the value and passes it as a new
        # stack each time. But if no value is passed, def refers back to the last state of default value and appends to it.
        
        # This behaviour may serve as a feature. Because mutable default arguments retain their state between function calls, they can serve some of the same roles as static local function
        # variables in the C language. In a sense, they work sort of like global variables, but their names are local to
        # the functions and so will not clash with names elsewhere in a program.

        # So, in order to get a desied behaviour for the default argument, we move it inside the function body:

        >>> def saver(x=None):
                if x = None:      
                        x = []
                x.append(1)
                print x

        >>> saver([2])
        [2, 1]
        >>> saver()
        [1]
        >>> saver()
        [1]

        # if could also be replaced by x = x or [], if x is empty or False, it will always return []. If an empty list were
        # passed in, the or expression would cause the function to extend and return a newly created list, rather than
        # extending and returning the passed-in list like the if version. (The expression becomes [] or [], which evaluates
        # to the new empty list on the right.

        >> def saver():          
	saver.x.append(1)    # The function name is global to the function itself. Here we can use the function attributes.
	print(saver.x)

	
        >>> saver.x = []
        >>> saver()
        [1]
        >>> saver()
        [1, 1]
        >>> saver()
        [1, 1, 1]


        # Another thing to remember is that, functions with no return or yield automatically return None.

        # Also, remember that when we have a function or a lambda inside a loop, we have to use defaults for the iterator.
        # Otherwise it uses only the last value of the iterator.
        >>> def makeActions():
                acts = []
                for i in range(5):                              # Use defaults instead
                        acts.append(lambda x, i=i: i ** x)      # Remember current i
                        return acts
        
                

        

## ----------------------------------
## MODULES: THE BIG PICTURE
## ----------------------------------

# Modules have three roles: Code reuse, System namespace partitioning, Implementing shared services or data.

# When python processes a module, first it tries to find it. When it searches for a module, it looks for it
# in the following order:
        # Home directory, where the top-level program file resides.

        # Directory lists or variables in the PYTHONPATH enviornment setting. You only need to set PYTHONPATH
        # to import from directories other than the one in which you are working

        # Standard library directories

        # The contents of any .pth (oath) files, which contains a list of directories, line by line

# After it finds the file, it compiles it and produces a byte-code of the file. If an older version
# of the compiled .pyc file already exists it regenerates it else it skips. If only a .pyc file for the
# module exists, it loads it. Also, if the module is in the sys.module listing, means it is already loaded.
# so python skips it, unless explicitly specified by imp.reload. More on that later.


# Then, the compiled file is executed along with the top-level code.

# To check the module search path on a machine, use sys.path
# The sys.path list merges all info in the different search paths. It is alos possible to modify this
# sys.path list, but this change only lasts for the duration of the script.

>>> import sys
>>> sys.path
['C:\\Python26\\Lib', 'C:\\Python26\\Lib\\idlelib', 'C:\\Python26\\python26.zip', 'C:\\Python26\\DLLs',
 'C:\\Python26\\lib', 'C:\\Python26\\lib\\plat-win', 'C:\\Python26\\lib\\lib-tk', 'C:\\Python26',
 'C:\\Python26\\lib\\site-packages']

# If you have, say for instance, name.py and name.so in different directories, python will load the one
# found in the first (leftmost) directory of the module search path during the left to right search of
# sys.path. If they are in the same directory, python follows a standard picking order. Therefore, it is
# better to make sure that your module names are distinct.


# Advanced module selection concepts

# import operation can be redefined using import hooks

# Files can be imported from compressed .zip archives

# For details, see the built-in __import__ function, the customizable tool that import statements actually run.

# Python supports use of .pyo optimized byte-code files, created and run with the -O Python command-line flag,
# they only run 5% faster than .pyc files.        


# Scripts and custom extensions can use 'disutils' tools in the standard library to automatically install themselves,
# so no path configuration is required. Systems that use disutils come with setup.py, which is run to install
# them; this script imports and uses distutils modules to place such systems in a directory that is automatically
# part of the module search path (usually in the Lib\sitepackages subdirectory of the Python install tree, wherever
# that resides on the target machine). For more details on distributing and installing with distutils, see the
# Python standard manual

# There are global and local scopes in a given module. They can be accessed by global() and local(), and they return
# a dictionary, with items as variables and their values. If we look at globals() in a given module:

# __builtins__ attribute points to a module that contains all of Python's built-in functions such as print() and globals(),
# and objects such as int and dict. This module is always automatically loaded, and does not require that you access its
# attributes using a namespace.

# __file__ attribute of a module is simply a string indicating the absolute path to the module's .py file on the 
# operating system.

# __package__ attribute of a module returns the name of the package to which the module belongs.

# The __doc__ attribute is very useful when used correctly. Python assumes the first comment in a module is its 
# docstring. Likewise, each function has its own __doc__ attribute, also presumed to be the first comment in its 
# definition.


## --------------------
## MODULE CODING BASICS
## --------------------

# When we write a python code, and save it with a .py extension, it is considered as a module. All the names
# assigned at the top level of the module become its attributes, and are exported for clients to use.

# For example, the follwing code in the file:

        def printer(x):                         # Module attribute
                print x

# Be advised, that it is not desirable to name a .py file with a reserved like 'if'. We'll get a syntax error,
# if imported. Both the names of module files and the names of directories should follow naming conventions.

# Modules coded in C/C++ are known extension modules, and are called external libraries for python.


# The import Statement:

>>> import module1                              # Get module as a whole
>>> module1.printer('Hello world!')             # Qualify to get names
Hello world!


# The from Statement:
# 'from' copies names from one file over to another scope, it allows us to use the copied names directly in the
# script without going through the module (e.g., printer):

>>> from module1 import printer                 # Copy out one variable
>>> printer('Hello world!')                     # No need to qualify name
Hello world!


# The from * Statement:
# This is a special form of from: when we use a *, we get copies of all the names assigned at the top level of
# the referenced module. Here again, we can then use the copied name printer in our script without going through
# the module name:

>>> from module1 import *                       # Copy out all variables
>>> printer('Hello world!')
Hello world!

# This command cannot be used from within a function in py3.0, but in py2.6, it is allowed, but a warning is issued.


# Imports happens only once per python session. Re-imports fetch the already created module object from
# Python’s internal modules table.


# Just like def, import and from are executable statements, and not compile time declarations. They may be
# nested inside if or inside defs, but they are not executed until python reaches them.

# When importing names from a module, they follow the assignment rules as with function arguments. Reassigning
# a fetched name has no effect on the module, but changing a fetched mutable object can change it in the module
# from which it was imported.

# small.py
x = 1
y = [1, 2]

>>> from small import x, y                      # Copy two names out
>>> x = 42                                      # Changes local x only
>>> y[0] = 42                                   # Changes shared mutable in-place

# Now, if we import the module again

>>> import small                                # Get module name (from doesn't)
>>> small.x                                     # Small's x is not my x
1
>>> small.y                                     # But we share a changed mutable
[42, 2]

# So, assignments work the same everywhere in python.

# Now, if you do have to make cross-file changes to a fetched name, you have to use import. Otherwise, it changes
# the name x in that scope only, not the x in the file.

>>> from small import x, y                      # Copy two names out
>>> x = 42                                      # Changes my x only
>>> import small                                # Get module name
>>> small.x = 42                                # Changes x in other module

# Also note that the change to y[0] as previously described changes an object, not a name.

# from only copies names from one module to another, it does not assign the module name itself. from statements
# create new variables in the importer, which initially refer to objects of the same names in the imported files.
# Only the names are copied, not the module itself. When we use from * , the equivalence is the same.

from module import name1, name2                 # Copy these two names out (only)

# is equivalent to this statement sequence:

import module                                   # Fetch the module object
name1 = module.name1                            # Copy names out by assignment
name2 = module.name2
del module                                      # Get rid of the module name

# So, in order to explain about the from Statement:
        # It makes the location of a variable more implicit and obscure, less meaningful than module.name

        # It may have the potential to corrupt namesspaces, if you use it to import variables that have the
        # same names as existing variables in the scope, your variables will be silently overwritten. This
        # doesn't happen with import since you go through a module's name (module.attr)

        # the from can be used carefully as long as you understand the namespace changes it can bring. If you
        # list the imported names explicitly, it isn't a major concern (from module import x, y, z).

        # With the reload call, from statement might reference prior versions of the objects.

        # the from module import * can corrupt namespaces and make names difficult to understand, when applied
        # to more than one file. It defeats the namespace partitioning feature of modules.
        
        # So limit the from * to just one import per file. Better, explicitly list variables when importing
        # using from.

        
# the import statement is preferred over from, when two attributes the modules have the same name, to avoid
# names being overwritten.

# O.py
import M, N                     # Get the whole modules, not their names
M.func()                        # We can call both names now
N.func()                        # The module names make them unique



# Module Namespaces

# Module statements run on the first import.

# module2.py
print('starting to load...')
import sys
name = 42

def func(): pass

class klass: pass

print('done loading.')

>>> import module2
starting to load...
done loading.
>>> import module2
>>> 

# Once the module is loaded, its scope becomes an attribute namespace in the module object we get back from
# import. Only top-level assignments in the module create module attributes. Assigned names through the attributes
# are stored in module's namespace.

>>> module2.sys
<module 'sys' (built-in)>      # import statements really assign module objects to names, and any type of assignment
                               # to a name at the top level of a file generates a module attribute.

>>> module2.name
42

>>> module2.func
<function func at 0x0000000004E36F98>

>>> module2.klass
<class module2.klass at 0x0000000004E5B938>

# Module namespaces created by imports are dictionary objects, internally; they may be accessed by built-in
# __dict__ attribute associated with module objects. The dir function is similar to sorted keys list of a
# module object's __dict__ attribute, includes inherited names for classes, may not be complete, prone to
# changing from release to release.

>>> module2.__dict__.keys()         # We can use usual dictionary methods with them
['name', '__builtins__', '__file__', '__package__', 'sys', 'klass', 'func', '__name__', '__doc__']

>>> dir(module2)                    # notice the entries are sorted
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'func', 'klass', 'name', 'sys']

>>> module2.__name__           # name as known to importers
'module2'
>>> module2.__file__           # name of the file with extension and directory path
'C:\\Python26\\module2.py'

# Attribute name qualification

# Simple variables
# X means search for the name X in the current scopes (following the LEGB rule).

# Qualification
# X.Y means find X in the current scopes, then search for the attribute Y in the object X (not in scopes).

# Qualification paths
# X.Y.Z means look up the name Y in the object X, then look up Z in the object X.Y.

# Generality
# Qualification works on all objects with attributes: modules, classes, C extension
# types, etc.



# Imports vs scopes

# moda.py
X = 88                  # My X: global to this file only
def f():
        global X        # Change this file's X
        X = 99          # Cannot see names in other modules

# modb.py
X = 11                  # My X: global to this file only

import moda             # Gain access to names in moda
moda.f()                # Sets moda.X, not this file's X
print(X, moda.X)

% python modb.py        # When run in a console
11 99

# Here we can see that import operations never give upward visibility to code in imported files - an imported
# file cannot see names in the importing file, unless they are explicitly imported.


# Namespace nesting

# mod3.py
X = 3

# mod2.py
X = 2
import mod3

print(X, end=' ')               # My global X
print(mod3.X)                   # mod3's X

# mod1.py
X = 1
import mod2

print(X, end=' ')               # My global X
print(mod2.X, end=' ')          # mod2's X
print(mod2.mod3.X)              # Nested mod3's X

# When mod1 imports mod2 here, it sets up a two-level namespace nesting. By using the path of names mod2.mod3.X,
# it can descend into mod3, which is nested in the imported mod2. The net effect is that mod1 can see the Xs in
# all three files, and hence has access to all three global scopes:

% python mod1.py
2 3
1 2 3

# The reverse, however, is not true: mod3 cannot see names in mod2, and mod2 cannot see names in mod1.




# Reloading modules - Reloads help to change part of the program without stopping it.

# Imports load and run a module's code only the first time the module is imported in the process.

# Later imports use the already loaded module object without reloading or rerunning the file's code.

# The reload function forces an already loaded module's code to be reloaded and rerun. Assignments
# in the file's new code change the existing module object in-place.

# Unlike import and from:
        # reload is a function and not a statement. (In py2.6, it is built-in)
        # reload is passed an existing module which was previously imported, not a name.

# reloading a module's file code overwrites its existing namespace, rather than deleting and re-creating it.

# Clients that have used from to fetch attributes in the past won't be affected by a reload.

# Example:

# changer.py
message = "First version"
def printer():
        print(message)

% python
>>> import changer
>>> changer.printer()
First version

# changer.py is changed
message = "After editing"
def printer():
        print('reloaded:', message)
        
% python
>>> import changer
>>> changer.printer()                   # No effect: uses loaded module
First version

>>> reload(changer)                     # Forces new code to load/run
<module 'changer' from 'changer.py'>
>>> changer.printer()                   # Runs the new version now
reloaded: After editing


## ---------------
## MODULE PACKAGES
## ---------------

# In addition to a module name, an import can name a directory path. A directory of python code is said
# to be a package, so such imports are known as package imports. A package import turns a directory on
# your computer into another python namespace, with attributes corresponding to the subdirectories and
# module files that the directory contains.

# In the import statement, instead of providing just a name, you can list a path of names separated
# by periods:

import dir1.dir2.mod

# The same goes for from statements:

from dir1.dir2.mod import x

# Here, this statement is assumed to correspond to a path throught the directory hierarchy on the machine,
# leading to the file mod.py
# Therefore:
dir0\dir1\dir2\mod.py           # Or mod.pyc, stc

# This dir0 is the directory name added to the module search path, can be arbitrarily platform specific
# directory path leading up to dir1. A pseudocode may be:

import C:\mycode\dir1\dir2\mod

# The C:\mycode is added to the PYTHONPATH or it may be the home directory or it may be in the .pth file.
# In which case it is written as:

import dir1.dir2.mod

# The dot notation is used for platform neutrality and to imply nested path objects. Now, each directory
# within the path of a package import statement must contain a file named __init__.py
# Here, dir1 and dir2 must contain the __init__.py file

# import statements run each directory's initialization file the first time that directory is traversed.
# You may also use the reload method if desired.
# Example:

# dir1\__init__.py
print('dir1 init')
x = 1

# dir1\dir2\__init__.py
print('dir2 init')
y = 2

# dir1\dir2\mod.py
print('in mod.py')
z = 3

% python
>>> import dir1.dir2.mod                                # First imports run init files
dir1 init
dir2 init
in mod.py
>>>
>>> import dir1.dir2.mod                                # Later imports do not
>>>

>>> reload(dir1)
dir1 init
<module 'dir1' from 'dir1\__init__.pyc'>
>>>
>>> reload(dir1.dir2)
dir2 init
<module 'dir1.dir2' from 'dir1\dir2\__init__.pyc'>
>>> reload(dir1.dir2.mod)
<module 'dir1.dir2.mod' from 'dir1\dir2\mod.pyc'>

# The __init__.py does:

# Package initialization - The first time python imports through a directory, it runs all the code inside
# this file. It is used to put code to initialize the state required by files in a package. Typically,
# they are not meant to be useful if executed directly.

# Now, the variables defines in the initialization files as well as the main module file can be accessed
# this way:

>>> dir1.x
1
>>> dir1.dir2.y
2
>>> dir1.dir2.mod.z
3

# from versus import with Packages

# It might be convenient to use the from Statement to avoid retying the paths at each access.

% python
>>> from dir1.dir2 import mod                   # Code path here only
dir1 init
dir2 init
in mod.py
>>> mod.z                                       # Don't repeat path
3
>>> from dir1.dir2.mod import z
>>> z
3

# Package imports also make imports more meaningful; by the name of a directory, it is more clear what role
# a module might play. You can avoid including everything in the module search path.

import utilities

import database.clients.utilities      # offers more information, when organised into a directory


# A case where package import is useful:

root\
        system1\
                __init__.py
                utilities.py
                main.py
                other.py
        system2\
                __init__.py
                utilities.py
                main.py
                other.py
        system3\                                # Here or elsewhere
                __init__.py                     # Your new code here
                myfile.py

# Here, two directories, system1 and system2 contain two versions of program files. If we to install a
# third program file as a common version, we can include everything under a root, which is the home
# directory. The will avoid errors when using straight import, where python will only use the first
# occurrence in the module search path. Here the files can be accessed by:

import system1.utilities
import system2.utilities
system1.utilities.function('spam')
system2.utilities.function('eggs')

# Note that you have to use import instead of from with packages only if you need to access the same
# attribute in two or more paths. If the name of the called function here was different in each path,
# from statements could be used to avoid repeating the full package path whenever you call one of the
# functions, as described earlier.

# You can also include the common files in the root directory, because it is the home directory that
# will be searched first. The code in the systems directory will keep working unchanged.



# Package relative imports

# Two things to keep in mind:
        # In py2.6 and in 3, you can use leading dots in from statements to indicate that the import
        # should be relative to the containing package. It will not search for modules elsewhere,
        # or in the sys.path, known as absolute search

        # In py2.6, normal imports perform relative-then-absolute search. Unlike py3.0 which only
        # performs absolute search under normal imports, it skips the containing package.

# To perform relative import,        

from . import spam          # relative to this package

# With this, python imports a module named spam located in the same package directory as the file in
# which this statement appears

from .spam import name

# With this, python imports a module named spam located in the same package as the file that contains
# this statement, import the variable name.

from .. import other

# performs an import a sibling of the current package directory. For example:

from . import D                 # Imports A.B.D (. means A.B)
from .. import E                # Imports A.E (.. means A)

# Now, to perform absolute import in py2.6 like 3.0,

from __future__ import absolute_import


# Relative imports versus absolute package paths

from mypkg import string                        # imports mypkg.string(absolute)

# A module can name its own package explicitly in an absolute import statement. Here, mypkg will be found
# in an absolute directory on sys.path. However, this form requires that the directory immediately containing
# mypkg be included in the module search path. Also, you must list all directories leading up to the module:

from system.section.mypkg import string         # system container on sys.path only

# Keep in mind that relative imports work with from Statements only.

# Packages are simply directories of Python modules with a special __init__.py file,
# which enables A.B.C directory path syntax in imports. In an import of A.B.C, for
# example, the directory named A is located relative to the normal module import
# search of sys.path, B is another package subdirectory within A, and C is a module
# or other importable item within B.


# Relative Imports in Action

>>> import string
>>> string
<module 'string' from 'c:\Python26\lib\string.py'>

C:\test> c:\Python30\python
>>> import string
stringstringstringstringstringstringstringstring
>>> string
<module 'string' from 'string.py'>

# It imports the strin.py from test because it is current working directory, or the
# home directory

# But relative imports are not allowed in code that is not a file being used as part
# of the package:

>>> from . import string
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: Attempted relative import in non-package

# Lets do another example:

C:\test> del string*            # delete the string .py and .pyc files
C:\test> mkdir pkg              # make a directory pkg inside test

# The new pkg directory has these two files

# test\pkg\spam.py
import eggs                     # <== Works in 2.6 but not 3.0. To make it work in 3.0, use, from . import eggs
print(eggs.X)

# test\pkg\eggs.py
X = 99999
import string
print(string)

C:\test> c:\Python26\python
>>> import pkg.spam          
<module 'string' from 'c:\Python26\lib\string.pyc'>     
99999
# Here, it first performs a relative search for the module eggs when it runs spam.py,
# finds it and runs it on first import. It imports the string module then prints
# other statements.


# But you have to keep in mind that if a file such a string.py is in the home directory,
# or the current working directory, python will import it instead of string module from
# standard library

# test\string.py
print('string' * 8)

# test\pkg\spam.py
from . import eggs
print(eggs.X)

# test\pkg\eggs.py
X = 99999
import string                   # <== Gets string in CWD, not Python lib!
print(string)

C:\test> c:\Python26\python 
>>> import pkg.spam
stringstringstringstringstringstringstringstring
<module 'string' from 'string.py'>
99999


# Now, if we include the string.py inside the pkg and try to import it

C:\test> del string*

# test\pkg\spam.py
import string                   # <== Relative in 2.6, absolute in 3.0
print(string)

# test\pkg\string.py
print('Ni' * 8)


C:\test> c:\Python26\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>

# If we do a relative import of string instead of a normal import

# test\pkg\spam.py
from . import string            # <== Relative in both 2.6 and 3.0
print(string)

# test\pkg\string.py
print('Ni' * 8)

C:\test> c:\Python26\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>

# Now, if we delete the string.py file here, the relative import will fail, and python
# will report an error. Files that use imports with dots, though, are implicitly bound
# to a package directory and cannot be used elsewhere without code changes.



## ------------------------
## ADVANCED MODULE CONCEPTS
## ------------------------

# Data Hiding in modules

# As a special case, you can prefix names with a single underscore (e.g., _X) to
# prevent them from being copied out when a client imports a module with a
# from * statement.

# You can also assign a list of variable name stringsto the variable __all__ at
# the top level of the module. The from * Statement will copy out only those names
# listed in the __all__ list.

# Now, the _X and the __all__ convention has meaning only to the from * statement
# and does not amount to a privacy declaration.



# Mixed usage modes: __name__ and __main__

# If the file is being run as a top-module file, the __name__ is set to the string
# "__main__" when it starts

# If the file is being imported, the __name__ is set to the module's name as known
# by its clients

# Now you can use the __name__ to check whether the file is run or imported.
# For example:

# runme.py
def tester():
        print("It's christmas in heaven...")

if __name__ == '__main__':
        tester()

 # Now if we run the file as usual:
 % python runme.py
 It's chrismas in heaven...

 # And if we import the file for the first time, we can see that the function doesn't get
 # executed:
 % python
 >>> import runme

 # But the function is still available when the file is imported:
 % python
 >>> import runme
 >>> runme.tester()

 
# Therefore the __name__ serves as a variable to check the usage mode flag.

# Another example, including a unit test at the end of the file:

# min.py
print('I am:', __name__)

def minmax(test, *args):
        res = arg[0]
        for arg in args[1:]:
                tf test(arg, res)
                res = arg
        return res

def lessthan(x, y): return x < y           # In both of these truth tests, it returns a boolean
def grtrthan(x, y): return x > y              

if __name__ == '__main__':
        print(minmax(lessthan, 4, 2, 1, 5, 6, 3))         # Self-test code
        print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

# If we run the file in a console
% python min.py
I am: __main__
1
6

# Now if we import it for the first time, and the file is run
% python
>>> import min
I am: min
# You can import the function if you'd like:
>>> min.minmax(min.lessthan, 's', 'p', 'a', 'm')
'a'

# Using comman-line arguments with __name__:

"""
Various specialized string display formatting utilities.
Test me with canned self-test or command-line arguments.
"""

def commas(N):
        digits = str(N)
        assert(digits.isdigit())
        result = ''
        while digits:
                last3 = digits[-3:]
                digits = digits[:-3]
                result = (last3 + ',' + result) if result else last3    # Here the result is the last value from previous iteration, so we have to add last3 to the result
                #print last3
                #print result
        return result
def money(N, width = 0):
    """
    format number N for display with commas, 2 decimal digits,
    leading $ and sign, and optional padding: $ -xxx,yyy.zz
    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f'%N)[-2:]
    format = '%s%s.%s' % (sign, whole, fract)
    return '$%*s' % (width, format)

if __name__ == '__main__':
        def selftest():
                tests = 0, 1 # fails: −1, 1.23
                tests += 12, 123, 1234, 12345, 123456, 1234567
                tests += 2 ** 32, 2 ** 100
                for test in tests:
                        print(commas(test))
                print('')
                tests = 0, 1, 1.23, 1., 1.2, 3.14159
                tests += 12.34, 12.344, 12.345, 12.346
                tests += 2 ** 32, (2 ** 32 + .2345)
                tests += 1.2345, 1.2, 0.2345
                #tests += −1.2345, −1.2, −0.2345
                #tests += −(2 ** 32), −(2**32 + .2345)
                tests += (2 ** 100)#, −(2 ** 100)
                for test in tests:
                        print('%s [%s]' % (money(test, 17), test))

import sys
if len(sys.argv) == 1:
        selftest()
else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))

# Output:
C:\misc> python formats.py 999999999 0
$999,999,999.00

C:\misc> python formats.py −999999999 0
$-999,999,999.00

C:\misc> python formats.py 123456789012345 0
$123,456,789,012,345.00

C:\misc> python formats.py −123456789012345 25
$ −123,456,789,012,345.00

C:\misc> python formats.py
0
1
12
123
1,234
12,345
123,456
1,234,567
4,294,967,296
1,267,650,600,228,229,401,496,703,205,376


# You can also use getopt and optparse modules for advanced command-line processing. Check the python's stand
# library and manuals

# Setting and changing the sys.path settings. Since the sys.path is a list a paths, you can perform list
# operations on it. These changes only remain for the current session of python:

>>> import sys
>>> sys.path
['C:\\Users\\localhost\\Documents', 'C:\\Python26\\Lib\\idlelib', 'c:\\Python26', 'C:\\Python26\\python26.zip'
 , 'C:\\Python26\\DLLs', 'C:\\Python26\\lib', 'C:\\Python26\\lib\\plat-win', 'C:\\Python26\\lib\\lib-tk',
 'C:\\Python26\\lib\\site-packages']

>>> sys.path.append('C:\\Users')
['C:\\Users\\localhost\\Documents', 'C:\\Python26\\Lib\\idlelib', 'c:\\Python26', 'C:\\Python26\\python26.zip'
 , 'C:\\Python26\\DLLs', 'C:\\Python26\\lib', 'C:\\Python26\\lib\\plat-win', 'C:\\Python26\\lib\\lib-tk',
 'C:\\Python26\\lib\\site-packages', 'C:\\Users']

>>> sys.path = [r'C:\temp']
>>> sys.path
['C:\\temp']


# The as Extension for import and from

import modulename as name

# is equivalent to

import modulename
name = modulename
del modulename

# You can also use

from modulename import attrname as name

# This comes in handy for providing a short simple name for entire directory path when using the package import
# feature described before.

"""
mydir.py: a module that lists the namespaces of other modules
"""

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
        sepline = sepchr * seplen
        if verbose:
                print sepline
                print('name:', module.__name__, 'file:', module.__file__)
                print sepline
        count = 0
        for attr in module.__dict__:
                print('%02d)%s' % (count, attr), end = ' ')
                if attr.startwith(' '):
                        print('<buit-in name>')
                else:
                        print(getattr(module, attr))
                count += 1
        if verbose:
                print sepline
                print(module.__name__, 'has %d names' % count)
                print sepline
if __name__ == '__main__':
        import mydir
        listing(mydir)
        



# Importing modules by name string

# The module name in an import or from statement is a hardcoded variable name. Unfortunately, you can't use
# import statements directly to load a module given its name as a string. Python expects a name,
# not a string.

>>> import 'string'
...error...

>>> x = 'String'
>>> import x

# Here, python will try to import a file x.py, not the variable x

# But, to load a module by a string name, you have to use the exec statement.

>>> modname = 'string'
>>> exec('import ' + modname)
>>> string
<module 'string' from 'C:\Python26\lib\string.pyc'>

# The only real drawback to exec is that it must compile the import statement each time it runs. Therefore, it
# may run quicker if it uses the built-in __import__ function to load from a string name instead.
>>> modname = 'string'
>>> string = __import__(modname)
>>> string
<module 'string' from 'C:\Python26\lib\string.pyc'>



# Transitive Module Reloads
# There might a case where the module files which are being imported might contain other imported modules as
# well. In that case, a reload on a module in the top-level file might not reload the included module files
# inside the module to be reloaded. In other words, we have to use a different method to reload nested modules.

"""
reloadall.py: transitively reload nested modules
"""
import types

def status(module):
        print ('reloading' + str(module.__name__))

def transitive_reload(module, visited):
        if not module in visited:
                status(module)
                reload(module)
                visited[module] = None
                #print visited
                for attrobj in module.__dict__.values():
                        if type(attrobj) == types.ModuleType:
                                transitive_reload(attrobj, visited)
def reload_all(*args):
        visited = {}
        #print args
        for arg in args:
                #print arg
                if type(arg) == types.ModuleType:
                        #print type(arg)
                        transitive_reload(arg, visited)
if __name__ == '__main__':
        import reloadall
        reload_all(reloadall)

# Here, first we define the functions. The function reload_all is run which executes the transitive_reload
# function. In the reload_all function, we pass in the module name. Since, we pass by value, if check if
# the passed in value belongs to a module. If it does, we pass in values to another function, transitive_reload.
# That function checks if the module was in the dictionary visited, which means it was already reloaded.
# Now, to check if the module has nested modules to be reloaded, we go through the __dict__ attribute of
# the module, which then checks of any value is that of a module, if it does, it recursive reloads the
# transitive_reload again to reload all nested functions.

# Module Design Concepts

        # You're always in a module in python. Even the code written at the interactive prompt goes in a built-in
        # module called __main__

        # Minimize module coupling: global variables. They should be as independent of global variables used
        # within other modules as possible.

        # Make sure all the components of a module share a general purpose

        # Modules should rarely change other module's variables. It is OK to import and use them. You should
        # instead try to communicate through deviced such as function arguments and return values. Not cross-
        # module changes.



# Module Gotchas

# Statement Order Matters in Top-Level code. Mixing defs with top-level code is not only hard to read,
# it’s dependent on statement ordering. As a rule of thumb, if you need to mix immediate code with defs,
# put your defs at the top of the file and your top-level code at the bottom.

func1()                                 # Error: "func1" not yet assigned

def func1():
        print(func2())                  # Okay: "func2" looked up later
        
func1()                                 # Error: "func2" not yet assigned

def func2():
        return "Hello"

func1()                                 # Okay: "func1" and "func2" assigned



# from Copies Names but Doesn’t Link. For link, use qualification import.
# Example:
# nested1.py
X = 99
def printer(): print(X)

# nested2.py
from nested1 import X, printer          # Copy names out
X = 88                                  # Changes my "X" only!
printer()                               # nested1's X is still 99

% python nested2.py
99


# from * Can obscure the meaning of variables.
# from module import * can accidently overwrite names you're using in your scope. Worse, it can make difficult
# to determine where a variable comes from. This is especially true if the from * form is used on more than
# one imported file. So, the solution is to explicitly list the attributes you want in the from statement.



# reload May not Impact from Imports, since the attributes imported using from are copied into the namespace,
# and are not attributes of the module object. So reloading a module won't update. That means that after reloading
# a module, we may have to use from import to load the object again.

from module import function
function(1, 2, 3)                               # from import a function

import module
reload(module)
function(1, 2, 3)                               # Won't update the function

import module
reload(module)
from module import function                     # Will now update, or give up and use module.function()
function(1, 2, 3)


# Recursive imports may not work
# For example:

# recur1.py
X = 1
import recur2                           
Y = 2

# recur2.py
from recur1 import X
from recur1 import Y

% python
>>> import recur1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
File "recur1.py", line 2, in <module>
  import recur2
File "recur2.py", line 2, in <module>
  from recur1 import Y
ImportError: cannot import name Y

# Since, it can't find Y in the second from import statement in recur2.py at that moment. The solution is
# literally not to use from statement. Or, such problems can be eliminated bu using careful design, by
# minimizing couplings. You can also postpone the module name access by using import and qualification,
# instead of from, or by running them inside functions or near the bottom of the file to defer their
# execution.




## --------------------
## OOP: The Big Picture
## --------------------


##Multiple instances
##Classes are essentially factories for generating one or more objects. Every time we
##call a class, we generate a new object with a distinct namespace. Each object generated
##from a class has access to the class’s attributes and gets a namespace of its
##own for data that varies per object.
##
##Customization via inheritance
##Classes also support the OOP notion of inheritance; we can extend a class by redefining
##its attributes outside the class itself. More generally, classes can build up
##namespace hierarchies, which define names to be used by objects created from
##classes in the hierarchy.
##
##Operator overloading
##By providing special protocol methods, classes can define objects that respond to
##the sorts of operations we saw at work on built-in types. For instance, objects made
##with classes can be sliced, concatenated, indexed, and so on. Python provides
##hooks that classes can use to intercept and implement any built-in type operation.


##Attribute Inheritance search:
##See p.613-615

##Each class statement generates a new class object.
##
##Each time a class is called, it generates a new instance object.
##
##Instances are automatically linked to the classes from which they are created.
##
##Classes are linked to their superclasses by listing them in parentheses in a class
##header line; the left-to-right order there gives the order in the tree.

class C2: ....                  # Make class objects
class C3: ....
class C1(C2, C3): ....          # Linked to superclasses

I1 = C1()                       # Make instance objects
I2 = C1()                       # Linked to their classes

##Attributes are usually attached to classes by assignments made within class statements,
##and not nested inside function def statements
##
##Attributes are usually attached to instances by assignments to a special argument passed
##to functions inside classes, called self.

class C1(C2, C3):                       # Make and link class C1
        def __init__(self, who):        # Assign name: C1.setname
                self.name = who         # Self is either I1 or I2

I1 = C1()                               # Make two instances
I2 = C1()
I1.setname('bob')                       # Sets I1.name to 'bob'
I2.setname('mel')                       # Sets I2.name to 'mel'
print(I1.name)                          # prints 'bob'

##What __init__ means:
##You have a class definition, and object somewhere which has inside of it all those internal
##definitions. When you call that, class definition, it calls __init__, which is the
##constructor, and creates a pointer to the instance, and then it needs to have an access
##to that, so it calls it passing in self as the pointer to the instance. Then it says it
##has access to that piece in memory, and now inside that piece in memory, you can do
##things like, define self.name to be the value passed in for name. So it's saying, where
##is self pointing to, inside of that structure create a variable name 'name' and a value
##associated with it.

##So, Python calls the __init__ method each each an instance is generated from a class.
##It is a used representative of a larger class of methods called operator overloading
##methods, which will be discussed more. Such methods are inherited in class trees as
##usual and have double underscores at the start and end of their names to make them distinct.
##Python runs them automatically when instances that support them appear in corresponding
##operations. If omitted, and only simple methods are used, the operations are not supported.

##To implement set intersection, a class might either provide a method named intersect, or
##overload the & expression operator to dispatch to the required logic by coding a method named
##__and__.


##Code Resue:
        
class Employee:                                 # General superclass
        def computeSalary(self): ...            # Common or default behavior
        def giveRaise(self): ...
        def promote(self): ...
        def retire(self): ...

##But now, you can write a subclass of Employee,

class Engineer(Employee):                       # Specialized subclass
        def computeSalary(self):                # Something custom here

##Now because this computeSalary version appears lower in the class tree, it will replace
##or override the original version of computeSalary method, if you create an instance of
##this class. However, if you have to use the original version, create an instance of that
##class:

bob = Employee()                                # Default behaviour
mel = Engineer()                                # Default salary calculator

##So now you know that you can make any instances of any class in a tree, not just the ones
##at the bottom. The class you make an instance from determines the level at which the attribute
##search will begin.

##The instances can be collected in a list and may be used in the following way:

company = [bob, mel]                            # A composite object
for emp in company:
        print(emp.computeSalary())              # Run this object's version

##This concept can also be termed as encapsulation, as here it hides the interface differences,
##without the user caring about what those methods actually do.

def processor(reader, converter, writer):
        while 1:
                data = reader.read()
                if not data: break
                data = converter(data)
                writer.write(data)

##By passing in instances of subclasses that specialise the required read and write method
##interfaces for various data sources, we can reuse the processor function for any data
##source we need to use, both now and in future:

class Reader:
        def read(self): ...                     # Default behaviour and tools
        def other(self): ...
class FileReader(Reader):
        def read(self): ...                     # Read from a local file
class SocketReader(Reader):
        def read(self): ...                     # Read from a network socket
...

processor(FileReader(...), Converter, FileWriter(...))
processor(SocketReader(...), Converter, TapeWriter(...))
processor(FtpReader(...), Converter, XmlWriter(...))



## -------------------
## CLASS CODING BASICS
## -------------------

##There are two kinds of objects in Python's OOP model: class objects and instance objects, where
##each has its own namespace. Class objects come from statements and instances come from calls.
##Each time you call a class, you get a new instance of that class. Here are some of the
##properties of a class object:
##
##       * Class statements generates a new class object and assigns it to the name in the class
##        header. Like defs, class statements typically run when the files they are coded in are
##        first imported.
##
##       * Top-level assignments within a class statement and not nested inside a def generate
##        attributes in a class object.

class FirstClass:
        def setdata(self, value):
                self.data = value
        def display(self):
                print(self.data)

##Here, the name of the methods are now the attributes for the class, so they are FirstClass.setdata
##and FirstClass.display. The first argument in a method automatically receives an implied instance
##object when called. Now, if we create instances:

x = FirstClass()
y = FirstClass()

##Python searches the attribute by inheritance search, looking up names in linked objects. Since
##classes can generate multiple instances, methods must go throught the self argument to get to the
##instance to be processed. Therefore:

x.setdata('King Arthur')                # Call method: self is x
y.setdata(3.14159)                      # Runs: FirstClass.setdata(y, 3.14159)

>>> x.display()                         # Here, the self.data differs in each instance
King Arthur
>>> y.display()
3.14159

##You can also change instance attributes in the class itself, by assigning to self in methods,
##or outside the class, by assigning to an explicit instance object.

>>> x.data = 'New Value'
>>> x.display()
New Value

##We can also generate a brand new attribute in the instance's namespace by assigning to its name
##outside the class's method function.

>>> x.anothername = 'spam'              # new attribute set outside of a class!

##So, in python, instances inherit from classes and classes inherit from superclasses. The key
##ideas are:
##       * Superclasses are listed in parentheses in a class header.
##
##       * Classes inherit from their superclasses.
##
##       * Instances inherit attributes from all accessible classes.
##
##       * Logic changes are made by subclassing, not by changing superclasses.

##To explain inheritance more, lets take another example. Here, we create a class which is a
##subclass of FirstClass

class SecondClass(FirstClass):                          # inherits setdata
        def display(self):                              # changes or overrides display method
                print('Current value = "{0}"'.format(self.data))


##Now, lets make an instance of the SecondClass:

>>> z = SecondClass()
>>> z.setdata(42)                                       # finds setdata in FirstClass
>>> z.display()                                         # finds overridden method in SecondClass
Current value = "42"

##However, this override doesn't affect the instance to the first class. It is external to FirstClass
##and doesn't affect existing or future FirstClass objects:

>>> x.display()
New value


##Class name is just a variable assigned to an object when the class statement runs and the object
##can be referenced with any normal expression. 
##If it is in a module, you can import it and use it normally:

from modulename import FirstClass                # copy FirstClass to this scope
class SecondClass(FirstClass):
        def display(self): ...

##Or

import FirstClass
class SecondClass(modulename.FirstClass):
        def display(self): ...

##In a module, You can mix any number of varialbe, functions and classes with distinct names,
##and they become the respective module attributes.

# food.py
var = 1                                         # food.var
def func():                                     # food.func
        ...
class spam:                                     # food.spam
        ...
class ham:                                      # food.ham
        ...
class eggs:                                     # food.eggs
        ...

##The name of the module file and the attribute can be of same name as well. But it is better if a
##class name starts with an uppercase letter.


# person.py
class person:                             
        ...

import person                   # import module
x = person.person()

from person import person
x = person()

# person.py
class Person:                   # better naming
        ...

import person
x = person.Person()             # Better naming, lowercase for modules, uppercase for classes



##Operator overloading and classes
##
##Operator overloading lets objects coded with classes intercept and respond to operations that work
##on built-in types: addition, slicing, printing, qualification and so on. It's mostly just an automatic
##dispatch mechanism- expressions and other built-in operations route control to implementations in
##classes. Here's the idea:
##
##        * Methods named with double underscores __X__ are specially made to intercept operations.
##
##        * Such methods are called automatically when instances when instances appear in built-in
##        operations. If an instance object inherits an __add__ method, that method is called
##        whenever the object appear in a + expression. The method's return value becomes the result of
##        the corresponding expression.
##
##        * Classes may override most built-in type operations. This includes expressions, but also basic
##        operations like printing and object creation.
##
##        * There are no defaults for operator overloading methods, and none are required. So if a class
##        does not define or inherit an operator overloading method, it just means that the corresponding
##        operation is not supported for the class's instances. If no __add__ exists, then + expressions
##        raise exceptions.
##
##        * Operators allow classes to integrate with python's object model. By overloading type operations,
##        user-defined objects implemented with classes can act just like built-ins, and so provide
##        consistency with oython object model and interface.

##The __init__ method is known as the constructor method, and is used to initialize the object's state.
##It's the operator overloading method you'll use the most.
##
##Here's we take another example where,
##
##        * __init__ is run automaticlly when a new instance object is created from ThirdClass
##
##        * __add__ is run when a ThirdClass instance appears in a + expression
##
##        * __str__ is run when an object is printed; technically when it's converted to its print string
##        by the str built-in function

Let's look at the whole example here with the ThirdClass:

>>> class FirstClass:                                           # Create a class with setdata and display methods,
	def setdata(self, value):                               # which sets the value and prints the attribute
		self.data = value                               # accordingly
	def display(self):
		print(self.data)

		
>>> x = FirstClass()                                            # Now, x and y are instances of FirstClass
>>> y = FirstClass()
>>> x.setdata('King Arthur')                                    # Here a value is set for a class attribute,
>>> x                                                           # using a method, which is the preferred way. 
<__main__.FirstClass instance at 0x0000000002F71FC8>            # Here, showing that x is a instance at the location
>>> x.display()                                                 # displaying the value of x using the display method
King Arthur
>>> y.setdata(3.14159)                                          # Here, x and y are in different namespaces, so
>>> y.display()                                                 # even if they're instances of same class, their
3.14159                                                         # attributes will have values which are in different locations
>>> x.anothername = 'spam'                                      # An instance can also be assigned an attribute outside
>>> x.display()                                                 # of a class
King Arthur
>>> x.anothername
'spam'
>>> class SecondClass(FirstClass):                              # SecondClass is inherited from the FirstClass
	def display(self):                                      # Inherited display() is overridden
		print('Current value = "{0}"'.format(self.data))

		
>>> z = SecondClass()
>>> z.display()                                                 # Here, we create an instance of the SecondClass.
                                                                # If we try to display() before setting the value   
Traceback (most recent call last):                              # of the attribute inside the class to be displayed, it gives an
  File "<pyshell#34>", line 1, in <module>                      # error since the attribute doesn't exist in memory until
    z.display()                                                 # it is given a value and run, even though it is defined in the class.
  File "<pyshell#32>", line 3, in display                       # This is because instances begin their lives as empty namespace objects.
    print('Current value = "{0}"'.format(self.data))
AttributeError: SecondClass instance has no attribute 'data'
>>> z.setdata(42)                                               # set the value, now it can be displayed.
>>> z.display()                                                 
Current value = "42"
>>> dir(z)                                                      # display the methods available in the class with that instance
['__doc__', '__module__', 'data', 'display', 'setdata']
>>> x.display()
King Arthur
>>> y.display()
3.14159
>>> class ThirdClass(SecondClass):                              # A ThirdClass inherited from SecondClass. This has
	def __init__(self, value):                              # overloaded methods for addition, print and initialization.
		self.data = value
	def __add__(self, other):
		return ThirdClass(self.data + other)            # Here, an overloaded method for addition behaviour. It   
	def __str__(self):                                      # returns an instance as a result of addition of self.data
		return '[ThirdClass: {0}]'.format(self.data)    # and entered string which is passed in as the value
	def mul(self, other):                                   # argument for ThirdClass __init__ method
		self.data *= other

		
>>> a = ThirdClass('abc')
>>> a.display()
Current value = "abc"
>>> print a
[ThirdClass: abc]
>>> b = a + 'xyz'                                               # Here because of the overloaded method, this expression  
>>> b                                                           # makes the instance behave just like a built-in object
<__main__.ThirdClass instance at 0x0000000002F7D3C8>            # undergoing addition.
>>> b.display()
Current value = "abcxyz"
>>> print b                                                     # Print method is overloaded too. If it's not, it doesn't resort to default behaviour, it just echoes the instance. 
[ThirdClass: abcxyz]
>>> a.mul(3)
>>> a.display()
Current value = "abcabcabc"
        
##From this example, it is important to know that if you omit an operator overloading method and do not inherit
##it from a superclass, the corresponding operation will not be supported for your instances; if it’s attempted,
##an exception will be thrown (or a standard default will be used, wherever applicable).

##As a note, you can check the __init__ method in a class to see which attributes an instance will have by inspecting
##its class's __init__ method.

##Lets revise again by using a simple class example:

>>> class rec: pass                                             # Empty namespace object
>>> rec.name = 'Bob'                                            # Just objects with attributes, but these attributes live 
>>> rec.age = 40                                                # in the class namespace, 'rec'

>>> print(rec.name)                                             # Like a C struct
Bob

>>> x = rec()                                                   # Instances inherit class names
>>> y = rec()

>>> x.name, y.name                                              # name is inherited from the class attributes. Here, y.name value  
('Bob', 'Bob')                                                  # is derived from attribute inheritance search.

>>> x.name = 'Sue'                                              # But assignment changes inherited x namespace only
>>> rec.name, x.name, y.name
('Bob', 'Sue', 'Bob')

##In fact, as we’ll explore in more detail later, the attributes of a namespace object are usually implemented as dictionaries,
##and class inheritance trees are (generally speaking) just dictionaries with links to other dictionaries. If you know where to
##look, you can see this explicitly. The __dict__ attribute is the namespace dictionary for most class-based objects (some classes
##may also define attributes in __slots__, an advanced and seldom used feature that we’ll study later.

>>> rec.__dict__.keys()
['__module__', 'name', 'age', '__dict__', '__weakref__', '__doc__']

>>> x.__dict__.keys()                                   # only 'name' exists in the x namespace
['name']

>>> y.__dict__.keys()                                   # y namespace is still empty
[]

>>> x.__class__                                         # each instance has a link to its class
<class '__main__.rec'>

>>> rec.__class__                                       # echoes a tuple of a class's superclass(es)
(<class 'object'>,)                                     # returned empty tuple here

>>> ThirdClass.__bases__
(<class __main__.SecondClass at 0x0000000002F744C0>,)   # from previous example

##Classes and instances are just namespace objects, with attributes created on the fly by assignment. Those assignments usually
##happen within the class statements you code, but they can occur anywhere you have a reference to one of the objects in the tree.
##Even methods, normally created by a def nested in a class, can be created completely independently of any class object.

>>> def upperName(self):
        return self.name.upper()                        # This def is not part of a class yet, just a simple function, not a method

>>> upperName(x)                                        # Call as a simple function
'SUE'

>>> rec.newMethod = upperName                           # Assign a new attribute to a class as an asigned method

>>> x.newMethod()                                       # use the mthod with the instance object now
'SUE'

>>> y.newMethod()
'BOB'

>>> rec.newMethod(x)                                    # can call the method through instance or a class
'SUE'



## ------------------------
## A MORE REALISTIC EXAMPLE
## ------------------------


# File person.py (start)

class Person:
        def __init__(self, name, job=None, pay=0):      # Constructor takes three arguments. This is passed in to be attached to the instance.
                self.name = name                        # Fills out fields when created, also known as state information.
                self.job = job                          # self is the new instance object
                self.pay = pay                          # pay is local variable in the scope of the function, but self.pay is an attribute of the instance.

if __name__ == '__main__':                              # To make sure the canned test code only runs as a top level script
        # self test code
        bob = Person('Bob Smith')                               # Test the class
        sue = Person('Sue Jones', job='dev', pay=100000)        # Runs __init__ automatically
        print(bob.name, bob.pay)                                # Fetch attached attributes
        print(sue.name, sue.pay)                                # sue's and bob's attrs differ

$ python person.py
('Bob Smith', 0)                                        # To avoid the parentheses in print, use print('{0} {1}'.format(bob.name, bob.pay))
('Sue Jones', 100000)


# Adding behaviour methods

>>> name = 'Bob Smith'                                  # Simple string, outside class
>>> name.split()                                        # Extract last name
['Bob', 'Smith']
>>> name.split()[-1]                                    # Or [1], if always just two parts
'Smith'

>>> pay = 100000                                        # Simple variable, outside class
>>> pay *= 1.10                                         # Give a 10% raise
>>> print(pay)                                          # Or: pay = pay * 1.10, if you like to type
110000.0                                                # Or: pay = pay + (pay * .10), if you _really_ do!


class Person:
        def __init__(self, name, job=None, pay=0):      # Process embedded built-in types
                self.name = name                        
                self.job = job                          
                self.pay = pay                          

if __name__ == '__main__':                              # To make sure the following code executes as a top level script              
        # self test code
        bob = Person('Bob Smith')                               # Test the class
        sue = Person('Sue Jones', job='dev', pay=100000)        # Runs __init__ automatically
        print(bob.name, bob.pay)                                # Fetch attached attributes
        print(sue.name, sue.pay)
        print(bob.name.split()[-1])
        sue.pay *= 1.10
        print(sue.pay)

##The problem with this approach here is that suppose you make multiple instances of such a class and if you make such a hard-coded last name
##extraction formula, you have to update every occurrence of the class as an instance. This can get worse if it is scattered across multiple
##files.

##The point here is that we want to code operations on objects in class methods instead of littering them throughout our program.

class Person:
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))                        # using int to address rounding issues. Could also use round(N, 2), using decimal type, or using a%.2f or {0:.2f}

if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print('{0} {1}'.format(bob.name, bob.pay))
        print('{0} {1}'.format(sue.name, sue.pay))
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue.pay)

Bob Smith 0
Sue Jones 100000
Smith Jones
110000


## Providing Print displays for an instance, implementing simple encapsulation by self-containment

class Person:
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))
        def __str__(self):                                                      # Added overloaded method for print behaviour
                return '[Person: {0} {1}]'.format(self.name, self.pay)          # You can view options for __repr__, but it is less user friendly
if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print(bob)
        print(sue)
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue)

[Person: Bob Smith 0]
[Person: Sue Jones 100000]                                                      # print now exhibits a behaviour
Smith Jones
[Person: Sue Jones 110000]


## Coding Subclasses and customization by inheritance

class Manager(Person):
        def giveRaise(self, percent, bonus=0.10):
                self.pay = int(self.pay * (1 + percent + other))                # Bad way to write. Instead of copying the original version, we call that function and change the passing argument. 


class Manager(Person):
        def giveRaise(self, percent, bonus=0.10):
                Person.giveRaise(self, percent + bonus)                         # Better way; proves easy maintenance as we have to write less code
                                                                                # Also, if we change the base giveRaise logic in future, we'd have to change it only in the Person class
##Here, recall that the normal method call of this form:
##        instance.method(args...)
##is automatically translated by python into this equivalent form:
##        class.method(instance, args...)

##Therefore, if we apply the changes:

class Person:
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))
        def __str__(self):                                                      
                return '[Person: {0} {1}]'.format(self.name, self.pay)
        
class Manager(Person):                                                          # Make a subclass
        def giveRaise(self, percent, bonus=0.10):                               # Override the giveRaise() method with the appropriate changes
                Person.giveRaise(self, percent + bonus)
                
if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print(bob)
        print(sue)
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue)
        tom = Manager('Tom Jones', 'mgr', 50000)                                # Make a Manager:__init__
        tom.giveRaise(.10)                                                      # Runs a custom version
        print(tom.lastName())                                                   # Runs inherited method
        print(tom)                                                              # Runs inherited __str__

[Person: Bob Smith 0]
[Person: Sue Jones 100000]
Smith Jones
[Person: Sue Jones 110000]
Jones
[Person: Tom Jones 60000]

Now, if we add the following code at the end and print the results:

class Person:
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))
        def __str__(self):                                                      
                return '[Person: {0} {1}]'.format(self.name, self.pay)
        
class Manager(Person):                                                          
        def giveRaise(self, percent, bonus=0.10):                               
                Person.giveRaise(self, percent + bonus)
                
if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print(bob)
        print(sue)
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue)
        tom = Manager('Tom Jones', 'mgr', 50000)
        tom.giveRaise(.10)
        print(tom.lastName())
        print(tom)
        print '--All three--'.format()                                          
        for obj in (bob, sue, tom):
            obj.giveRaise(0.10)
            print(obj)

[Person: Bob Smith 0]
[Person: Sue Jones 100000]
Smith Jones
[Person: Sue Jones 110000]
Jones
[Person: Tom Jones 60000]
--All three--
[Person: Bob Smith 0]
[Person: Sue Jones 121000]
[Person: Tom Jones 72000]

##Therefore, we can learn the following from what we've seen so far:
##
## * Although we could have simply coded manager from scratch as new, independent code, we would have have had to 
##   reimplement all the behaviours in Person that are the same for Managers.
##
## * Although we could have simply changed the exising Person class in-place for the requirements of Manager's
##   giveRaise, doing so would probably break the places where we still need the original Person behaviour.
##
## * Although we could have simply changed the existing Person class in its entirety, renamed the copy to Manager,
##   and changed its giveRaise, doing so would reintroduce code redundancy that would double our work in the future:
##   changes made to Person in the future would not be picked up automatically, but would have to be manually
##   propagated to Manager's code. As usual, the cut-and-paste approach may seem quick now, but it doubles your work
##   in the future.

##In the previous code, when we created the 'tom' instance, it was pointless to prvide the 'mgr' value to the job
##attribute, since we already created an instance of the Manager class. So, we can create an __init__ in Manager
##that assumes that the job is 'mgr'.

class Person:
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))
        def __str__(self):
                return '[Person: {0}, {1}]'.format(self.name, self.pay)

class Manager(Person):
        def __init__(self, name, pay):
                Person.__init__(self, name, 'mgr', pay)                         # We redefine constructor which automatically calls the 
        def giveRaise(self, percent, bonus=0.10):                               # constructor from its superclass and passes in the 'mgr' as job
                return Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print(bob)
        print(sue)
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue)
        tom = Manager('Tom Jones', 50000)
        tom.giveRaise(.10)
        print(tom.lastName())
        print(tom)

[Person: Bob Smith, 0]
[Person: Sue Jones, 100000]
Smith Jones
[Person: Sue Jones, 110000]
Jones
[Person: Tom Jones, 60000]
                
##Therefore, OOP in python can be summarised as:
##        * Instance creation - filling out instances attributes
##        * Behaviour methods - encapsulating logic in class methods
##        * Operator overloading - providing behaviour for built-in operations like printing
##        * Customizing behaviour - redefining methods in subclasses to specialize them
##        * Customizing constructors - adding initialization logic to superclass steps

##Most of these concepts are based on: attribute inheritance search in object trees, the special self argument in methods
##and operator overloading's automatic dispatch to methods. We can also avoid code redundancy by wrapping up logic in
##methods and called back to superclass methods from extensions to avoid having multiple copies of the same code.

##Instead of inheritance from a superclass, there are other ways to combine classes too. For example, a common coding pattern
##involves nesting objects inside each other to build up composites. This idea is to code Manager class by embedding Person
##class, instead of inherting from it.

##This is done by using the __getattr__ operator overloading method to intercept undefined attribute fetches and delegate
##them to the embedded object with the getattr built-in.

class Person:
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))
        def __str__(self):
                return '[Person: {0}, {1}]'.format(self.name, self.pay)

class Manager:
        def __init__(self, name, pay):
                self.person = Person(name, 'mgr', pay)                          # Embed a Person object, self.person                        
        def giveRaise(self, percent, bonus=0.10):                               
                return self.person.giveRaise(percent + bonus)                   # Intercept and Raise
        def __getattr__(self, attr):
                return getattr(self.person, attr)                               # Delegate all other attrs through self.person
        def __str__(self):
                return str(self.person)                                         # Must overload in 3.0

if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print(bob)
        print(sue)
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue)
        tom = Manager('Tom Jones', 50000)
        tom.giveRaise(.10)
        print(tom.lastName())
        print(tom)

# Output
[Person: Bob Smith, 0]
[Person: Sue Jones, 100000]
Smith Jones
[Person: Sue Jones, 110000]
Jones
[Person: Tom Jones, 60000]

##This coding pattern usually known as delegation- a composite based structure that manages a wrapped object and propagates
##method calls to it. This pattern works in our example, but it is less suited than inheritance to the kinds of direct
##customizations we meant to express. Manager class isn't a Person here, so we need extra code to manually dispatch method
##calls to the embedded object; operator overloading methods like __str__ must be redefined. Still, object embedding, and
##design patterns based upon it, can be a very good fit when embedded objects require more limited interaction with the
##container than direct customization implies. A controller layer like this alternative Manager, for example, might
##come in handy if we want to trace or validate calls to another object’s methods.

bob = Person(...)
sue = Person(...)
tom = Person(...)

class Department:
        def __init__(self, *args):
                self.members = list(args)
        def addMember(self, person):
                self.members.append(person)
        def giveRaise(self, percent):
                for person in self.members:
                        person.giveRaise(percent)
        def showAll(self):
                for person in self.members:
                        print(person)

development = Department(bob, sue)                              # Embed objects in a composite
development.addMember(tom)
development.giveRaises(.10)                                     # Runs embedded objects' giveRaise
development.showAll()                                           # Runs embedded objects' __str__s

##Designing classes with compositions and delegations are going to be explored later.
        

##Using Introspection Tools

##  * These tools are special attributes and functions that give us access to some of the internals of objects'
##  implementations.
##
##  * The built-in instance.__class__ attribute gives a link from an instance to the class from which it was created.
##  Classes in turn have a __name__ just like modules, and a __bases__ sequence that provides access to superclasses.
##
##  * The built-in object.__dict__ attribute provides dictionary value for every attribute attached to a namespace
##  object.
##
##  * A class method has useful attributes, im_self, im_class and im_func to return the instance, the class and the 
##  function object respectively.

##If we take the previous example:

class Person:
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))
        def __str__(self):
                return '[Person: {0}, {1}]'.format(self.name, self.pay)

class Manager(Person):
        def __init__(self, name, pay):
                Person.__init__(self, name, 'mgr', pay)                         
        def giveRaise(self, percent, bonus=0.10):                               
                return Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print(bob)
        print(sue)
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue)
        tom = Manager('Tom Jones', 50000)
        tom.giveRaise(.10)
        print(tom.lastName())
        print(tom)
        bob.__class__                                           # Show bob's class and its name
        bob.__class__.__name__
        bob.__dict__.keys()                                     # attributes are like dictionary keys
        for key in bob.__dict__:
                print '{0} => {1}'.format(key, bob.__dict__[key])
        for key in bob.__dict__:
                print '{0} => {1}'.format(key, getattr(bob, key))     # getattr fetches the value of an object.attribute
                

[Person: Bob Smith, 0]
[Person: Sue Jones, 100000]
Smith Jones
[Person: Sue Jones, 110000]
Jones
[Person: Tom Jones, 60000]
pay => 0
job => None
name => Bob Smith
pay => 0
job => None
name => Bob Smith

##You can try out these introspection tools to work in a superclass that displays accurate class names and
##formats all attributes of an instance of any class.

"""Assorted class utilities and tools"""

class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their classes names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{0}={1}'.format(key, getattr(self, key)))
        return ','.join(attrs)
    def __str__(self):
        return '[{0}: {1}]'.format(self.__class__.__name__, self.gatherAttrs())
    
if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
    class SubTest(TopTest):
        pass
                
    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)

[TopTest: attr1=0,attr2=1]
[SubTest: attr1=2,attr2=3]

##Here in this example, we simply print the attribute names and their values in their respective instance
##namespaces derived from their classes. Instance X has been created from TopTest and Y is from SubTest,
##so we print their attributes attr1 and attr2, and their values in a specific format defined by the
##overloaded __str__ method.


##Another thing to keep in mind here is that the __dict__ attribute only displays instance attributes,
##not the attributes inherited from classes above it in the tree. Inherited class attributes are attached
##to the class only, not copied down to instances.
##If you want to include the inherited attributes too, you can use the __class__ link to climb up to the
##instance's class, and then use the __dict__ attribute there to fetch class attributes, and then iterate
##through the class's __bases__ attribute to climb to even higher superclasses (repeating as necessary).

##The simplest way to do it is by using the built-in dir call on the instance, it would include the
##inherited attributes in a sorted list.

>>> bob.__dict__.keys()                                                 # Instance attrs only
['pay', 'job', 'name']

>>> dir(bob)                                                            # + inherited attrs in classes
['__doc__', '__init__', '__module__', '__str__', 'giveRaise', 'job',
'lastName', 'name', 'pay']

##Name considerations in tool Classes
##
##If a subclass inherits AttrDisplay, it may want to use both if its __str__ and gatherAttrs. But there
##might be a case where the subclass wants to define a gatherAttrs of its own. In that case, the lower
##version of gatherAttrs will be used, if an instance of the subclass is created.

class AttrDisplay:

   
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{0}={1}'.format(key, getattr(self, key)))
        return ','.join(attrs)
    def __str__(self):
        return '[{0}: {1}]'.format(self.__class__.__name__, self.gatherAttrs())
    
if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
        def gatherAttrs(self):                                  # gatherAttrs overridden
            return 'Spam'
    class SubTest(TopTest):
        pass
                
    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)

[TopTest: Spam]
[SubTest: Spam]

##To minimize the chances of name collisions like this, you can prefix methods not meant for external use
##with a sinlge underscore: _gatherAttrs in our case. But this can be broken if another class defines
##_gatherAttrs too. But it is usually sufficient for methods internal to a class. A better method would
##be to use two underscores at the front of a method name only: __gatherAttrs in this case. Python
##automatically expands such names to include the enclosing class's name, which makes them unique.
##
##Our classes' final form:

class AttrDisplay:

        def gatherAttrs(self):
                attrs = []
                for key in sorted(self.__dict__):
                        attrs.append('{0} = {1}'.format(key, getattr(self, key)))
                return ', '.join(attrs)
        def __str__(self):
                return '[{0}: {1}]'.format(self.__class__.__name__, self.gatherAttrs())

class Person(AttrDisplay):
        def __init__(self, name, job=None, pay=0):
                self.name = name
                self.job = job
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1]
        def giveRaise(self, percent):
                self.pay = int(self.pay * (1 + percent))

class Manager(Person):
        def __init__(self, name, pay):
                Person.__init__(self, name, 'mgr', pay)
        def giveRaise(self, percent, bonus = 0.10):
                Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
        bob = Person('Bob Smith')
        sue = Person('Sue Jones', job='dev', pay=100000)
        print(bob)
        print(sue)
        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
        sue.giveRaise(.10)
        print(sue)
        tom = Manager('Tom Jones', 50000)
        tom.giveRaise(.10)
        print(tom.lastName())
        print(tom)

[Person: job = None, name = Bob Smith, pay = 0]
[Person: job = dev, name = Sue Jones, pay = 100000]
Smith Jones
[Person: job = dev, name = Sue Jones, pay = 110000]
Jones
[Manager: job = mgr, name = Tom Jones, pay = 60000]

##You can now see that it correctly displays the classes' name since they inherit the __str__ which has
##the appropriate format for displaying classes from which the instances are created.

##We can also use this general attribute display class in the future by saving it in a module and importing
##it, thus supporting reuse.

##Now, if we have to store the objects created by classes, and if we kill python they'll disappear since
##they're transient objects in memory and not stored in a permanent medium file like a file.

##So it is necessary to use 'object persistence' making objects live on after the program creates them exits.
##There are three ways to store objects in a database by standard library modules.

##pickle - Serializes arbitrary Python objects to and from a string of bytes.

##dbm (named anydbm in py2.6) - Implements an access-by-key filesystem for storing strings.

##shelve - Uses the other two modules to store Python objects on a file by key.

##Storing Objects on a Shelve Database:
 
from person import Person, Manager      # Storing the classes Person, Manager in a file (.py) and importing them
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve                           # importing shelve module from standard library
db = shelve.open('persondb')            # filename when objects are stored
for obj in (bob, sue, tom):             # store object's name attr as key
        db[obj.name] = obj              # store obj on shelve by key
db.close()                              # close after making changes

##Here, you'll notice that we can assign objects to shelves using their own names as keys. In a shelve,
##the key can be any string, including one we might create to be unique using tools such as process IDs
##and timestamps(available in the os and time modules). The only rule is that keys must be strings and
##should be unique since e can store just one object per key. The values we store under keys though can be
##Python objects of almost any sort: built-in types like strings, lists and dictionaries.

##The database is stored as a file now. If we have to check it, we can us ehe directory listing module in
##the python standard library

>>> import glob                          # Directory listing module: verify files are present               
>>> glob.glob('person*')
['persondb']

>>> print open('persondb').read()
'Tom Jones', (1024, 91)
...more omitted...

##The usual open() is not very user friendly for shelve files. In this case, we have to use shelve.open

>>> import shelve
>>> db = shelve.open('persondb')        # Reopen the shelve

>>> len(db)                             # Three 'records' stored
3

>>> db.keys()                           # list of keys, which is the index
['Bob Smith', 'Sue Jones', 'Tom Jones']

>>> db['Bob Smith']                     # Fetch the value of the key in the stored dictionary
[Person: job = None, name = Bob Smith, pay = 0]

>>> bob = db['Bob Smith']               # Assign the value to a variable, which actually becomes an instance

>>> print db
{'Tom Jones': <person.Manager instance at 0x0000000002678E48>,
 'Sue Jones': <person.Person instance at 0x0000000002678E08>,
 'Bob Smith': <person.Person instance at 0x0000000002678D88>}

>>> print(bob)                          # Runs __str__ from AttrDisplay()
[Person: job = None, name = Bob Smith, pay = 0]

>>> bob.lastName()                      # Runs lastName from Person
'Smith'

>>> for key in db:                      # Iterate, fetch and print
        print '{0} => {1}'.format(key, db[key])
        
Bob Smith => [Person: job = None, name = Bob Smith, pay = 0]
Sue Jones => [Person: job = dev, name = Sue Jones, pay = 100000]
Tom Jones => [Manager: job = mgr, name = Tom Jones, pay = 50000]

>>> for key in sorted(db, reverse=True):
        print '{0} => {1}'.format(key, db[key])

Tom Jones => [Manager: job = mgr, name = Tom Jones, pay = 50000]
Sue Jones => [Person: job = dev, name = Sue Jones, pay = 100000]
Bob Smith => [Person: job = None, name = Bob Smith, pay = 0]

##Notice that we don’t have to import our Person or Manager classes here in order to load
##or use our stored objects. For example, we can call bob’s lastName method freely, and
##get his custom print display format automatically, even though we don’t have his
##Person class in our scope here. This works because when Python pickles a class instance,
##it records its self instance attributes, along with the name of the class it was created
##from and the module where the class lives. When bob is later fetched from the shelve
##and unpickled, Python will automatically reimport the class and link bob to it.

##Shelves (really, the pickle module they use) automatically relink an instance to the
##class it was created from when that instance is later loaded back into memory.
##Python reimports the class from its module internally, creates an instance with its
##stored attributes, and sets the instance’s __class__ link to point to its original class.
##This way, loaded instances automatically obtain all their original methods (like
##lastName, giveRaise, and __str__), even if we have not imported the instance’s class
##into our scope.

##The upshot of this scheme is that class instances automatically acquire all their class
##behavior when they are loaded in the future. We have to import our classes only to
##make new instances, not to process existing ones.

##The downside is that classes and their module’s files must be importable when an
##instance is later loaded. More formally, pickleable classes must be coded at the top
##level of a module file accessible from a directory listed on the sys.path module
##search path.


##Updating a record on a Shelve

# updatedb.py
import shelve
db = shelve.open('persondb')                            # reopen the shelve again

for key in db:
    print '{0} => {1}'.format(key, db[key])             # print the existing records
    
sue = db['Sue Jones']                                   # create an instance from a record

sue.giveRaise(0.10)                                     # change an attribute by using a method

db['Sue Jones'] = sue                                   # update the change back to the shelve

for key in db:                                          # print the changes
    print '{0}\t=> {1}'.format(key, db[key])
    
db.close()                                              # close the shelve


Bob Smith => [Person: job = None, name = Bob Smith, pay = 0]
Sue Jones => [Person: job = dev, name = Sue Jones, pay = 100000]
Tom Jones => [Manager: job = mgr, name = Tom Jones, pay = 50000]
Bob Smith	=> [Person: job = None, name = Bob Smith, pay = 0]
Sue Jones	=> [Person: job = dev, name = Sue Jones, pay = 110000]
Tom Jones	=> [Manager: job = mgr, name = Tom Jones, pay = 50000]

Bob Smith => [Person: job = None, name = Bob Smith, pay = 0]                    # Run for the second time
Sue Jones => [Person: job = dev, name = Sue Jones, pay = 110000]                
Tom Jones => [Manager: job = mgr, name = Tom Jones, pay = 50000]
Bob Smith	=> [Person: job = None, name = Bob Smith, pay = 0]
Sue Jones	=> [Person: job = dev, name = Sue Jones, pay = 121000]          # Results updated
Tom Jones	=> [Manager: job = mgr, name = Tom Jones, pay = 50000]



## --------------------
## CLASS CODING DETAILS
## --------------------

##Eg.1
>>> class SharedData:
        spam = 42                       # Generates a class data attribute
>>> x = SharedData()                    # make two instances
>>> y = SharedData()
>>> x.spam, y.spam                      # They inherit and share 'spam'
(42, 42)

>>> SharedData.spam = 99
>>> x.spam, y.spam, SharedData.spam
(99, 99, 99)

>>> x.spam = 88
>>> x.spam, y.spam, SharedData.spam
(88, 99, 99)

##Eg.2
class MixedNames:                       # Define class
        data = 'spam'                   # Assign class attr
        def __init__(self, value):      # Assign method name
                self.data = value       # Assign instance attr
        def display(self):
                print(self.data, MixedNames.data)       # Instance attr, class attr

>>> x = MixedNames(1)                   # Make two instance objects
>>> y = MixedNames(2)                   # Each has its own data
>>> x.display(); y.display()            # self.data differs, MixedNames.data
1 spam
2 spam


##Methods

##Python maps instance method calls to class method function as follows:

instance.method(args...)

##is translated to:

class.method(instance, args...)

class NextClass:                        # Define class
        def printer(self, text):        # Define method, becomes a class attribute
                self.message = text
                print(self.message)

>>> x = NextClass()                     # Make instance

>>> x.printer('instance call')          # Call its method
instance call

>>> x.message                           # Instance changed
'instance call'

>>> x.message                           # Instance changed
'instance call'

>>> NextClass.printer(x, 'class call')  # Direct Class call
class call

>>> x.message                           # Instance changed again
'class call'

>>> NextClass.printer('bad call')       # method must be called with the NextClass Instance
...error...


##Inheritance - In Python, inheritance happens when an object is qualified and it involves searching an
##attribute definition tree. Every time you use an expression of the form object.attr, Python searches
##the namespace tree from bottom to top, beginning with object, looking for the first attr it can find.

##Instance may replace inherited attibutes completely provide attributes that a superclass expects to
##find, and extend superclass methods by calling back to the superclass from an overridden method.

##The subclass replaces Super's method function with its own specialized version, but within the
##replacement, Sub calls back to the version exported by Super to carry out the default behaviour. In
##other words, Sub.method just extends Super.method's behaviour, rather than replacing it completely.

##Example:

class Super:
        def method(self):
                print('in Super.method')

class Sub(Super):
        def method(self):                               # Override method
                print('starting Sub.method')            # Add actions here
                Super.method(self)                      # Run default action
                print('ending Sub.method')

>>> x = Super()                                         # Make a Super instance
>>> x.method()                                          # Runs Super.method
in Super.method

>>> x = Sub()                                           # Make a Sub instance
>>> x.method()                                          # Runs Sub.method, calls Super.method
starting Sub.method
in Super.method
ending Sub.method


##Class Interfacing Techniques

##Extension is one of the ways to interface with a superclass. There are more:

class Super:
        def method(self):
                print('in Super method')                # default behaviour
        def delegate(self):
                self.action()                           # Expect to be defined

class Inheritor(Super):                                 # Inherit method verbatim
        pass

class Replacer(Super):
        def method(self):
                print('in Replacer.method')             # Redefine or override Super.method()

class Extender(Super):                                  
        def method(self):                               # Extend method behaviour
                print('starting Extender.method')
                Super.method(self)
                print('ending Extender.method')

class Provider(Super):
        def action(self):                               # Fill in a required method called in Super
                print('in Provider.action')

if __name__ == '__main__':
        for klass in (Inheritor, Replacer, Extender):
                print('\n' + klass.__name__ + '.....')
                print klass;print klass()
                klass().method()                        # you have to call the instance
        print('\nProvider...')
        x = Provider()
        x.delegate()                                    # delegate method is called through provider instance

# output

Inheritor.....
__main__.Inheritor
<__main__.Inheritor instance at 0x000000000261C6C8>
in Super method

Replacer.....
__main__.Replacer
<__main__.Replacer instance at 0x000000000261C6C8>
in Replacer.method

Extender.....
__main__.Extender
<__main__.Extender instance at 0x000000000261C6C8>
starting Extender.method
in Super method
ending Extender.method

Provider...
in Provider.action


##On the initial x.delegate call, python finds the delegate method in Super by searching the provider instance
##and above. The x is passed in to the method's self argument as usual.

##Then, inside the Super.delegate method, self.action invokes a new, independent inhertance search of self and
##above. Because self references a Provider instance, the action method is located in the Provider subclass.

##This type of class methodology is known as an abstract superclass. This 'filling in the blanks" sort of coding
##structure of typical of OOP frameworks. In this case, if the expected method is not defined in a subclass,
##python raises an exception.

##You can make such subclass requirements more obvious with assert statements or by raising the built-in
##NotImplementedError exception with raise statements.

class Super:
        def delegate(self):
                self.action()
        def action(self):
                assert False, 'action must be defined!'                 # If this version is called

>>> X = Super()
>>> X.delegate()
AssertionError: action must be defined!


class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined !')

>>> X = Super()
>>> X.delegate()
NotImplementedError: action must be defined!



##Special Implementation for an abstract superclass

##Abstract superclasses, which require methods to be filled in by subclasses, may be implemented with special
##class syntax.

##Since this topic uses function decorators and metaclass declarations, we'll meet this later.


##Namespaces: The whole story

##Unqualified names (e.g., X) deal with scopes, they follow LEGB rules:
##        Assignment(X = value) creates or changes the name X in the current local scope, unless
##        declared global. If it's just a Reference(X), then it looks for the name X in the current
##        local scope, then any and all enclosing functions, then the current global scope, then
##        the built-in scope (LEGB)

##Qualified attribute names (e.g., object.X) use object namespaces:
##        Creates or alters the attribute name X in the namespace of the object being qualified, and
##        none other. Inheritance attribute search happens only on attribute reference not on
##        attribute assignment.

##Some scopes initialize object namespaces(for modules and classes).


##The "Zen" of Python Namespaces: Assignments Classify Names

##In python, the place where you 'assign' a name is crucial - it fully determines the scope or the
##object in which a name will reside.

# manynames.py

X = 11                                  # Global (module) name/attribute (X, or manynames.X)

def f():
        print(X)                        # Access global X (11)

def g():
        X = 22                          # Local (function) variable (X, hides module X)
        print(X)

class C:
        X = 33                          # Class attribute (C.X)
        def m(self):
                X = 44                  # Local variable in method
                self.X = 55             # Instance attribute (instance.X)

if __name__ == '__main__':
        print(X)                        # 11: module (a.k.a. manynames.X outside file)
        f()                             # 11: global
        g()                             # 22: local
        print(X)                        # 11: module name unchanged

        obj = C()                       # Make instance of class C
        print obj.__dict__              # {}: current namespace attributes, not inherited attributes
        print(obj.X)                    # 33: class attribute(a.k.a. obj.X if no X in instance)

        obj.m()                         # create new attribute by executing method and attach X to instance namespace
        print obj.__dict__              # {'X':55} : Added namespace attribute
        print(obj.X)                    # 55: instance
        print(C.X)                      # 33: class

        print(C.m.X)                    # error - only visible inside method
        print(g.X)                      # error - only visible inside function


##Now if we import the file manynames.py and test the imported attributes:

# otherfile.py

import manynames

X = 66
print(X)                                # 66: the global here
print(manynames.X)                      # 11: globals become attributes after imports

manynames.f()                           # 11: manynames's X, not the one here!
manynames.g()                           # 22: local in other

print(manynames.C.X)                    # 33: attribute of class in other module
I = manynames.C()
print(I.X)                              # 33: still from class here
I.m()
print(I.X)                              # 55: now from instance!


##Namespace Dictionaries

>>> class super:
        def hello(self):
                self.data1 = 'spam'

>>> class sub(super):
        def hola(self):
                self.data2 = 'eggs'
                
                
>>> X = sub()
>>> X.__dict__                                          # Current Instance namespace dictionary
{}

>>> X.__class__
<class __main__.sub at 0x0000000002FA0620>
>>> X.__class__.__name__                                # X is an instance of class 'sub'
'sub'

>>> sub.__bases__                                       # sub is a subclass of super
(<class __main__.super at 0x0000000002FA05C8>,)

>>> super.__bases__                                     # super doesn't inherit from other class(es)
()

>>> Y = sub()

>>> X.hello()                                           # runs a method through an instance
>>> X.__dict__
{'data1': 'spam'}                                       # namespace updated

>>> X.hola()                                            
>>> X.__dict__
{'data1': 'spam', 'data2': 'eggs'}

>>> sub.__dict__                                        # view namespace attributes for the sub class
{'__module__': '__main__', '__doc__': None, 'hola': <function hola at 0x0000000002FE90B8>}
>>> sub.__dict__.keys()                                 
['__module__', '__doc__', 'hola']

>>> super.__dict__.keys()
['__module__', 'hello', '__doc__']

>>> Y.__dict__
{}

>>> X.data1, X.__dict__
('spam', {'data1': 'spam', 'data2': 'eggs'})

>>> X.data1, X.__dict__['data1']                        # echo the values of attributes in the instance X namespace
('spam', 'spam')

>>> X.data3 = 'toast'                                   

>>> X.__dict__
{'data1': 'spam', 'data3': 'toast', 'data2': 'eggs'}

>>> X.__dict__['data3']
'toast'

>>> X.__dict__['data3'] = 'ham'
>>> X.__dict__['data3']
'ham'

>>> dir(X)                                              # returns the inherited and namespace attributes
['__doc__', '__module__', 'data1', 'data2', 'data3', 'hello', 'hola']
>>> dir(sub)
['__doc__', '__module__', 'hello', 'hola']
>>> dir(Y)
['__doc__', '__module__', 'hello', 'hola']
>>> dir(super)
['__doc__', '__module__', 'hello']


##Namespace links

# classtree.py

"""
Climb inheritance trees using namespace links,
displaying higher superclasses with indentation
"""

def classtree(cls, indent):
        print('.' * indent + cls.__name__)              # print class name here
        for supercls in cls.__bases__:
                classtree(supercls, indent + 3)         # recursion is used here to climb up in classes

def instancetree(inst):
        print('Tree of %s' % inst)                      # show instance
        classtree(inst.__class__,3)                     # climb to its class

def selftest():
        class A:        pass
        class B(A):     pass
        class C(A):     pass
        class D(B, C):  pass
        class E:        pass
        class F(D, E):  pass
        instancetree(B())
        instancetree(F())
if __name__ == '__main__':
        selftest()

##Output
Tree of <__main__.B instance at 0x000000000253C548>
...B
......A
Tree of <__main__.F instance at 0x000000000253C548>
...F
......D
.........B
............A
.........C
............A
......E

##We can reuse the instancetree() function for other classes too:

>>> class Emp: pass

>>> class Person(Emp): pass
>>> bob = Person()

>>> import classtree
>>> clastree.instancetree(bob)
Tree of <__main__.Person instance at 0x000000000256C2C8>
...Person
......Emp



##Documentation Strings Revisited

# docstr.py

"I am: docstr.__doc__"

def func(args):
        "I am: docstr.func.__doc__"
        pass

class spam:
        "I am: spam.__doc__ or docstr.spam.__doc__"
        def method(self, arg):
                "I am: spam.method.__doc__ or self.method.__doc__"
                pass

>>> import docstr
>>> docstr.__doc__
'I am: docstr.__doc__'


>>> docstr.func.__doc__
'I am: docstr.func.__doc__'

>>> docstr.spam.__doc__
'I am: spam.__doc__ or docstr.spam.__doc__'

>>> docstr.spam.method.__doc__
'I am: spam.method.__doc__ or self.method.__doc__'

>>> help(docstr)                                                # PyDoc tool
Help on module docstr:

NAME
    docstr - I am: docstr.__doc__

FILE
    c:\users\localhost\documents\eclipse\exercises\docstr.py

CLASSES
    spam
    
    class spam
     |  I am: spam.__doc__ or docstr.spam.__doc__
     |  
     |  Methods defined here:
     |  
     |  method(self, arg)
     |      I am: spam.method.__doc__ or self.method.__doc__

FUNCTIONS
    func(args)
        I am: docstr.func.__doc__

        
## --------------------
## OPERATOR OVERLOADING
## --------------------


##Operator Overloading simply means intercepting built-in operations in class methods. Python
##automatically invokes such methods when instances of the class appear in built-in operations,
##and the method's return value becomes the result of the corresponding operation.
##
## * Operator overloading lets classes intercept normal python operations
##
## * Classes can overload all python expression operators
##
## * Classes can also overload built-in operations such as printing, function calls, attribute access, etc
##
## * Overloading makes class instances act more like built-in types.
##
## * Overloading is implemented by providing specially named class methods.

##The first example demonstrates a method to intercept instance construction (__init__) as well as
##one for catching subtraction expressions (__sub__):

class Number:
        def __init__(self, start):                      # Constructor, initialization
                self.data = start
        def __sub__(self, other):                       # On instance, subtraction
                return Number(self.data - other)        # Return new instance

>>> X = Number(5)
>>> Y  = X - 2
>>> Y.data
3

##Operator overloading methods are also all optional—if you don’t code or inherit one, that
##operation is simply unsupported by your class, and attempting it will raise an exception.


##Indexing and Slicing: __getitem__ and __setitem__

class Indexer:
        def __getitem__(self, index):                   # catches the instance with an index with its item
                return index ** 2

>>> X = Indexer()
>>> X[1]
1
>>> X[2]
4
>>> for i in range(20):
	print X[i],

0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361


>>> L = [1, 3, 5, 7, 9, 11]                             # Common slicing operations
>>> L[2:4]
[5, 7]
>>> L[1:]
[3, 5, 7, 9, 11]
>>> L[-1:]
[11]
>>> L[:-1]
[1, 3, 5, 7, 9]
>>> L[::2]
[1, 5, 9]
>>> L[slice(2,4)]
[5, 7]
>>> L[slice(1, None)]
[3, 5, 7, 9, 11]
>>> L[slice(None, -1)]
[1, 3, 5, 7, 9]
>>> L[slice(None, None, 2)]
[1, 5, 9]

##Now, if we have to implement these operations for the instance using the __getitem__, we have to
##make some changes:

>>> class Indexer:
        data = [1, 3, 5, 7, 9, 11]
        def __getitem__(self, index):                              # intercept index or slice
                print 'getitem: {0}'. format(index)
                return self.data[index]                         # perform index or slice
                
>>> X = Indexer()

>>> X[0]
getitem: 0
1
>>> X[1]
getitem: 1
3
>>> X[-1]
getitem: -1
11
>>> X[2:4]
getitem: slice(2, 4, None)
[5, 7]
>>> X[1:]
getitem: slice(1, 9223372036854775807L, None)
[3, 5, 7, 9, 11]
>>> X[:-1]
...error...

##This index query works in the book, but a small change has to be made in the class statement:

class Indexer:
	data = [1, 3, 5, 7, 9, 11]
	def __len__(self):                                      # __len__ has to be added
                return len(self.data)
	def __getitem__(self, index):
		print 'getitem: {0}'.format(index)
		return self.data[index]

##So now:

>>> X = Indexer()
>>> X[:-1]
getitem: slice(0, 5, None)
[1, 3, 5, 7, 9]
>>> X[::2]
getitem: slice(None, None, 2)
[1, 5, 9]

##In py2.6, you can also define __getslice__ and __setslice__ methods to intercept slice and
##assignments specifically. They were passed the bounds of the slice expression and were
##preferred over __getitem__ and __setitem__ for slices.


##Index iteration with __getitem__: The __getitem__ is also a way to overload iteration in Python.
##If this method is defined, for loops call the class’s __getitem__ each time through, with
##successively higher offsets. Therefore it works for any construct that demands iteration.

class Stepper:
        def __getitem__(self, index):
                return self.data[index]

>>> X = Stepper()                       # X is a stepper object
>>> X.data = 'Spammer'
>>> for item in X:                      # for loops call __getitem__, indexes items from 0 to N
	print item,

S p a m m e r

>>> 'p' in X                            # All call __getitem__ too
True

>>> [c for c in X]                      # List comprehension
['S', 'p', 'a', 'm', 'm', 'e', 'r']

>>> map(str.upper, X)                   # map calls
['S', 'P', 'A', 'M', 'M', 'E', 'R']

>>> (a, b, c, d, e, f, g) = X           # Sequence assignments
>>> a, d, f
('S', 'm', 'e')

>>> list(X)
['S', 'p', 'a', 'm', 'm', 'e', 'r']
>>> tuple(X)
('S', 'p', 'a', 'm', 'm', 'e', 'r')
>>> ''.join(X)
'Spammer'

>>> X
<__main__.Stepper instance at 0x0000000002FE77C8>


##Iterator Objects: __iter__ and __next__

##For an iteration context to overload an iterator method like __getitem__ works as described, it
##is better to use the __iter__ method. Technically, iteration contexts work by calling the iter
##built-in function to try to find an __iter__ method, which is expected to return an iterator
##object. If it’s provided, Python then repeatedly calls this iterator object’s __next__ method
##to produce items until a StopIteration exception is raised. If no such __iter__ method is found,
##Python falls back on the __getitem__ scheme and repeatedly indexes by offsets as before, until
##an IndexError exception is raised.

##Just note that in py2.6, object.__next__() will be described as object.next() or the next(object).

class Squares:
        def __init__(self, start, stop):
                self.value = start - 1
                self.stop = stop
        def __iter__(self):
                return self
        def __next__(self):                             # use def next(self) in py2.6
                if self.value == self.stop:
                        raise StopIteration
                self.value += 1
                return self.value ** 2

>>> for item in Squares(1, 5):
	print item,

1 4 9 16 25        

##Here the iterator object is the instance 'self', since the next() method is a part of the class.
##The end of the iteration of indicated by a raise exception.

>>> X = Squares(1, 5)                                   # Iterate manually: what loops do
>>> I = iter(X)                                         # iter calls __iter__
>>> next(I)                                             # next calls __next__
1
>>> next(I)
4
>>> next(I)
9
>>> next(I)
16
>>> next(I)
25
>>> next(I)

Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    next(I)
StopIteration

##Keep in mind that the __iter__ and the __next__ method are really only for iteration, and not indexing
##and therefore you have to include the overloading __getitem__ for that:

>>> X = Squares(1, 5)
>>> X[1]
.....
AttributeError: Squares instance has no attribute '__getitem__'

##You also have to be aware that the class's __iter__ method may be designed for a single traversal,
##not many. For example, the Squares class is a one-shot iteration. You have to make a new iterator
##object for each new iteration.

>>> X = Squares(1, 5)

>>> [n for n in X]                                      # Exhausts items
[1, 4, 9, 16, 25]
>>> [n for n in X]                                      # Now, it's empty
[]

>>> [n for n in Squares(1, 5)]                          # makes a new iterator each time
[1, 4, 9, 16, 25]
>>> [n for n in Squares(1, 5)]
[1, 4, 9, 16, 25]

>>> list(Squares(1, 5))                                 # makes a new iterator each time
[1, 4, 9, 16, 25]
>>> list(Squares(1, 5))
[1, 4, 9, 16, 25]


##Multiple Iterations on one object

##If we do multiple with for loops, which we've studied earlier:

>>> S = 'ace'
>>> for x in S:
...     for y in S:
...             print(x + y, end=' ')
...
aa ac ae ca cc ce ea ec ee

class SkipIterator:
        def __init__(self, wrapped):
                self.wrapped = wrapped                          # Iterator state information
                self.offset = 0
        def __next__(self):                                     # Use next(self) in py2.6
                if self.offset >= len(self.wrapped):            # Terminate iterations
                        raise StopIteration
                else:
                        item = self.wrapped[self.offset]        # else return and skip
                        self.offset += 2
                        return item
class SkipObject:
        def __init__(self, wrapped):                            # Save item to be used
                self.wrapped = wrapped
        def __iter__(self):
                return SkipIterator(self.wrapped)               # New iterator each time

if __name__ == '__main__':
        alpha = 'Abcdef'
        skipper = SkipObject(alpha)                             # Make container object
        I = iter(skipper)                                       # Make an iterator on it
        print(next(I), next(I), next(I))                        # Visit offsets 0, 2, 4

        for x in skipper:                                       # for calls __iter__ automatically
                for y in skipper:                               # Nested fors call __iter__ again each time
                print(x + y),                                   # Each iterator has its own state, offset

# Output:
('A', 'c', 'e')
AA Ac Ae cA cc ce eA ec ee

##By contrast, our earlier Squares example supports just one active iteration, unless we call
##Squares again in nested loops to obtain new objects. Here, there is just one SkipObject, with
##multiple iterator objects created from it.

##As before if we write a similar solution using for loops:

>>> S = 'Abcdef'
>>> for x in S[::2]:
        for y in S[::2]:                                        # New object on each iteration
                print(x + y),

AA Ac Ae cA cc ce eA ec ee               

##Now, this isn't quite the same since: Each slice expression will physically store the result list
##all at once in memory, iterators on the other hand produce one value at a time, which can save space.
##Second, slices produce new objects, so we're not iterating over same object in multiple places.
##So, the class method provides a better solution. To get closer to this idea using for clauses:

>>> S = 'Abcdef'
>>> S = S[::2]
>>> S
'Ace'
>>> for x in S:
        for y in S:                                             # Same object, new iterators
                print(x + y),

AA Ac Ae cA cc ce eA ec ee

##This method is closer to the class, but it still stores the slice result in memory all at once.


##Membership: __contains__, __iter__ and __getitem__

##Classes implement the 'in' membership operator as an iteration, suing either the __iter__ method
##or the __getitem__ method. To support more specific member classes may use __contain__ method,
##which is preferred over __iter__, which is preferred over __getitem__. 

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, item):                    # Fallback for iteration
        print ('get[{0}]:'.format(item)),              # Also for index, slice
        return self.data[item]
    def __iter__(self):                             # Preferred for iteration
        print ('iter=>'.format()),                  # Allows only 1 active iterator
        self.ix = 0
        return self
    def next(self):
        print 'next:',
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):                      # Preferred for 'in'
        print 'contains: ',
        return x in self.data
    
X = Iters([1, 2, 3, 4, 5])                          # Make instance
print(3 in X)                                       # Membership
for i in X:                                         # For loops
    print ('{0} |'.format(i)),

print()                                             # To get a newline
print([i**2 for i in X])                            # Other iteration contexts
print map(bin, X)                                   # map binary conversion to sequence items

I = iter(X)
while True:                                         # Manual iteration (what other contexts do)
    try:
        print ('{0} @'.format(next(I))),
    except StopIteration:
        break

# Output. You'll notice that __getitem__ is never called. 
contains:  True
iter=> next: 1 | next: 2 | next: 3 | next: 4 | next: 5 | next: ()
iter=> next: next: next: next: next: next: [1, 4, 9, 16, 25]
iter=> next: next: next: next: next: next: ['0b1', '0b10', '0b11', '0b100', '0b101']
iter=> next: 1 @ next: 2 @ next: 3 @ next: 4 @ next: 5 @ next:

# Now, if we comment out its __contains__ method, the membership falls back on __iter__
iter=> next: next: next: True
iter=> next: 1 | next: 2 | next: 3 | next: 4 | next: 5 | next: ()
iter=> next: next: next: next: next: next: [1, 4, 9, 16, 25]
iter=> next: next: next: next: next: next: ['0b1', '0b10', '0b11', '0b100', '0b101']
iter=> next: 1 @ next: 2 @ next: 3 @ next: 4 @ next: 5 @ next:

# Now, if we comment out both __contains__ and __iter__ method. The indexes falls back on
# __getitem__
get[0]: get[1]: get[2]: True
get[0]: 1 | get[1]: 2 | get[2]: 3 | get[3]: 4 | get[4]: 5 | get[5]: ()
get[0]: get[1]: get[2]: get[3]: get[4]: get[5]: [1, 4, 9, 16, 25]
get[0]: get[1]: get[2]: get[3]: get[4]: get[5]: ['0b1', '0b10', '0b11', '0b100', '0b101']
get[0]: 1 @ get[1]: 2 @ get[2]: 3 @ get[3]: 4 @ get[4]: 5 @ get[5]:


##Attribute Reference: __getattr__ and __setattr__

##The __getattr__ is called whenever an instance is qualified with an unknown attribute. It is not
##called if an attribute is found in inheritance tree search. The __getattr__ is called only when
##an attribute is referenced, not on assignment.

# Example

class empty:
        def __getattr__(self, attrname):
                if attrname == 'age':
                        return 40
                else:
                        raise AttributeError, attrname
>>> X = empty()
>>> X.age                                               # gets routed to __getattr__
40
>>> X.name
...error...
AttributeError: name

##Related overloading method __setattr__ intercepts all attribute assignments. If this method is used
##self.attr = value becomes self.__setattr__(attr, value). Make sure that assignments within
##__setattr__ calls are done by indexing the attribute dictionary.

##So use self.__dict__.['attrname'] = value, and not self.attrname = value

class AccessControl:
        def __setattr__(self, attr, value):
                if attr == 'age':
                        self.__dict__[attr] = value
                else:
                        raise AttributeError, attr + ' not allowed'

>>> X = AccessControl()
>>> X.age = 40                                          # Calls __setattr__
>>> X.age
40
>>> X.name = 'mel'
...text omitted...
AttributeError: name not allowed              


##Similarly, the __getattribute__ method intercepts all attribute fetches, not just those that
##are undefined, but when using it you must be more cautious than with __getattr__ to avoid loops.

##Now, this example demonstrates the previous example to allow each subclass to have its own
##list of private names that cannot be assigned to its instances:

class PrivateExec(Exception): pass                      # More on Exception later

class Privacy:
        def __setattr__(self, attrname, value):
                if attrname in self.privates:
                        raise PrivateExec(attrname, self)
                else:
                        self.__dict__[attrname] = value
class Test1(Privacy):                                   # Test 1 has a private name
        privates = ['age']

class Test2(Privacy):
        privates = ['name', 'pay']
        def __init__(self):
                self.__dict__['name'] = 'Tom'

>>> x = Test1()
>>> y = Test2()

>>> x.name = 'Bob'
>>> y.name = 'Sue'
...error...

>>> y.age = 30
>>> x.age = 40
...error...


##String representation: __repr__ and __str__

##These methods are called automatically when class instances are printed or converted to strings.

class adder:                                            # this class has no overloading print or str methods
        def __init__(self, value=0):
                self.data = value
        def __add__(self, other):
                self.data += other

class addrepr(adder):
        def __repr__(self):
                return 'addrepr({0})'.format(self.data)
        
# Output
>>> x = addrepr(2)
>>> x + 3
>>> print x
addrepr(5)
>>> str(x), repr(x)
('addrepr(5)', 'addrepr(5)')

##Note that __repr__ is used for interactive echoes, repr function, and nested apperances
##as well for print and str if no __str__ is present. If both are present, then __str__
##overrides __repr__ for print and str functions.

##Also, keep in mind that both __str__ and __repr__ should return strings, otherwise
##an error is raised. You may also use a converter if needed.

##When there's an object nested, for e.g., in a list, then it falls back to __repr__
##for printing. For example:

class adder:                                            # this class has no overloading print or str methods
        def __init__(self, value=0):
                self.data = value
        def __add__(self, other):
                self.data += other

class addboth(adder):
        def __str__(self):
                return '[Str: {0}]'.format(self.data)
        def __repr__(self):
                return '[Repr: {0}]'.format(self.data)
        
>>> X = addboth(4)
>>> X + 2
>>> X
[Repr: 6]                                               # using __repr_ for echoes
>>> print X                                             
[Str: 6]                                                # using __str__ for print
>>> str(X)                                              # using __str__ for str
'[Str: 6]'
>>> objs = [addboth(3), addboth(4)]
>>> for x in objs:
	print x                                         # using __str__ for print

	
[Str: 3]
[Str: 4]
>>> print objs
[[Repr: 3], [Repr: 4]]                                  # using __repr__ for print


##Right-Side and In-Place Addition: __radd__ and __iadd__

##Since the __add__ method does not support the use of instance objects on the right side
##of the + operator, we have to use the __radd__ method. It is only called when instance
##is on the right side of the operator.

class Commuter:
        def __init__(self, val):
                self.val = val
        def __add__(self, other):
                print 'add: {0}, {1}'.format(self.val, other)
                return self.val + other
        def __radd__(self, other):
                print 'radd: {0}, {1}'.format(self.val, other)
                return self.val + other

>>> x = Commuter(88)
>>> y = Commuter(99)

>>> x + 1                                       # using __add__ for instance on LHS
add: 88, 1
89
>>> 1 + y                                       # using __radd__ for instance on RHS
radd: 99, 1
100
>>> x + y                                       # LHS is given preference first.
add: 88, <__main__.Commuter instance at 0x0000000002FFDDC8>
radd: 99, 88
187

##There may be a case where a class may be need to be propagated to the result of an add.
##In the previous case, an int is returned as the result; but we want an instance of the
##class. Here, we type test if the other value to be added to the instance is already an
##instance of the Commuter class. If that is true, the value to be added is just an attribute
##taken from the instance in order to avoid an instance being added and thus triggering
##__radd__. So when we return, we're just adding attribute values and not instances.
##The final value is passed as an argument for another instance creation, which is
##the desirable return object.

class Commuter:
        def __init__(self, val):
                self.val = val
        def __add__(self, otherSelf):                   # adding two instances, from which attributes are added
                if isinstance(otherSelf, Commuter):     # testing for instance
                        otherSelf = otherSelf.val
                return Commuter(self.val + otherSelf)   
        def __radd__(self, other):
                return Commuter(self.val + other)
        def __str__(self):
                return '<Commuter: {0}>'.format(self.val)

>>> x = Commuter(88)
>>> y = Commuter(99)

>>> print(x + 10)                                       # Result is the same instance
<Commuter: 98>
>>> print(10 + y)
<Commuter: 109>

>>> z = x + y                                           # doesn't recur to __radd__
>>> print z
<Commuter: 187>
>>> print(z + 10)
<Commuter: 197>
>>> print(z + z)
<Commuter: 374>


##In-Place Addition: To implement += in-place addition, you can use either __add__ or __iadd__. If both
##are present, __iadd__ is preferred over += in-place addition. But __iadd__ allows for more efficient
##in-place change.

class Number:
        def __init__(self, val):
                self.val = val
        def __iadd__(self, other):                      # __iadd__ explicit: x += y
                self.val += other
                return self                             # usually returns self

>>> x = Number(5)
>>> x
<__main__.Number instance at 0x0000000002FE7488>
>>> x += 1
>>> x += 1
>>> x.val                                               # in-place update
7

##Here's an example where in-place falls back on __add__ and returns an instance with in-place change.

class Number:
        def __init__(self, val):
                self.val = val
        def __add__(self, other):
                return Number(self.val + other)         # propagates class type. 

>>> x = Number(5)
>>> x += 1
>>> x += 1
>>> x.val
7

##Now if the return type is not am instance, and if an in-place addition is used, x becomes an 'int' value.
##Example:
        
def __add__(self, other):
		print 'add: {0}, {1}'.format(self.val, other)
		return(self.val + other)                
>>> x += 7
add: 6, 7
>>> x
13
>>> type(x)
<type 'int'>

##So, in this case if in-place addition, always return an instance like above.

##Call Expressions: __call__

##Using a __call__ method applies function call expression to instances. An instance becomes a callable
##object. Without the __call__ method, you can't execute an instance like a function call.

>>> instanceObject(args)                                # if no __call__ method is defined
...error...

class Callee:
        def __call__(self, *pargs, **kargs):
                print('Called:', pargs, kargs)

>>> C = Callee()
>>> C(1, 2, 3)
('Called:', (1, 2, 3), {})

>>> C(1, 2, 3, x=4, y=5)
('Called:', (1, 2, 3), {'y': 5, 'x': 4})

##The formal argument passing methods are supported by the method:

class C:
        def __call__(self, a, b, c=5, d=6): ...         # Normals and defaults

class C:
        def __call__(self, *pargs, **kargs): ...        # Collect Arbitrary arguments

>>> C(1, 2)                                             
('Called:', (1, 2), {})
>>> C(1, 2, 3, 4)
('Called:', (1, 2, 3, 4), {})
>>> C(a=1, b=2, d=4)
('Called:', (), {'a': 1, 'b': 2, 'd': 4})
>>> C(*[1, 2], c=3, d=4)
('Called:', (1, 2), {'c': 3, 'd': 4})
>>> C(1, *(2,), c=3, d=4)
('Called:', (1, 2), {'c': 3, 'd': 4})
>>> C(1, (2,), c=3, d=4)
('Called:', (1, (2,)), {'c': 3, 'd': 4})

##The good thing about call expressions with class instances to emulate functions is that they retain
##state information between calls, which is useful:

class Prod:
        def __init__(self, value):
                self.value = value
        def __call__(self, other):                      # can also use a normal method like 
                return self.value * other               # def comp(self, other):
                                                        #         return self.value * other, since there's only 1 argument.
>>> x = Prod(2)
>>> x(3)                                                # Remembers '2' in state. returns 2 * 3
6
>>> x(4)                                                # Remembers '2' in state. returns 2 * 4                                
8



##Function Interfaces and Callback base code.

##This is used to tie information to callback function; also used to retain state information. This can be
##done by using a class that defines an object that supports a function-call interface, which has state information.

##Example:

class Callback:
        def __init__(self, color):                      # Function + state information
                self.color = color
        def __call__(self):                             # Supports call with no argument
                print('turn', self.color)

>>> cb1 = Callback('blue')                              
>>> cb2 = Callback('green')                             # passing state information
>>> cb1()
('turn', 'blue')
>>> cb2()
('turn', 'green')                                       # during callback, it displays the information


##You can also lambda functions to store state information using default arguments:

>>> cb3 = (lambda color = 'red': 'turn ' + color)

>>> cb3()
'turn red'
>>> cb3('blue')
'turn blue'
>>> cb3()                                               # unlike instance callback, this cannot retain passed in information.
'turn red'


##Another method is to use the bound methods of a class. A bound method object is a kind of object that remembers the
##self instance and the referenced function. A bound method may therefore be called as a simple function without an
##instance later:

class Callback:
        def __init__(self, color):
                self.color = color
        def changeColor(self):
                print('turn', self.color)

>>> object = Callback('blue')
>>> cb = object.changeColor                             # Registered event handler
>>> cb()                                                # On event prints 'blue'



##Comparisons: __lt__(less than), __gt__(greater than), and others

##Classes can define methods to intercept all six comparison operators: <, >, <=, >=, == and !=. There are no RHS and
##LHS variants of these methods. The methods __gt__ and __lt__ are used when only one operand supports comparison.

##There are no implicit relationships among the comparison operators. The truth of == does not imply that != is false,
##for example, so both __eq__ and __ne__ should be defined to ensure that both operators behave correctly.

##The __cmp__ method is used by all comparisons if no more specific comparison methods are defined; it returns a number
##that is less than, equal to, or greater than zero, to signal less than, equal, and greater than results for the
##comparison of its two arguments (self and another operand). This method often uses the cmp(x, y) built-in to compute
##its result.

class C:
        data = 'spam'
        def __gt__(self, other):
                return self.data > other
        def __lt__(self, other):
                return self.data < other

>>> X = C()
>>> X > 'ham'                                           # Runs __gt__
True
>>> X < 'ham'                                           # Runs __lt__
False

##Using the __cmp__ Method:

##This method is used as a fallback, when the specific methods as shown above are not defined. Its integer result is used
##to evaluate the operator being run.

class C:
        data = 'spam'
        def __cmp__(self, other):
                return cmp(self.data, other)

>>> X = C()
>>> X > 'ham'
True
>>> X < 'ham'
False


class C:
        data = 'spam'
        def __cmp__(self, other):
                return (self.data > other) - (self.data < other)

>>> X = C()
>>> X > 'ham'
True
>>> X < 'ham'
False


##Boolean Tests: __nonzero__ and __len__   (In py2.6, you should use __nonzero__ instead of __bool__)

##In py2.6, if a __bool__ returns False, it is ignored and the object is always considered true. So use __nonzero__.

##These methods help to define the boolean nature of their instances. Python first tries __nonzero__ to obtain a direct
##Boolean value and then, if that's missing, falls back to __len__ to determine a truth value from the object's length.

class Truth:
        def __nonzero__(self):
                print 'in nonzero'
                return True

>>> X = Truth()
>>> bool(X)
in nonzero
True

# Similarly,
class Truth:
        def __nonzero__(self):
                print 'in nonzero'
                return 0
>>> X = Truth()
>>> bool(X)
in nonzero
False

# Using __len__
class Truth:
        def __nonzero__(self):
                print 'in nonzero'
                return True
        def __len__(self):
                print 'in len'
                return True

>>> X = Truth()
>>> bool(X)                                     # Tries __nonzero__ first
in nonzero
True



##Object Destruction (destructor) : __del__

##It's the counterpart of __init__ constructor, and runs at garbage collection time. But in python, generally, destructors
##are normally not used since python reclaims automatically. Also, you cannot always predict when an instance will be
##reclaimed, which is done better explicitly using try/finally statement. Please see pg.733 for more subtle details.

class Life:
        def __init__(self, name='unknown'):
                print('Hello', name)
                self.name = name
        def __del__(self):
                print('GoodBye', self.name)

>>> brian = Life('Brian')
('Hello', 'Brian')

>>> brian = 'Rosetta'                                   # Instance destroyed
('GoodBye', 'Brian')



## ----------------------
## DESIGNING WITH CLASSES
## ----------------------

##Python's OOP can be summarized by three ideas:

##Inheritance: Inheritance is based on attribute lookup in Python (in X.name expressions)

##Polymorphism: In X.method, the meaning of method depends of the type (class) of X.

##Encapsulation: Methods and operators implement behaviour; data hiding is a convention by default. That is, hiding
##implementation details behind an object's interface.


##Overloading by Call Signatures (or Not)

##Polymorphism can also be implemented by using overloading functions with distinct type signatures. Since there are
##no type declarations in python, functions can be overloaded with distinct interfaces:

class C:
        def meth(self, x):
                pass
        def meth(self, x, y, z):
                pass

##Even though the argument passed in could be tested for type, it is more desirable to design a code to expect an object
##interface, not a specific data type; to be suitable for a broader range of types and applications.

class C:
        def meth(self, *args):
                if len(args) == 1:
                        pass
                elif type(args[0]) == int:
                        pass

class C:                                                # Better, built for object interface. Assuming x does the right thing
        def meth(self, x):
                x.operation()

##Although, it is better to use distinct method names for distinct operations, rather than relying on overloading or call
##signatures.


##OOP and Inheritance: 'Is-a' Relationships

##Inheritance is kicked off by attribute qualifications, which triggers search up the inheritance tree. From a OOP design
##point of view, inheritance is a way to specify set membership: a class defines a set of properties that may be
##inherited and customized by more specific sets, i.e., subclasses.

##Example:

class Employee:
        def __init__(self, name, salary=0):
                self.name = name
                self.salary = salary
        def giveRaise(self, percent):
                self.salary = int(self.salary + (self.salary * percent))
        def work(self):
                print '{0} does stuff'.format(self.name)
        def __repr__(self):
                return '<Employee: name={0}, salary={1}>'.format(self.name, self.salary)

class Chef(Employee):
        def __init__(self, name):
                Employee.__init__(self, name, 50000)
        def work(self):
                print '{0} makes food'.format(self.name)

class Server(Employee):
        def __init__(self, name):
                Employee.__init__(self, name, 40000)
        def work(self):
                print '{0} interfaces with customer'.format(self.name)

class PizzaRobot(Chef):
        def __init__(self, name):
                Chef.__init__(self, name)
        def work(self):
                print '{0} makes pizza'.format(self.name)

if __name__ == '__main__':
        bob = PizzaRobot('bob')
        print(bob)
        bob.work()
        bob.giveRaise(0.20)
        print(bob); print('\n'),

        for klass in (Employee, Chef, Server, PizzaRobot):
                obj = klass(klass.__name__)                     # passes the class name as the name argument for __init__
                obj.work() 
        
# Output
<Employee: name=bob, salary=50000>
bob makes pizza
<Employee: name=bob, salary=60000>

Employee does stuff
Chef makes food
Server interfaces with customer
PizzaRobot makes pizza


##OOP and Composition: 'Has-a' Relationships

##Composition involves embedding other objects in a container object, and activating the mto implement container
##methods. With an OOP design, composition is another way to represent relationships in a problem domain. Rather than
##set membership as shown in the previous example, composition has to do with components - parts of the whole.

##Composition reflects relationships between parts, called 'has-a' relationships, also known as aggregation.

##Now, in order to understand this concept, we'll expand on our previous example:

class Employee:
        def __init__(self, name, salary=0):
                self.name = name
                self.salary = salary
        def giveRaise(self, percent):
                self.salary = int(self.salary + (self.salary * percent))
        def work(self):
                print '{0} does stuff'.format(self.name)
        def __repr__(self):
                return '<Employee: name={0}, salary={1}>'.format(self.name, self.salary)

class Chef(Employee):
        def __init__(self, name):
                Employee.__init__(self, name, 50000)
        def work(self):
                print '{0} makes food'.format(self.name)

class Server(Employee):
        def __init__(self, name):
                Employee.__init__(self, name, 40000)
        def work(self):
                print '{0} interfaces with customer'.format(self.name)

class PizzaRobot(Chef):
        def __init__(self, name):
                Chef.__init__(self, name)
        def work(self):
                print '{0} makes pizza'.format(self.name)

class Customer:                                                                 # Expanding here by adding a customer class
        def __init__(self, name):
                self.name = name
        def order(self, server):
                print '{0} order from {1}'.format(self.name, server)
        def pay(self, server):
                print '{0} pays for item to {1}'.format(self.name, server)

class Oven:
        def bake(self):
                print('oven bakes')

class PizzaShop:
        def __init__(self):
                self.server = Server('Pat')
                self.chef = PizzaRobot('Bob')
                self.oven = Oven()

        def order(self, name):
                customer = Customer(name)
                customer.order(self.server)
                self.chef.work()
                self.oven.bake()
                customer.pay(self.server)


if __name__ == '__main__':
        scene = PizzaShop()
        scene.order('Homer')
        print('...')
        scene.order('Shaggy')


##Here, the PizzaShop is the container, its constructor makes and embeds instances of the employee classes as well
##as an Oven class. When the self-test is run, the PizzaShop order method is called, and the embedded objects are
##asked to carry out their actions. A new customer object is made on each order, and the embedded Server object is
##passed on to the order method. Customers come and go, but the Server object is part of PizzaShop composite.

##The PizzaShop handles two orders here: one from 'Homer' and another is 'Shaggy'.

##Output:

Homer order from <Employee: name=Pat, salary=40000>
Bob makes pizza
oven bakes
Homer pays for item to <Employee: name=Pat, salary=40000>
...
Shaggy order from <Employee: name=Pat, salary=40000>
Bob makes pizza
oven bakes
Shaggy pays for item to <Employee: name=Pat, salary=40000>


##Stream Processors Revisited

def processor(reader, converter, writer):                               # data processing function
        while 1:
                data = reader.read()
                if not data:
                        break
                data = converter(data)
                writer.write(data)

# Instead of using a function, we can use a class definition with a container with embedded objects to process methods 

# streams.py

class Processor:
        def __init__(self, reader, writer):
                self.reader = reader
                self.writer = writer
        def process(self):
                while 1:
                        data = self.reader.readline()
                        if not data:
                                break
                        data = self.converter(data)
                        self.writer.write(data)
        def converter(self, data):
                assert False, 'converter must be defined'               # Or raise exception


##Here's an example where the Processor class has a method process, which is a container. This way, reader and
##writer objects are embedded within the class instance (composition), and we supply the conversion logic in a
##subclass rather than passing in a converter function (inheritance).

##Also, the converter method defined here is incomplete, and will be filled by a subclass. So it's an example
##of an abstract superclass.

from streams import Processor

class Uppercase(Processor):
        def converter(self, data):
                return data.upper()

if __name__ == '__main__':
        import sys
        obj = Uppercase(open('spam.txt'), sys.stdout)                   # These arguments are passed for reader, writer
        obj.process()
        
##Here, the class Uppercase inherits the Processor and only defines what's unique about it - for data conversion
##to uppercase. When this file is run, it makes and runs an instance that reads from the file spam.txt and writes
##the uppercase equivalent of that file to the stdout stream.

# Output                                                # After reading the file with the content 'spam'              

SPAM

##The self-test code which runs can also be modified to write to files on disk, or print
##text inside HTML tags:

import sys
obj = Uppercase(open('spam.txt'), open('spamDump.txt', 'w'))    # Write to disk
obj.process()

class HTMLize:
        def write(self, line):
                print '<PRE>{0}</PRE>'.format(line.rstrip())    # print with HTML tags
<PRE>SPAM</PRE>
<PRE>SPAM</PRE>
<PRE>SPAM!</PRE>

##If you trace through this example’s control flow, you’ll see that we get both uppercase
##conversion (by inheritance) and HTML formatting (by composition), even though the
##core processing logic in the original Processor superclass knows nothing about either
##step. The processing code only cares that writers have a write method and that a method
##named convert is defined; it doesn’t care what those methods do when they are called.
##Such polymorphism and encapsulation of logic is behind much of the power of classes.


##Classes and Persistence: Data storage that contains both data and logic

##Using shelves and pickle to store instances:

import pickle                           # Writing an object with pickle
object = someClass()
file = open('filename', 'wb')
pickle.dump(object, file)               # saving object to a file

import pickle
file = open('filename', 'rb')           # open the file for reading
object = pickle.load(file)              # load the object from a file to in-memory object

import shelve                           # using shelve, uses access by key
object = someClass()
dbase = shelve.open('filename')
dbase['key'] = object                   # saving object by key

import shelve
dbase = shelve.open('filename')
object = dbase['key']                   # fetch the object by key

##We can store the PizzaShop() instance using pickle to store database of employees and shops,
##making them persistent across Python executions.

from pizzashop import PizzaShop

import pickle                           # Pickling an instance
file = open('filenameP', 'wb')          # Unlike shelve, you have to standard open a file
objectShop = PizzaShop()                # Create Instance
print '{0}, {1}'.format(objectShop.server, objectShop.chef)
pickle.dump(objectShop, file)           # pickle the instance to a file

# Output
<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>

import pickle                           # Unpickling an object from a file
file = open('filenameP', 'rb')          # Open a file on disk and get reference
obj = pickle.load(file)                 # Unpickle a file and load it as in-memory object
print '{0}, {1}'.format(obj.server, obj.chef)   # printing the stored attributes
obj.order('Sue')

# Output
<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>
Sue order from <Employee: name=Pat, salary=40000>
Bob makes pizza
oven bakes
Sue pays for item to <Employee: name=Pat, salary=40000>


##OOP and delegation: 'Wrapper' Objects

# trace.py
class wrapper:
        def __init__(self, object):                                     # this allows to wrap an input argument based on its object type
                self.wrapped = object                                   # save object
        def __getattr__(self, attrname):
                print 'Trace: {0}'.format(attrname)                     # trace fetch
                return getattr(self.wrapped, attrname)                  # delegate fetch

##Here, the getattr(X, N) is like X.N, except N is an expression that evaluates to a string at runtime, not a variable.
##In fact, getattr(X, N) is similar to X.__dict__[N], but the former also performs inheritance search, while the latter
##does not.

>>> from trace import wrapper

>>> x = wrapper([1, 2, 3])                                              # wrap a list                                        

>>> x                                                                   
Trace: __repr__
[1, 2, 3]
>>> type(x)
<type 'instance'>

>>> x.append(4)                                                         # delegate to list method
Trace: append

>>> dir(x)
Trace: __members__
Trace: __methods__
['__doc__', '__getattr__', '__init__', '__module__', 'wrapped']

>>> x.wrapped                                                           # echo an attribute
[1, 2, 3, 4]

##In py2.6, operator overloading methods run by built-in operations are routed through generic attribute interception
##methods like __getattr__. Printing a wrapped object directly for example, calls this method for __repr__ or __str__,
##which passes the call on to the wrapped object.

>>> x = wrapper({'a':1, 'b':2})                                         # wrap a dictionary

>>> x
Trace: __repr__
{'a': 1, 'b': 2}

>>> x.keys()                                                            # delegate to dictionary method
Trace: keys
['a', 'b']

##The net effect here is to augment the entire interface of the wrapped object, with additional code in the wrapper class.
##Thus, using an object as the input argument along with delegation can also be used to extend built-in types.

##Pseudoprivate class attributes

##A name with double underscores is automatically expanded to include its class name. A name like __X
##is changed to _className__X automatically. This name is somewhat unique and causes less name clashes.

##One of the main problems that the pseudoprivate attribute feature is meant to alleviate has to do with
##the way instance attributes are stored. In Python, all instance attributes wind up in the single
##instance object at the bottom of the class tree.

##If the name of an attribute is equal in two distinct classes, it is okay as long as they are not
##inherited together by a subclass. Otherwise, we might need to use the pseudoprivate prefix.

class C1:
        def meth1(self):
                self.X = 88                     # self.X
        def meth2(self):
                print(self.X)

class C2:
        def metha(self):                        
                self.X = 99                     # self.X
        def methb(self):
                print(self.X)
                
>>> class C3(C1, C2):
	pass

>>> I = C3()
>>> I
<__main__.C3 instance at 0x0000000002E20808>
>>> I.meth1(); I.metha()                        # metha() executed later, will define the value of X
>>> I.X
99
>>> I.metha(); I.meth1()                        # meth1() executed later, will define the value of X
>>> I.X
88

##When the name X is prefixed in the methods, it allows us to access both of their values.

>>> I = C3()
>>> I.__dict__
{}
>>> I.meth1();I.metha()
>>> I.__dict__                                  # echoing and printing the namespace
{'_C2__X': 99, '_C1__X': 88}

>>> I._C2__X                                    # accessing by attribute key
99

##Pseudoprivate names can also be applied to methods as well:

class Super:
        def method(self): pass                  # A real application method

class Tool:
        def __method(self): pass                # Becomes _Tool__method()
        def other(self): self.__method()        # Use internal method

class Sub1(Tool, Super):
        def actions(self): self.method()        # Runs Super.method() as expected

class Sub2(Tool):
        def __init__(self): self.method= 99     # Doesn't break Tool.__method()
        
        

##Creating Methods as objects: Bound or Unbound

##Example:
        
class Spam:
        def doit(self, message):
                print(message)

##Usually, we'd create an instance an instance of the class and use qualification
##with an attribute, in this case, a method. The method is called.
                
>>> object1 = Spam()
>>> object1.doit('hello world')
hello world
>>> object1
<__main__.Spam instance at 0x0000000002D40808>

##For a bound method, we access a function attribute of a class by qualifying an instance,
##which is turn returns a bound method object. To call the bound method, pass the required
##argument(s).

>>> object1 = Spam()
>>> boundT = object1.doit                       # instance + method
>>> boundT('hello world')
hello world
>>> boundT
<bound method Spam.doit of <__main__.Spam instance at 0x0000000002D40808>>

##To return an unbound object, we qualify the class name with the function attribute. Then,
##to call the method, you must provide an instance object explicitly as the first argument.

>>> object1 = Spam()
>>> unboundT = Spam.doit                        # class + method
>>> unboundT(object1, 'hello world')
hello world
>>> unboundT
<unbound method Spam.doit>

##Another pitfall to watch out for when defining class methods:
        
class Selfless:
	def __init__(self, data):
		self.data = data
	def selfless(arg1, arg2):               # Among the input arguments, self should be 
		return arg1 + arg2              # included as first
	def normal(self, arg1, arg2):
		return self.data + arg1 + arg2

>>> X = Selfless(2)
>>> Selfless.selfless(3, 4)                     # error
unbound method selfless() must be called with Selfless instance as first argument (got int instance instead)

>>> X.selfless(3, 4)                            # error
TypeError: selfless() takes exactly 2 arguments (3 given)

>>> X.selfless(3)                               # error
TypeError: unsupported operand type(s) for +: 'instance' and 'int'

##In all of these calls, the first input argument is taken as the instance, since self was not described
##in the definition


##Bound methods and other callable objects

##Since bound methods can be processed as generic objects, they can be passed around a program arbitrarily. They combine
##instance and a function in a single package, and is callable.

class Number:
        def __init__(self, base):
                self.base = base
        def double(self):
                return self.base * 2
        def triple(self):
                return self.base * 3

>>> x = Number(2)                                       # Class instance objects
>>> y = Number(3)                                       # State + methods
>>> z = Number(4)
>>> x.double()                                          # Normal immediate calls
4
>>> acts = [x.double, y.double, y.triple, z.double]     # List of bound method calls
>>> for act in acts:                                    # Calls are deferred
	print act()                                     # Call as through functions

4
6
9
8

##Like simple functions, they have introspection information of their own, including attributes that give access to the
##instance object and method function they pair.

>>> bound = x.double
>>> bound.__self__                                      # Included Instance
<__main__.Number instance at 0x0000000002D63808>
>>> bound.__func__                                      # Included method
<function double at 0x0000000002D682E8>
>>> bound.__self__.base                                 # Accessing included instance attribute
2
>>> bound()                                             # calling the metod
4

##Therefore, bound methods are one of the callable types in python. Next example demonstrates, simple functions coded
##with a def or lambda, instances that inherit a __call__, and a bound instance can be treated and called the same.

def square(arg):
        return arg ** 2                                 # Simple function

class Sum:
        def __init__(self, val):
                self.val = val
        def __call__(self, arg):                        # __call__ method
                return self.val + arg

class Product:
        def __init__(self, val):
                self.val = val
        def method(self, arg):                          # bound method
                return self.val * arg

>>> sobject = Sum(2)
>>> pobject = Product(3)
>>> actions = [square, sobject, pobject.method]         # Function, instance, bound method

>>> for act in actions:                                 # all three called the same way
	print act(5)

25
7
15

>>> actions[-1](5)                                      # Index, comprehensions, maps
15
>>> [act(5) for act in actions]
[25, 7, 15]
>>> map((lambda x: x(5)), actions)
[25, 7, 15]


##Classes are callable objects too, but they are generally used to create instance objects.

class Negate:
        def __init__(self, val):
                self.val = -val
        def __repr__(self):                             # print intercept
                return str(self.val)

>>> actions = [square, sobject, pobject.method, Negate] # call a class too
>>> for act in actions:
	print act(5)

25
7
15
-5

>>> [act(5) for act in actions]                         # runs __repr__ not __str__
[25, 7, 15, -5]            

##One of the places where bound methods and callbacks is in Tkinter GUI interface code that registers methods as event
##callback handlers:

class MyWidget:
        def handler(self):
                ...use self.attr for state...
        def makewidgets(self):
                b = Button(text='spam', command=self.handler)

##Here, the bound method self.handler remembers both self and MyGui.handler



##Multiple Inheritance: 'Mix-in' Classes

class Spam:
        def __init__(self):                             # no __repr__ or __str__
                self.data1 = 'food'

>>> X = Spam()
>>> print(X)
<__main__.Spam instance at 0x0000000002D53208>

##Here we can provide a __str__ or __repr__ method to implement a custom string representation. But rather than coding
##these in each class, we'll create a general purpose class and inherit it all the classes.

##Listing instance attributes with __dict__

##Here's a generic tool class which overloads the __str__ method for all classes that include it in their header lines.

# lister.py

class ListInstance:
        """
        Mix-in class that provides a formatted print() or str() of instances via inheritance of __str__, coded here;
        displays instance attrs only; self is the instance of the lowest class; uses __X names to avoid clashing with
        client's attrs
        """

        def __str__(self):
                return '<Instance of {0}, address {1}:\n{2}>'.format(self.__class__.__name__, id(self), self.__attrnames())
        def __attrnames(self):
                result = ''
                for attr in sorted(self.__dict__):                              # Traverse the keys
                        result += '\tname {0}={1}\n'.format(attr, self.__dict__[attr])
                return result
        
##Here's what's going on in this class. This class is ultimately derived for printing utility:
        
##        * Each instance's class name can be printed using __class__.__name__
##        
##        * It scans the instance's attribute dictionary and prints accordingly.
##        
##        * It displays the instance's memory address by calling the id(), which returns any object's address.
##        
##        * It uses a pseudoprivate name for the method __attrnames.
##        
##        * Has an __str__ overloading method. Instances derived from this class display their attributes
##        automatically when printed.
        
>>> from lister import ListInstance
>>> class Spam(ListInstance):                                   # Inherit the ListInstance
	def __init__(self):
		self.data1 = 'food'

		
>>> x = Spam()
>>> x                                                           # The __repr__ is still a default
<__main__.Spam instance at 0x0000000002D530C8>
>>> print(x)                                                    # print() and str() run __str__
<Instance of Spam, address 47526088:
	name data1=food
>
>>> str(x)
'<Instance of Spam, address 47526088:\n\tname data1=food\n>'

##This ListInstance can mixed with other superclasses in a class header, known as multiple inheritance. That way we
##can get __str__ for free, while inheriting from existing superclasses.

>>> from lister import *

class Super:
        def __init__(self):
                self.data1 = 'spam'
        def ham(self):
                pass

class Sub(Super, ListInstance):
        def __init__(self):
                Super.__init__(self)
                self.data2 = 'eggs'
                self.data3 = 42
        def spam(self):
                pass

if __name__ == '__main__':
        X = Sub()
        print(X)

# Output:
<Instance of Sub, address 47503112:
	name data1=spam
	name data2=eggs
	name data3=42
>

##Here, the Sub class inherits from Super and ListInheritance. When we make an instance of Sub and print, we automatically
##get the custom print representation.

##The next example also shows that the ListInstance works in any class, since self refers to an instance of subclass that
##pulls this class in:

>>> import lister
>>> class C(ListInstance): pass                         # list as a superclass

>>> I = C()                                             # create instance
>>> I.a = 1; I.b = 2; I.c = 3                           # add instance attributes
>>> print(I)                                            # print with __str__
<Instance of C, address 47951688:
	name a=1
	name b=2
	name c=3
>
 

##List inherited attributes with dir

##To print both namespace and inherited attributes.

# lister.py

class ListInherited:
        """
        Use dir() to collect both instance attrs and names inherited from its classes; getattr() fetches inherited
        names not in self.__dict__; use __str__ not __repr__, or else tis loops when printing bound methods!
        """
        def __str__(self):
                return '<Instance of {0}, address {1}:\n{2}>'.format(self.__class__.__name__, id(self), self.__attrnames())
        def __attrnames(self):
                result = ''
                for attr in dir(self):                                          # Instance dir()
                        if attr[:2] == '__' and attr[-2:] == '__':
                                result += '\tname {0}=<>\n'.format(attr)
                        else:
                                result += '\tname {0}={1}\n'.format(attr, getattr(self, attr))
                return result

>>> class Sub(Super, ListInherited): pass

>>> I = Sub()
>>> print(I)
<Instance of Sub, address 47485832:
	name _ListInherited__attrnames=<bound method Sub.__attrnames of <__main__.Sub instance at 0x0000000002D49388>>
	name __doc__=<>
	name __init__=<>
	name __module__=<>
	name __str__=<>
	name data1=spam
	name ham=<bound method Sub.ham of <__main__.Sub instance at 0x0000000002D49388>>
>

##The ham is a method inside the class Super. When an instance is created, that method becomes a bound method as (Sub.ham)
##instance, since the method 'ham' is called by qualifying with the instance. Lets take another example.

>>> I = Super()                                                         # create an instance of Super                                                      
>>> I
<__main__.Super instance at 0x0000000002D493C8>
>>> dir(I)
['__doc__', '__init__', '__module__', 'data1', 'ham']                   # list the namespace and inherited attributes
>>> getattr(I, 'ham')                                                   # getattr returns the value
<bound method Super.ham of <__main__.Super instance at 0x0000000002D493C8>>


##One caution here—now that we’re displaying inherited methods too, we have to use __str__ instead of __repr__ to overload
##printing. With __repr__, this code will loop— displaying the value of a method triggers the __repr__ of the method’s
##class, in order to display the class. That is, if the lister’s __repr__ tries to display a method, displaying the method’s
##class will trigger the lister’s __repr__ again. Subtle, but true!



##Listing attributes per object in class trees

##In the last example of the ListInherited, it still doesn't tell us which class an inherited name comes from. 
##Here, we display the attributes grouped by the classes they live in - it sketches the full class tree, displaying
##attributes attached to each object along the way. It does this by traversing the inheritance tree from an instance's
##__class__ to its class, and then from the class's __bases__ to all superclasses recursively.


class ListTree:
        """
        Mix-in that returns an __str__ trace of the entire class tree an all its objects' attrs at and above self;
        run by print(), str() returns constructed string; uses __X attr names to avoid impacting clients; uses
        generator expr to recurse to superclasses; uses str.format() to make substitutions clearer
        """

        def __str__(self):                              # print() overloading
                self.__visited = {}
                return '<Instance of {0}, address {1}:\n{2}{3}>'.format(self.__class__.__name__,
                                                                        id(self),
                                                                        self.__attrnames(self, 0),
                                                                        self.__listclass(self.__class__, 4))

        def __listclass(self, aClass, indent):          # 
                dots = '.' * indent
                if aClass in self.__visited:
                        #return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(dots,            # This return content is not used anyway
                                                                                      #aClass.__name__,
                                                                                      #id(aClass))
                        return 
                else:
                        self.__visited[aClass] = True
                        genabove = (self.__listclass(c, indent + 4) for c in aClass.__bases__)
                        return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(dots,
                                                                                    aClass.__name__,
                                                                                    id(aClass),
                                                                                    self.__attrnames(aClass, indent),
                                                                                    ''.join(genabove),
                                                                                    dots)

        def __attrnames(self, obj, indent):
                spaces = ' ' * (indent + 4)
                result = ''
                for attr in sorted(obj.__dict__):
                        if attr.startswith('__') and attr.endswith('__'):
                                result += spaces + '{0} = <>\n'.format(attr)
                        else:
                                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
                return result
        


        
>>> class Sub(Super, ListTree): pass

>>> I = Sub()
>>> print(I)
<Instance of Sub, address 47485832:
    _ListTree__visited={}
    data1=spam

....<Class Sub, address 48174272:
        __doc__ = <>
        __module__ = <>

........<Class Super, address 48174536:
            __doc__ = <>
            __init__ = <>
            __module__ = <>
            ham=<unbound method Super.ham>
........>

........<Class ListTree, address 48175064:
            _ListTree__attrnames=<unbound method ListTree.__attrnames>
            _ListTree__listclass=<unbound method ListTree.__listclass>
            __doc__ = <>
            __module__ = <>
            __str__ = <>
........>
....>
>      

##Here's how it's working. When the the print is called, it is intercepted by the __str__. Then, it returns the print format
##with the name of the instance, address in one line with the included format. Within the same print format a newline character
##is returned and then the _ListTree__attrnames is called with the input argument instance name and 0(no indent). In there,
##it finds two attributes as dictionary entires. So it returns and prints their name accordingly with newlines.

##Next, still within the __str__, it calls the _ListTree__listclass method with the instance's __class__ and 4(indent) as input
##arguments. Then in _ListTree__listclass method, it tests if the input __class__ exists in _ListTree__visited. Since it doesn't,
##it goes to the else statement, where it creates a dictionary entry with the __class__ with the value True. Next, it creates
##a generator object with reference to an expression generator. There, the expression is recursive, where it runs for number of
##superclasses the input class has inherited from, known as __bases__. Then it goes to the return statement with print format
##method. In the print method, it prints the indent with dots. Then it prints the class __name__, its address in one line.
##In a newline, it calls the _ListTree__attrnames method which 

##When the print is intercepted, it is caught by __str__ first. Here's the rough order data of the execution stack for the
##this script:
##
##1) After the instance is created, the print is intercepted by __str__. There, it first empty dict the variable I.__visited.
##Then, it moves on to the next line in the __str__, where it continues with the string format method. There, it prints the
##class name, its address and then for printing the third output in the format(), it visits the __attrnames method.
##
##2) At the __attrnames, it takes in the instance and the indent value of 0. It sets the value of spaces
##for string formatting for print. So it only uses 4 white spaces. Then, it iterates through the instance attributes.
##Currently, there're only the __Listree_visited and the data1 attributes. So, it returns the constructed string 'result' with
##the attributes. Then, the control goes back to the __str__ method again, where the string format() gets the __attrnames values.
##
##3)Next, it goes for the __listclass method for getting its return format the string format(). The control passes over to the
##__listclass method where it is passed the __class__(Sub) and the indent value of 4. There it first checks if the __class__ exists
##in the __visited dict. Since it doesn't, it skips to the else clause where it first creates a dict entry in __visited with
##the __class__ for Sub. Next, it goes to the expression generator which assigns the expression reference to genabove.
##Then, it goes for the return statement where it executes the string format() method, and prints __class__.__name__, Sub and
##its address. Then for printing the __attrnames, the control passes over to __attrnames with the arguments __class__ and
##indent of 4. It begins to construct the result string with the class Sub attributes. This class has only the __doc__ and
##__module__ attributes. So it constructs the string with spaces and return tags to the result and returns. The control passes
##over to __listclass.
##
##4) There in __listclass, the control goes in the string method where it tries to execute the join() method, which recursively
##processes all the superclasses and goes thorugh the __listclass again and again, till it finds no more base classes.


##You'll also notice that the methods are unbound, since we fetch them from classes directly, instead of from instances.                                                                     



##Classes are objects: Generic Object Factories

##Since classes are objects, you can pass them to functions that generate arbitrary kinds of objects, called factories. Although
##trivial to implement, they can call any class with any number of constructor arguments in one step to generate any sort
##of instance.

def factory(aClass, *args):                             # Varargs tuple. With the class name and class input arguments
        return aClass(*args)                            # call aClass with arguments(option). returns this to an variable, which becomes an instance

class Spam:
        def doit(self, message):
                print(message)

class Person:
        def __init__(self, name, job):
                self.name = name
                self.job = job

>>> object1 = factory(Spam)                             # Make a Spam instance
>>> object2 = factory(Person, 'Guido', 'guru')          # Make a person instance
>>> object2
<__main__.Person instance at 0x0000000002D53108>
>>> object2.name
'Guido'
>>> object1.doit('Spam')                                # call a method
Spam

##The object generator function called factory can also be extended to include kwargs in its input argument as well.

def factory(aClass, *args, **kwargs):                   # +kwargs dict
        return aClass(*args, **kwargs)                  # Call aClass

##The factory generator can actually invoke any callable object, including functions and methods and not just a class.

##Once of the cases where a factory generator might be useful is where we have to create an instance where we're not
##aware of class constructor arguments. In that case, we might use default arguments.

##Factory-style functions or code like getattr() might also be used to fetch a class from a module so they won't have
##to be hardcoded. For example:

>>> import streamtypes                                  # Customizable code. oad a module
>>> aClass = getattr(streamtypes, className)            # fetch a class reference from a module
>>> reader = factory(aClass, classarg)                  # Or aClass(classarg). Create a reference



## ---------------------
## ADVANCED CLASS TOPICS
## ---------------------


##Extending Built-in Types


##Extending Types by embedding

##In this example, a class just wraps a Python list with extra set operations. But because it’s a class, it also
##supports multiple instances and customization by inheritance in subclasses.

class Set:
        def __init__(self, value = []):                         # Constructor
                self.data = []                                  # Manages a list
                self.concat(value)

        def intersect(self, other):                             # other is any input sequence
                res = []
                for x in self.data:     
                        if x in other:                          # pick common items
                                res.append(x)
                return Set(res)                                 # Return a new Set         

        def union(self, other):                                 # other is any sequence
                res = self.data[:]                              # Copy of my list
                for x in other:                                 # add items to res only if non-existent
                        if not x in res:
                                res.append(x)
                return Set(res)

        def concat(self, value):                                # value: list, Set
                for x in value:
                        if not x in self.data:                  # remove duplicates
                                self.data.append(x)
        def __len__(self):                                      # len(self)
                return len(self.data)

        def __getitem__(self, key):                             # self[i]
                return self.data[key]

        def __and__(self, other):                               # self & other
                return self.intersect(other)

        def __or__(self, other):                                # self | other
                return self.union(other)

        def __repr__(self):                                     # print()
                return 'Set: ' + repr(self.data))

if __name__ == '__main__':
        x = Set([1, 3, 5, 7])
        print(x.union(Set([1, 4, 7])))
        print(x | Set([1, 4, 6])))

# Output
Set: [1, 3, 5, 7, 4]
Set: [1, 3, 5, 7, 4, 6]


##Extending Types by Embedding

##All built-in types can be subclassed. Type-conversion functions such as list, str, dict and tuple have become built-in
##type names - although transparent to your script, a type conversion call (e.g., list('spam')) is now really an invocation
##of a type's object constructor.

##Now, you can subclass these built-in types to customize them. Instances of such a class can be used as that built-in type
##with custom extensions. Example:

# Map 1..N to 0..N-1; call back to built-in version.

class MyList(list):
        def __getitem__(self, offset):
                print '(indexing {0} at {1})'.format(self, offset)
                return list.__getitem__(self, offset - 1)

if __name__ == '__main__':
        print(list('abc'))
        x = MyList('ABC')
        print(x)

        print(x[1])
        print(x[3])

        x.append('spam'); print(x)
        x.reverse();      print(x)

# Output
['a', 'b', 'c']
['A', 'B', 'C']
(indexing ['A', 'B', 'C'] at 1)
A
(indexing ['A', 'B', 'C'] at 3)
C
['A', 'B', 'C', 'spam']
['spam', 'C', 'B', 'A']

##The following example customizes lists to add just methods and operators related to set processing. Because all
##other behaviour is inherited from built-in list superclass, this makes for a shorter and simpler name.

class Set(list):
        def __init__(self, value = []):
                list.__init__([])
                self.concat(value)

        def intersect(self, other):
                res = []
                for x in self:
                        if x in other:
                                res.append(x)
                return Set(res)

        def union(self, other):
                res = Set(self)                                         # copy the Set class reference with the list.
                res.concat(other)
                return res

        def concat(self, value):
                for x in value:
                        if not x in self:
                                self.append(x)

        def __and__(self, other):
                return self.intersect(other)

        def __or__(self, other):
                return self.union(other)

        def __repr__(self):
                return 'Set: ' + list.__repr__(self)                    # Set: + normal (self) list printed as an repr

if __name__ == '__main__':
        x = Set([1, 3, 5, 7])
        y = Set([2, 1, 4, 5, 6])
        print(x, y, len(x))
        print(x.intersect(y), y.union(x))
        print(x & y, x | y)
        x.reverse(); print(x)

# Output
(Set: [1, 3, 5, 7], Set: [2, 1, 4, 5, 6], 4)
(Set: [1, 5], Set: [2, 1, 4, 5, 6, 3, 7])
(Set: [1, 5], Set: [1, 3, 5, 7, 2, 4, 6])
Set: [7, 5, 3, 1]


##The 'New-Style' Class Model

##The only syntactic difference for new-style classes is that they are derived from either a built-in type, such as a
##list, or a special built-in class known as object. The object can be used as a superclass when no type is appropriate
##to use. Any class derived from object, or any other built-in type, is automatically treated as a new-style class.

class newStyle(object):
        pass

##New-Style Class Changes

##Classes and types merged
##Classes and types are synonyms. type(I) returns the class an instance is made from, and is same as I.__class__.__doc__ 


>>> class newStyle(object): pass                                # New Style class

>>> I = newStyle()
>>> type(I)                                                     # Type of instance is class it's made from
<class '__main__.newStyle'>
>>> I.__class__
<class '__main__.newStyle'>
>>> type(newStyle)                                              # Class is a type, and type is a class
<type 'type'>
>>> type([1, 2, 3])                                             # Built-in types work the same way
<type 'list'>
>>> type(list)
<type 'type'>
>>> list.__class__
<type 'type'>

>>> class Style: pass                                           # Classic old style class

>>> I = Style()
>>> type(I)                                                     # Instance is of type 'Instance', made from classes
<type 'instance'>
>>> I.__class__
<class __main__.Style at 0x00000000025340A0>
>>> type(Style)                                                 # Classes are not the same as types
<type 'classobj'>

##So each new style class is generated by a metaclass - a class that is normally either type itself, or a subclass
##of it customized to augment or manage generated classes.


##Implications for type testing

>>> class C: pass                                               # create two classic classes

>>> class D: pass

>>> c = C()                                                     # create their instances
>>> d = D()
>>> type(c) == type(d)                                          # their types match since they're of type 'instance'
True
>>> c.__class__ == d.__class__                                  # their classes will be distinct
False
>>> type(c), type(d)                                            # same instance type, no type derived from their classes
(<type 'instance'>, <type 'instance'>)
>>> c.__class__, d.__class__
(<class __main__.C at 0x0000000002D93CA8>, <class __main__.D at 0x0000000002D93D00>)


>>> class C(object): pass                                       # create two new style classes

>>> class D(object): pass

>>> c = C()                                                     # create their instances
>>> d = D()
>>> type(c) == type(d)                                          # their types mismatch since we're comparing the instances' classes
False
>>> type(c), type(d)                                            # their classes' returned as their types
(<class '__main__.C'>, <class '__main__.D'>)
>>> c.__class__, d.__class__                                    # their __class__ is same as their types
(<class '__main__.C'>, <class '__main__.D'>)


##All objects derive from 'object'

##Because all classes inherit from the class 'object' either implicitly or explicitly, and because all types are now
##classes, every object derives from the object built-in class, whether directly or through a superclass.

>>> class C(object): pass

>>> X = C()
>>> type(X)                                                     # type is now a class, which is a type
<class '__main__.C'>
>>> type(C)                                                     # class is a type. All classes are now a type
<type 'type'>
>>> isinstance(X, object)                                       # Both instance and class derive from object                       
True
>>> isinstance(C, object)
True

##Because built-in types are now classes, their instances derive from object too:

>>> type('spam')                                                # type derive from type 'str'
<type 'str'>
>>> type(str)                                                   # str is a type
<type 'type'>
1
>>> isinstance(str, object)
True
>>> isinstance('spam', object)
True

>>> type(type)                                                  # all types are types, as well as new style classes
<type 'type'>
>>> type(object)
<type 'type'>

>>> isinstance(type, object)                                    # All classes derive from object, even type
True
>>> isinstance(object, type)                                    # types make classes, and type is a class
True
>>> type is object
False


##Diamond pattern inheritance search order

##In this search pattern, Python first looks in any superclasses to the right of the first one searched before ascending
##all the way to the common superclass at the top. The search proceeds across by levels before moving up.

##Example of classic search:

>>> class A:
	attr = 1

	
>>> class B(A):                                 # B and C derive from A
	pass

>>> class C(A):
	attr = 2

	
>>> class D(B, C):                              # Tries A before C
	pass

>>> x = D()
>>> x.attr                                      # Searches x, D, B, A. Finds attr in A, quits searching C
1


>>> class A(object):                            # New-Style Class, derived from object
	attr = 1

	
>>> class B(A):                                 # B and C derived from A
	pass

>>> class C(A):
	attr = 2

	
>>> class D(B, C):                              # Tries C before A
	pass

>>> x = D()
>>> x.attr                                      # Searches x, D, B, C. Finds attr in C, quits searching for A next
2


##Explicit conflict resolution

##Forcing the selection of an attribute from anywhere in the tree by assigning or otherwise naming. This method works
##for classic and new style classes. Any top-level attribute can be picked in this method, names or methods.

>>> class A:                                    # Defining an old-style class
	attr = 1

	
>>> class B(A):
	pass

>>> class C(A):
	attr = 2

	
>>> class D(B, C):
	attr = C.attr                           # Explicitly specifying the class and attribute to derive from using qualification
	
>>> x = D()
>>> x.attr                                      # Returns the attr from class C instead of A
2


>>> class A:                                    # Using classic classes with explicit attribute assignment for methods
	def meth(s): print('A.meth')

	
>>> class C(A):
	def meth(s): print('C.meth')

	
>>> class B(A):
	pass

>>> class D(B, C): pass                         # Using classic search order

>>> x = D()
>>> x.meth()                    
A.meth                                          # returns method from A

>>> class D(B, C): meth = C.meth                # Pick C's method as per diamond search order

>>> x = D()
>>> x.meth()
C.meth                                          # returns method from C

>>> class D(B, C): meth = B.meth                # picks class B. B derives method 'meth' from A as per classic search

>>> x = D()
>>> x.meth()
A.meth                                          # returns A as specified
>>> class D(B, C):      
.	def meth(self):
		C.meth(self)                    # pick a method by calling explicitly 

		
>>> x = D()
>>> x.meth()
C.meth

##This assignment technique can be handy in multiple inheritance scenarios in general. For instance, if you want part of
##a superclass on the left and part of a superclass on the right, you might need to tell Python which same-named
##attributes to choose by using explicit assignments in subclasses.

##Also see the Super function for providing generic access to superclasses in single inheritance trees, super supports
##a cooperative mode for resolving some conflicts in multiple inheritance trees.


##Scope of search order change

##Just as important, the implied object superclass in the new-style model provides default methods for a variety of
##built-in operations, including the __str__ and __repr__ display format methods. Run a dir(object) to see which methods
##are provided. Without the new-style search order, in multiple inheritance cases the defaults in object would always
##override redefinitions in user-coded classes, unless they were always made in the leftmost superclass.


##New-Style Class Extensions

##Instance Slots

##This a special attribute at the top level of a new style class definition, created by assigning a sequence of string
##attribute names, known as __slots__ class attribute.

>>> class limiter(object):                                      # __slots__ in a new style class
	__slots__ = ['age', 'name', 'job']

>>> x = limiter()
>>> x.age                                                       # attribute has to assigned like any other named variable
AttributeError: age
>>> x.age = 40                                                  # create an attribute, named in __slot__
>>> x.age
40
>>> x.ape = 1000                                                # no ape attribute in __slots__
AttributeError: 'limiter' object has no attribute 'ape'

##This can avoid assignments to illegal attribute names. This can also conserve namespace dictionary space.


##Slots and generic code

##If __slots__ attribute is used, an instance may not have a __dict__ attribute, since the slots limit the attribute
##namespace. An instance in this case does not have an attribute dictionary, it uses class descriptors instead.
##Tools such as getattr, setattr and dir that access attributes by string name must be careful to use more storage-neutral
##tools than __dict__, which apply to attributes based on either __dict__ or __slots__.

>>> class C:                                            # __slots__ only work with new style classes
	__slots__ = ['a', 'b']
>>> X.__dict__                                          # still has a __dict__ attribute
{}


>>> class C(object):                                    # __slots__ with a new style class. No __dict__ by default
	__slots__ = ['a', 'b']

	
>>> X = C()                                                     
>>> X.a = 1
>>> X.a
1
>>> X.__dict__                                                  # no dictionary namespace here
AttributeError: 'C' object has no attribute '__dict__'

>>> getattr(X, 'a')                                             # getattr() and setattr() still work
1
>>> setattr(X, 'b', 2)
>>> X.b
2

>>> 'a' in dir(X)                               # dir() finds slot attributes too
True
>>> 'b' in dir(X)
True

        
>>> class D(object):                                            
	__slots__ = ['a', 'b']
	def __init__(self):                                     
		self.d = 4                      # cannot add new attributes since there's no __dict__
>>> X = D()
AttributeError: 'D' object has no attribute 'd'



>>> class D(object):
	__slots__ = ['a', 'b', '__dict__']      # Add __dict__ to the list for attribute name dictionary
	c = 3                                   # Class attrs work normally
	def __init__(self):
		self.d = 4                      # d in self.d is put in __dict__

		
>>> X = D()
>>> X.d
4
>>> X.__dict__                  # here this instance object has both __dict__ and __slots__
{'d': 4}
>>> X.c                         # access class attribute
3
>>> X.__dict__                  # access __dict__ in __slots__
{'d': 4}
>>> X.__slots__                 # getattr() for __slots__ too
['a', 'b', '__dict__']

>>> X.a
AttributeError: a
>>> X.a = 1                     # assign an attribute
>>> X.b = 5

>>> getattr(X, 'a'), getattr(X, 'c'), getattr(X, 'd')
(1, 3, 4)

>>> for attr in list(X.__dict__) + X.__slots__:                 # concatenating __dict__ and __slots__
	print '{0} => {1}'.format(attr, getattr(X, attr))       # using an iterator to traverse attributes

d => 4
a => 1
b => 5
__dict__ => {'d': 4}

##This iterator can be rewritten in case __dict__ or __slots__ doesn't exist:

>>> getattr(X, '__dict__', [])                          # __dict__ returns the attribute dictionary
{'d': 4}
>>> list(getattr(X, '__dict__', []))                    # return empty list [] if not found
['d']
>>> getattr(X, '__slots__', [])                         # __slots__ returns the assigned list
['a', 'b', '__dict__']

>>> for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
	print '{0} => {1}'.format(attr, getattr(X, attr))

d => 4
a => 1
b => 5
__dict__ => {'d': 4}



##Multiple __slots__ lists in superclasses

##If multiple classes in a class tree have their own __slots__, certain conditions develop:

##If a subclass inherits from a superclass without a __slots__, the __dict__ attribute of the superclass
##will always be accessible, making a __slots__ in the subclass meaningless.

##If a class defines the same slot name as a superclass, the version of the name defined by the superclass
##slot will be accessible only by fetching its descriptor directly from the superclass.

##Because the meaning of a __slots__ declaration in limited to the class in which it appears, subclasses
##will have a __dict__ unless they also define a __slots__.

>>> class E(object):
	__slots__ = ['c', 'd']                  # Superclass has __slots__

	
>>> class D(E):
	__slots__ = ['a', '__dict__']           # subclass of E has __slots__ too

	
>>> X = D()                                     # instance of D, also of type class D
>>> X.__slots__                                 # X inherits lowest __slots__
['a', '__dict__']
>>> D.__slots__                                 # __slots__ in D 
['a', '__dict__']

>>> E.__slots__                                 # __slots__ in class E. Merges with __slots__ in its subclass.
['c', 'd']

>>> dir(X)                                      # X inherits collectively from D and E.
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__',
 '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__slots__', '__str__', '__subclasshook__', 'a', 'c', 'd']

>>> X.a = 1; X.b = 2; X.c = 3                   
>>> X.a, X.c
(1, 3)

>>> X.__dict__                                  # X.b is written to dictionary namespace __dict__
{'b': 2}


>>> for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
	print '{0} => {1}'.format(attr, getattr(X, attr))

b => 2                                          # slots in superclass missed! But dir(X) includes it.
a => 1
__dict__ => {'b': 2}

##Slots are best treated as class attributes, rather than considering them as instance attributes.



##Class properties

##Property is a way of defining getattr, setattr, del and docs for an instance or a class attribute. With
##this, you can create normal defs inside a class definition for __getattr__, __setattr__, etc. This is
##for use inside new style classes.

##They're simply an alternative to __getattr__ and __setattr__ methods. Property are typically assigned at
##the top level of a class statement. Example:

>>> class classic:
	def __getattr__(self, name):
		if name == 'age':
			return 40
		else:
			raise AttributeError

		
>>> x = classic()
>>> x.age                                       # Runs __getattr__
40
>>> x.name                                      # Runs __getattr__. Only 'age' allowed as an attribute name
AttributeError

##Using property:
        
>>> class newProps(object):
	def getage(self):
		return 40
	age = property(getage, None, None, None)        # get, set, del, docs. 

	
>>> x = newProps()                                                                     
>>> x.age                                       # Runs getage. __getattr__ is routed to getage                                              
40
>>> x.name                                      # exception raise since no attribute found. Normal fetch.
AttributeError: 'newProps' object has no attribute 'name'


>>> class newProps(object):                     
	def getage(self):                       # for __getattr__. Notice managed attributes like 'age' don't need an argument here.
		return 40
	def setage(self, value):                        # for __setattr__
		print 'Set Age: {0}'.format(value)
		self._age = value
	age = property(getage, setage, None, None)      # property for 'age'

>>> x = newProps()
>>> x.age                               # Runs getage
40
>>> x._age                              # setage is not executed yet. Instance attribute _age not yet created.
AttributeError: 'newProps' object has no attribute '_age'

>>> x.age = 42                          # Runs setage
Set Age: 42
>>> x._age                              # Normal fetch; no getage call
42
>>> x.job = 'trainer'                   # Normal assign; not setage call
>>> x.job
'trainer'

##The equivalent classic class incurs extra method calls for assignments to attributes not being managed and needs to route
##attribute assignments through the attribute dictionary (or, for new-style classes, to the object superclass’s __setattr__)
##to avoid loops:
        
>>> class classic:
	def __getattr__(self, name):            # top-level attributes that are not managed by property need extra assignments
		if name == 'age':
			return 40               
		else:
			raise AttributeError
	def __setattr__(self, name, value):     # On all assignments
		print 'set: {0}{1}'.format(name, value)
		if name == 'age':
			self.__dict__['_age'] = value
		else:
			self.__dict__[name] = value

>>> x = classic()
>>> x.age                                       # calls __getattr__
40
>>> x.age = 42                                  # calls __setattr__
set: age42
>>> x._age                                      # normal fetch; not __getattr__ call
42
>>> x.job = 'trainer'                           # calls __setattr__
set: jobtrainer
>>> x.job                                       # normal fetch; no __getattr__ call
'trainer'


##For more details on property descriptions, see pg.793


##__getattribute__ and Descriptors

##The __getattribute__ method unlike __getattr__, is able to intercept all attribute references, not just undefined references. 
##Attribute descriptors are classes with special __get__ and __set__ methods, assigned to class attributes and inherited by
##instances. We'll see properties, __getattribute__ and descriptors more later.


##Metaclasses

##To be discussed later.....



##Static and Class Methods

##Two kinds of methods in a class can be called without an instance. These are static and class methods. These modes are special
##built-in functions called staticmethod and classmethod.


##Static Methods in py2.6

##Static methods have a slightly different implementation in py3.0. Check pg.796.

##In py2.6, fetching a method from a class produces an unbound method, which cannot be called without passing an instance. Hence,
##in order for a method to be called without an instance, we need to declare it as static.

##Suppose we create a class attribute to count the number of instances created from a class:

>>> class Spam(object):
        numInstances = 0                        # class attribute
        def __init__(self):
                Spam.numInstances += 1          # increment at each initialization
        def printNumInstances():                # cannot call methods without a self object through an instance or a class(qualification)
                print 'Number of instances created: '.format(Spam.numInstances)

>>> a = Spam()
>>> b = Spam()
>>> c = Spam()

>>> Spam.printNumInstances()                    # call fail when called through class (class.methodName)
TypeError: unbound method printNumInstances() must be called with Spam instance as
first argument (got nothing instead)

>>> c.printNumInstances()                       # call fail when called through instance (self.methodName)
TypeError: printNumInstances() takes no arguments (1 given)

##Static method alternative

##We can define such a self-less function to be called outside the class.

def printNumInstances():
                print 'Number of instances created: {0}'.format(Spam.numInstances)

class Spam(object):
        numInstances = 0
        def __init__(self):
                Spam.numInstances += 1

a = Spam()
b = Spam()
c = Spam()

>>> printNumInstances()
Number of instances created: 3


##But the problem with this approach is that we cannot customize this function by inheritance, since is outside the class's
##namespace and this function might be too far removed in a large module or program. 
        
##For using and defining the printNumInstances function inside the class, we can use this with an instance defined as a method:

>>> class Spam(object):
        numInstances = 0
        def __init__(self):
                Spam.numInstances += 1
        def printNumInstances(self):
                print 'Number of instances created: {0}'.format(Spam.numInstances)

>>> a, b, c = Spam(), Spam(), Spam()

>>> a.printNumInstances()
Number of instances created: 3

##Again, this method is unworkable since we have to create an instance to query the Number. Second, calling the instance
##changes the data itself.

##Using Static and Class methods

##To designate methods as static and class methods, classes built-in functions staticmethod and classmethod. Both mark
##a function object as special, they require no instance if static, and requiring a class argument if a class method.

class Methods:
        def imeth(self, x):                     # Normal instance method: passed a self
                print(self, x)

        def smeth(x):                           # Static: no instance passed
                print(x)

        def cmeth(cls, x):                      # Class: gets class, not instance
                print(cls, x)

        smeth = staticmethod(smeth)             # Make smeth a static method. Simply reassign method names.
        cmeth = classmethod(cmeth)              # Make cmeth a class method

>>> obj = Methods()                             # Make an instance

>>> obj.imeth(1)                                # Normal method, call through instance. With self in its argument.
(<__main__.Methods instance at 0x0000000002DABA88>, 1) # Becomes imeth(obj, 1)

>>> Methods.imeth               
<unbound method Methods.imeth>

>>> Methods.imeth(obj, 2)                       # Normal method, call through class
(<__main__.Methods instance at 0x0000000002DABA88>, 2)  # Instance passed explicitly

##Static methods called:
>>> Methods.smeth(3)                            # Static method, call through class
3                                               # No instance passed or expected
>>> obj.smeth(4)                                # Static method, call through instance
4                                               # Instance not passed
##Class methods called:
>>> Methods.cmeth(1)                            # Class method, call through class
(<class __main__.Methods at 0x0000000002D93D00>, 1)     # Becomes cmeth(Methods, 1)
>>> obj.cmeth(5)                                # Class method, call through instance
(<class __main__.Methods at 0x0000000002D93D00>, 5)     # Becomes cmeth(Methods, 5). Python automatically
                                                        # passes the Class, not the instance; whether
                                                        # its called through instance or class.

##Counting Instances with Static Methods

class Spam(object):
        numInstances = 0
        def __init__(self):
                Spam.numInstances += 1
        def printNumInstances():
                print 'Number of instances created: {0}'.format(Spam.numInstances)
        printNumInstances = staticmethod(printNumInstances)

>>> a, b, c = Spam(), Spam(), Spam()

>>> a.printNumInstances()
Number of instances created: 3
>>> Spam.printNumInstances()
Number of instances created: 3

##It is also possible to make inherited methods static. Instead of defining the method as an outside function,
##it can be created inside a class scope, and can be used for customization by extension:

class Spam(object):
        numInstances = 0
        def __init__(self):
                Spam.numInstances += 1
        def printNumInstances():                        
                print 'Number of instances created: {0}'.format(Spam.numInstances)
        printNumInstances = staticmethod(printNumInstances)

class Sub(Spam):
        def printNumInstances():                        # Override a static method 
                print 'Extra Stuff...'
                Spam.printNumInstances()                # Call the original method
        printNumInstances = staticmethod(printNumInstances)


>>> a, b = Sub(), Sub()
>>> a.printNumInstances()                               # Call from subclass instance
Extra Stuff...
Number of instances created: 2
>>> Sub.printNumInstances()                             # Call from subclass itself
Extra Stuff...
Number of instances created: 2
>>> Spam.printNumInstances()
Number of instances created: 2

>>> class Other(Spam): pass                             # A Subclass can also inherit static method without
                                                        # redefining it. Inherit verbatim.
>>> c = Other()
>>> c.printNumInstances()
Number of instances created: 3


##Counting Instances with Class Methods

>>> class Spam:
        numInstances = 0
        def __init__(self):
                Spam.numInstances += 1
        def printNumInstances(cls):
                print 'Number of instances created: {0}'.format(cls.numInstances)       # cls is Spam, since class is passed for a classmethod
        printNumInstances = classmethod(printNumInstances)

        
>>> a, b = Spam(), Spam()
>>> a.printNumInstances()
Number of instances created: 2                          # passes class to the first argument
>>> Spam.printNumInstances()
Number of instances created: 2                          # also passes class to the first argument

>>> class Sub(Spam):
	def printNumInstances(cls):                     # Override a class method
		print 'Extra Stuff...{0}'.format(cls)
		Spam.printNumInstances()                # Call back original
	printNumInstances = classmethod(printNumInstances)

	
>>> class Other(Spam): pass

>>> x, y = Sub(), Sub()

>>> x.printNumInstances()                               # Call from subclass instance
Extra Stuff...__main__.Sub
Number of instances created: 2
>>> Spam.printNumInstances()                            # Call using the superclass                           
Number of instances created: 2
>>> Sub.printNumInstances()                             # Call using subclass
Extra Stuff...__main__.Sub
Number of instances created: 2

>>> z = Other()                                         # Create another instance
>>> z.printNumInstances()                               # Call using the instance. The class name is passed. 
Number of instances created: 3


##Counting instances per class with class methods

##Since class methods always receive the lowest class in an instance's tree, therefore:
##
## * Static methods and explicit class names may be a better solution for processing data local to a class.
##
## * Class methods may be better suited to processing data that may differ for each class in a hierarchy.

class Spam:
	numInstances = 0                    # Per-class instance counters
	def count(cls):
		cls.numInstances += 1           # cls is the lowest class above instance
	def __init__(self):
		self.count()                    # Passes self.__class__ to the count
	count = classmethod(count)

class Sub(Spam):
	numInstances = 0
	def __init__(self):                     # Redefines __init__
		Spam.__init__(self)

class Other(Spam):                          # Inherits __init__
	numInstances = 0

>>> x = Spam()
>>> y1, y2 = Sub(), Sub()
>>> z1, z2, z3 = Other(), Other(), Other()

>>> x.numInstances
1
>>> y1.numInstances
2
>>> z1.numInstances
3
>>> Spam.numInstances, Sub.numInstances, Other.numInstances
(1, 2, 3)



##Decorators and Metaclasses: Part1

##For a brief intro, see pg.804

##Function Decorator Basics

##It is a runtime declaration for the function coded before the def statement. It consists of @ symbol, followed
##by a 'metafunction', a function that manages another function.

class C:
        @staticmethod                                   # Decoration syntax
        def meth():
                pass

##This has the same effect as the previous example:

class C:
        def meth():
                pass
        meth = staticmethod(meth)                       # Rebind name


##Here, calling the method's function name later actually triggers the result of its staticmethod decorator first.

class Spam:
        numInstances = 0
        def __init__(self):
                self.count()
        def count(self):
                Spam.numInstances += 1
        @staticmethod                                   # Decoration before def
        def printNumInstances():
                print 'Number of instances created: {0}'.format(Spam.numInstances)

>>> a, b, c = Spam(), Spam(), Spam()

>>> a.printNumInstances()                               # Call from both class and instance works now
Number of instances created: 3
>>> Spam.printNumInstances()                            
Number of instances created: 3                          # Both print 'Number of instances created: 3'

        
##A First Function Decorator Example

##Decorators have wide utility and user defined custom uses. This example, a class with __call__ method saves the
##decorated function in the instance and catches calls to the original name.

class tracer:
        def __init__(self, func):
                self.calls = 0
                self.func = func
        def __call__(self, *args):
                self.calls += 1
                print 'call {0} to {1}'.format(self.calls, self.func.__name__)
                self.func(*args)

@tracer                         # Same as 'spam = tracer(spam)'
def spam(a, b, c):              # Wrap spam in a decorator object                       
        print(a, b, c)

>>> spam(1, 2, 3)               # spam is the instance. This calls the __call__ method with (1, 2, 3) with input arguement.
call 1 to spam                  # __call__ adds logic and runs original object. The second line of output comes from the spam function.
(1, 2, 3)
>>> spam('a', 'b', 'c')
call 2 to spam
('a', 'b', 'c')
>>> spam(4, 5, 6)
call 3 to spam
(4, 5, 6)

##Using the decorated function, with a tracer decorator, we save the defined function with the instance. The function
##name is also the instance. Since the class tracer has a __call__ method, when the instance is called with arguments,
##it dispatches it to the original function. It passes the function reference to the __init__ argument.

##However, this decorator works for any function that takes positional arguments, but it does not return the decorated
##function’s result, doesn’t handle keyword arguments, and cannot decorate class method functions (in short, for methods
##its __call__ would be passed a tracer instance only).


##Class Decorators and Metaclasses

##Class decorators are similar to function decorators, but they are run at the end of a class statement to rebind a
##class name to a callable. As such, they can be used to either manage classes just after they are created, or insert
##a layer of wrapper logic to manage instances when they are later created.

def decorator(aClass):
        pass

@decorator
class C:
        pass

##Is equivalent of :
        
def decorator(aClass):
        pass

class C:
        pass
C = decorator(C)

##Class Decorators are usually used to augment classes. For example, if we can automatically augment the classes with
##instance counters and any other data required:

def counter(aClass):
        aClass.numInstances = 0
        return aClass                   # return class itself, instead of a wrapper

@counter                                # is equivalent of Spam = counter(Spam)
class Spam:
        pass

@counter:
        class Sub(Spam):
                pass

##Metaclasses generally redefines the __new__ or __init__ method of the type class, in order to assume control of the
##creation or initialization of a new class object. The net effect, as with class decorators, is to define code to be
##run automatically at class creation time. Both schemes are free to augment a class or return an arbitrary object to
##replace it. More about metaclasses in a later chapter.


##Class Gotchas

##Changing Class Attributes can have side effects, since they are like mutable objects. They can be changed in-place.
##As far as possible, we should not change a class attribute dynamically outside the class statement. If we do have
##to change them, we shoudl do so with class defs interfaces.

>>> class X:
...     a = 1                   # Class attribute
...
>>> I = X()
>>> I.a                         # Inherited by instance
1
>>> X.a


>>> X.a = 2                     # May change more than X
>>> I.a                         # I changes too
2
>>> J = X()                     # J inherits from X's runtime values
>>> J.a                         # (but assigning to J.a changes a in J, not X or I)
2

##Changing Mutable Class Attributes can have side efects too. Changing a class attribute outside the class in-place
##can affect the value of that attribute for all instances.

>>> class C:
	shared = []                     # Class attribute
	def __init__(self):
		self.perobj = []        # Instance attribute

>>> x = C()                             # Two instances
>>> y = C()                             # Implicity chare class attrs
>>> y.shared, y.perobj
([], [])
>>> x.shared.append('spam')             # Impacts y's view too
>>> x.perobj.append('spam')             # Impacts x's data only
>>> x.shared, x.perobj
(['spam'], ['spam'])
>>> y.shared, y.perobj                  # y sees change made through x
(['spam'], [])
>>> C.shared                            # Stored on class and shared
['spam']


##Multiple Inheritance: Order Matters

##In normal inheritance attribute search, python searches superclasses from bottom to top, and then left to right.
##If we have to override attribute inheritance, we will have manually assign in the subclass.

class ListTree:
        def __str__(self): pass
        def other(self): pass
        
class Super:
        def __str__(self): pass
        def other(self): pass
        
class Sub(ListTree, Super):             # Get ListTree's __str__ by listing it first
        other = Super.other             # But explicitly pick Super's version of other
        def __init__(self): pass

x = Sub()                               # Inheritance searches Sub before ListTree/Super


##Methods, Classes and Nested Scopes

>>> def generate():
	class Spam:
		count = 1
		def method(self):
			print(Spam.count)
	return Spam()

>>> generate().method()
1
>>> print Spam.count
<unbound method Spam.count>


def generate():
        return Spam()

class Spam:                                     # Declare at top level
        count = 1
        def method(self):
                print(Spam.count)

>>> generate().method()
1


def generate():
	class Spam:
		count = 1
		def method(self):
			print(self.__class__.count)  # To return a instance's class object
	return Spam()

>>> generate().method()
1



## ----------------
## EXCEPTION BASICS
## ----------------

##There're are different variations of exceptions. They're events that can modify the flow of control
##through the program.

##try/except - Catch and recover from exceptions raised by python or by you.
##try/finally - Perform cleanup actions, whether exceptions occur or not.
##raise - Trigger an exception manually in your code.
##assert - Conditionally trigger an exception in your code.
##with/as - Implement context managers in Python 2.6 and 3.0

##Exception roles

## *Error handling - Python raises exceptions whenever it detects errors in programs at runtime. You can
##either respond to the error, or ignore it to let python print an error message.
##
## *Event notification - Exception can also be used to signal valid conditions without you having to pass
##result flags around a program or test them explicitly. For instance, a search routine might raise an
##exception on failure, rather than returning an integer result code.
##
## *Special-case handling - Sometimes a condition may occur so rarely that it’s hard to justify convoluting
##your code to handle it. You can often eliminate special-case code by handling unusual cases in exception
##handlers in higher levels of your program.
##
## *Termination actions - As you'll see, try/finally statement allows you to guarantee that required closing
##time operations will be performed, regardless of the presence or absence of exceptions in your programs.

## *Unusual control flows - Finally, because exceptions are sort of high-level 'go to', you can use them as
##the basis for implementing exotic control flows. For instance, although the language does not explicitly
##support backtracking, it can be implemented in Python by using exceptions and a bit of support logic
##to unwind assignments.


##Default exception handler - One of the examples when python would raise an exception would be when we
##query out of range or bounds for an indexed sequence. By default, without a handler, python prints
##an error message:

>>> def fetcher(obj, index):
	return obj[index]

>>> x = 'spam'
>>> fetcher(x, 5)
Traceback (most recent call last):                      # stacktrace
  File "<pyshell#62>", line 1, in <module>
    fetcher(x, 5)
  File "<pyshell#60>", line 2, in fetcher
    return obj[index]
IndexError: string index out of range                   # exception raised, error message

##The error message also includes stacktrace, a list of all the lines and functions that were active when the
##the exception occurred. The <pyshell> is displayed when using IDLE, and <stdin> is displayed when using
##basic shell interface interface. The source line numbers won't be of much help here, if we're not using
##a file. If we execute a python file (% python first.py), we get the file name "first.py".


##Catching Exceptions

##If you don't want the default exception behaviour:

>>> try:
	fetcher(x, 4)
except IndexError:                      # Catch and recover
	print 'Got Exception'

Got Exception

##After the exception is caught and handled, the program resumes execution after the entire try statement
##that caught it - which is why we get the 'continuing' message here:

>>> def catcher():
	try:
		fetcher(x, 4)
	except IndexError:
		print 'Got Exception'
	print 'Continuing'

	
>>> catcher()
Got Exception
Continuing


##Raising Exceptions

##Instead of letting python 'raise' errors or exceptions for us, we can also create our own exception events.
##These are called user-triggered exceptions.

>>> try:
	raise IndexError
except:
	print 'Got Exception'

Got Exception

##Here, the user-triggered exception is caught and recovered, and the print statement is executed.

##Without a recover, it'd echo the following error message:

>>> raise IndexError
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    raise IndexError
IndexError

##Instead of 'raise', an 'assert' statement can be used to trigger exceptions too; it's a conditional raise,
##and is used for debugging purposes during development.

>>> assert False, 'Nobody excepts the Spanish Inquisition!'
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    assert False, 'Nobody excepts the Spanish Inquisition!'
AssertionError: Nobody excepts the Spanish Inquisition!


##User-Defined Exceptions

##User-defined exceptions are coded with classes, which inherit from a built-in exception class: usually the
##class named Exception. Class-based exceptions allow scripts to build exception categories, inherit
##behaviour, and have attached state information.

class Bad(Exception):                   # User-defined exception
        pass

def doomed():
        raise Bad()                     # Raise an instance

try:
        doomed()
except Bad:                             # Catch class name
        print 'Got bad'
        

##Termination Actions

##Try statements can include finally blocks. They look like except handlers for exceptions, but the try/finally
##combination specifies termination actions that always execute 'on the way out', regardless of whether
##an exception occurs in the try block. Here, the print would run independent of an exception event.

>>> try:
	fetcher(x, 3)
finally:                                # Termination actions
	print 'after fetch'

'm'
after fetch

##Here, even if the try statement runs without an exception, the finally statement will still run, and the
##program will resume after try. In a similar case, if we write the fetcher and the print as two consecutive
##statements, the print would never be reached if fetcher fails. The try/finally combination avoids that
##pitfall.

fetcher(x, 5)                           # raise an exception
print 'after fetch'                     # print won't run


>>> def after():
	try:
		fetcher(x, 5)           # would be out of range
	finally:
		print 'after fetch'
	print 'after try'

	
>>> after()
after fetch                             # print inside finally runs

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    after()
  File "<pyshell#31>", line 3, in after
    fetcher(x, 5)
  File "<pyshell#14>", line 2, in fetcher
    return obj[index]
IndexError: string index out of range

##Here we don't get the 'after try' message since the control does not resume after the try/finally encounters
##an exception. Here's an example, where we don't encounter an exception.

>>> def after():
	try:
		fetcher(x, 3)           # within range
	finally:
		print 'after fetcher'
	print 'after try'

>>> after()                             # no exception here
after fetcher                           
after try

##In practice, try/except combinations are useful for catching and recovering from exceptions, and try/finally
##combinations come in handy to guarantee that termination actions will fire regardless of any exceptions that
##may occur in the try block’s code.

##There's also an alternative to try/finally statement when using some types of objects. The with/as
##statement runs an object's context management logic to guarantee that termination actions occur:

>>> with open('lumberjack.txt', 'w') as file:                   # Always close file on exit
	file.write('The larch\n')

>>> file
<closed file 'lumberjack.txt', mode 'w' at 0x0000000002EED828>

##Although this option requires fewer lines of code, it’s only applicable when processing certain object types,
##so try/finally is a more general termination structure. On the other hand, with/as may also run startup
##actions and supports user-defined context management code.



## ------------------------
## EXCEPTION CODING DETAILS
## ------------------------

##The try/except/else Statement

##The try is a compound statement; its most complete form is sketched below. It starts with a try header line,
##followed by a block of (usually) indented statements, then one or more except clauses that identify exceptions
##to be caught, and an optional else clause at the end.

try:
        <statement>
except <name1>:                 # Catch a specific exception only. Runs a particular statement for that exception.
        <statements>
except (name2, name3):          # Catch any of the listed exceptions. Runs the exception statement if any of them are raised.
        <statements>
except <name4> as <data>:       # <data> has to do with raise statements and exception classes. Catch the listed exception and its instance. 
        <statements>
except:                         # Catch all (or all other) exception types. Use with care, since, they catch all errors or exceptions; they may catch exceptions meant for other handlers. Also catches system exit as an exception.
        <statements>
else:                           # the else clause runs if no exception is raised
        <statements>
        
##If an exception does occur while the try block’s statements are running, Python jumps back to the try and runs
##the statements under the first except clause that matches the raised exception. Control resumes below the entire
##try statement after the except block runs (unless the except block raises another exception).

##If an exception occurs and it is not caught by any except statements, it passes control to a higher try or its top-
##level exception handler, python's default exception behaviour triggers.

##except clauses are focused exception handlers—they catch exceptions that occur only within the statements in the
##associated try block.

##As an alternative, catching an exception named Exception ignores exceptions related to system exits:

try:
        action()
except Exception:               # Catch all possible exceptions, except exits
        pass

##Example: Catching built-in exceptions

def kaboom(x, y):
    print x + y                         # Trigger TypeError

try:
    kaboom([0, 2, 1], 'spam')
except TypeError:                       # Catch and recover here
    print 'Hello world'
print 'Resuming here'                   # Continue here if exception or not

Hello world
Resuming here

##When the exception occurs, control passes on to the except clause, where it prints 'Hello world' and then it
##continues below the try statement with the next print. 


##The try/finally statement

##If a finally clause is included in a try, Python will always run its block of statements 'on the way out' of the try
##statement, whether an exception occurred while the try block was running or not.

try:
        <statements>            # Run this action first
finally:
        <statements>            # Always run this code on the way out

##If an exception does occur during the try block’s run, Python still comes back and runs the finally block, but it then
##propagates the exception up to a higher try or the top-level default handler; the program does not resume execution
##below the try statement:

def kaboom(x, y):
    print x + y
    
try:
    kaboom([0, 2, 1], 'spam')           # Will raise an exception
finally:
    print 'Hello world'
print 'Resuming here'

Hello world                             # finally runs
..error..                               # unlike except, control doesn't resume below try

##If no exception occurs while the try block is running, Python jumps back to run the finally block and then continues
##execution past below the try statement:

try:
    kaboom([0, 2, 1], [3, 4, 5])        # Won't raise an exception
finally:
    print 'Hello world'
print 'Resuming here'

[0, 2, 1, 3, 4, 5]                      # try runs
Hello world                             # finally runs
Resuming here                           # control resumes below try

# Also, as of python 2.5, finally can be used with try as follows:

try:
        <statements>
except <name1>:
        <statements>
finally:
        <statements>
else:
        <statements>

##Coding termination actions with try/finally

##In this code, we’ve wrapped a call to a file-processing function in a try with a finally clause to make sure that the
##file is always closed, and thus finalized, whether the function triggers an exception or not. This way, later code can
##be sure that the file’s output buffer’s content has been flushed from memory to disk. try/finally statements is a good way to ensure that your closing-time
##(i.e., termination) activities always run:

class MyError(Exception): pass

def stuff(file):
        raise MyError()
file = open('data', 'w')                # Open an input file

try:
        stuff(file)                     # Raises exception, since the file doesn't exist
finally:
        file.close()                    # always close the file to flush output buffers
print 'not reached'                     # continue here only if no exception

...error...
        

##Unified try/except/finally

try:                                    # Merged form
        <main-action>
except Exception1:
        <handler1>
except Exception2:
        <handler2>
else:
        <else-block>
finally:
        <finally-block>

##Here, the finally block will run regardless of whether there's an exception. Also, if there's an exception, control will
##resume after try. This won't happen if there's no except statement merged with finally inside try.

class MyError(Exception): pass

def stuff(file):
        raise MyError()
file = open('data', 'w')

try:
        stuff(file)                     # will raise an exception
except MyError:
    print 'File Error'
finally:
        file.close()                    # will close() regardless of exception
        print 'File closed'
print 'After try'

File Error
File closed
After try
        
##This unified try statement must have the following order syntax:

try -> except                   # can use multiple except statements

try -> except -> else           # else comes after except

try -> except -> else -> finally  # where the else and finally are optional. You can mix finally and else, only if except appears

try -> except -> finally        # can use finally here; no else.

try -> finally                  # can exist separately 


##Combining finally and except by nesting

##The nesting technique was used in previous versions of python where mixed merging wasn't possible. This technique has
##the same effect as unified mixed merging.

try:                            # nested equivalent to unified merged form
        try:
                <main-action>
        except <Exception1>:
                <handler1>
        except <Exception2>:
                <handler2>
        else:
                <no-error>
finally:
        <cleanup>

##Here the finally statement is executed on the way out regardless of what happened in the <main-action>. But, this
##nested form is more obscure and involving writing more data.


##Unified try example:

sep = '-' * 32 + '\n'

print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
        x = 'spam'[99]
except IndexError:
        print 'except run'
finally:
        print 'finally run'
print 'after try'

print(sep + 'NO EXCEPTION RAISED')
try:
        x = 'spam'[3]
except IndexError:
        print 'except run'
finally:
        print 'finally run'
print 'after try'

print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
        x = 'spam'[3]
except IndexError:
        print 'except run'
else:
        print 'else run'
finally:
        print 'finally run'
print 'after try'        
        
print(sep + 'EXCEPTION RAISED, BUT NOT CAUGHT')
try:
        x = 1 / 0
except IndexError:
        print 'except run'
finally:
        print 'finally run'
print 'after try'

# Output
--------------------------------
EXCEPTION RAISED AND CAUGHT
except run
finally run
after try
--------------------------------
NO EXCEPTION RAISED
finally run
after try
--------------------------------
NO EXCEPTION RAISED, WITH ELSE
else run
finally run
after try
--------------------------------
EXCEPTION RAISED, BUT NOT CAUGHT
finally run
..error..
ZeroDivisionError: integer division or modulo by zero


##The raise statement

##To raise exceptions explicitly, you can code raise statements. Now, since exceptions are always of classes in py2.6 and 3,
##we can either raise an instance of class or make and raise instance of class.

raise <instance>                # raise an instance of class
raise <class(<arguements>)>     # make and raise instance of class
raise

##For example:

raise IndexError                # Class (instance created)
raise IndexError()              # Instance (created in statement)

exc = IndexError()              # you can also create instance ahead of time
raise exc

excs = [IndexError, TypeError]  # create a list of exceptions
raise excs[0]                   # raise a selected exception from a list

##If a try includes an except name as X: clause, the variable X will be assigned the instance provided in the raise. This
##X allows the handler to access both data in the instance provided in the raise:

try:
        <main-action>
except IndexError as X:         # X assigned the raised instance object (optional)
        <handler>



class MyExc(Exception): pass

raise MyExc('spam')             # can create an instance using the constructor arguments

try:
        <main-action>
except MyExc as X:              # Instance available in the handler as X
        print X.args            # print the instance attribute



##Propagating Exceptions with raise

try:
        raise IndexError('spam')        # Exceptions remembers arguments
except IndexError:
        print 'propagating'
        raise                           # Reraise most recent exception

propagating
Traceback (most recent call last):
  File "C:\Users\localhost\Documents\Eclipse\Exercises\test.py", line 917, in <module>
    raise IndexError('spam')        # Exceptions remembers arguments
IndexError: spam

##Running a raise this way reraises the exception and propagates it to a higher handler, in this case, default python handler.
        


##The assert Statement

##An assert can be thought of as a conditional raise statement.

assert <test>, <data>           # The <data> part is optional

##works like the following code:

if __debug__:
        if not <test>:          # if test fails, python raises an exception. The optional data argument is used as the exception's constructor argument.
                raise AssertionError(<data>)

##Like all exceptions, the AssertionError exception will kill your program if it’s not caught with a try, in which case the data
##item shows up as part of the error message.

##assert statements may be removed from a compiled program’s byte code if the -O Python command-line flag is used, thereby
##optimizing the program. AssertionError is a built-in exception, and the __debug__ flag is a built-in name that is
##automatically set to True unless the -O flag is used.

##Example:

def f(x):
        assert x < 0, 'x is negative'   # if assert condition is true, then exception is raised with the data statement.
        return x ** 2

>>> f(1)        # will raise an exception since 1 < 0 is false
    assert x < 0, 'x is negative'       # error message includes the value listed in the assert statement.
AssertionError: x is negative

##assert is mostly intended for trapping user-defined constraints, not for catching genuine programming errors.

def reciprocal(x):
        assert x != 0                   # A useless assert!
        return 1 / x                    # Python checks for zero automatically



##with/as context managers

##Python 2.6 and 3.0 introduced a new exception-related statement—the with, and its optional as clause. In py2.5, enabled with an
##import of this form:

from __future__ import with_statement

##the with/as statement is meant to be an alternative for try/finally usage, but it is more useful for termination time or cleanup
##activities that must run regardless of an exception. Unlike try/finally, they support context management protocol. The basic
##format of with statement:

with expression [as variable]:
        <with-block>

##Note that the variable is not necessarily assigned the result of the expression; the result of the expression is the object
##that supports the context protocol, and the variable may be assigned something else intended to be used inside the statement.
##The object returned by the expression may then run startup code before the with-block is started, as well as termination code
##after the block is done, regardless of whether the block raised an exception or not.

##Some python objects have been augmented to support this protocol.

with open(r'C:\misc\myfile', 'r') as myfile:
        for line in myfile:
                print line

##Here, after the block is finished executing, the myfile is closed automatically, regardless of whether there was an exception.
##The context management protocol ensures that myfile is closed after the block is executed.

##To do the same with a try/finally:

myfile = open(r'C:\misc\myfile', 'r')

try:
        for line in myfile:
                print line
finally:
        myfile.close()

##You can also use with context management to manage decimal context from decimal module:

with decimal.localcontext() as ctx:
        ctx.prec = 2
        x = decimal.Decimal('1.00') / decimal.Decimal('3.00')

##After the block finishes, the precision is returned to what it was before the context statement began. To do it with a
##try/finally, we'd have to save and restore it manually.


##The Context Management Protocol

##Creating custom context managers with types as opposed to built-in types with context managers. Here's how the with statement works:

##* The expression is evaluated, resulting in an object known as a context manager that must have __enter__ and __exit__ methods.
##
##* The context manager’s __enter__ method is called. The value it returns is assigned to the variable in the as clause if present, or
##simply discarded otherwise.
##
##* The code in the nested with block is executed.
##
##* If the with block raises an exception, the __exit__(type, value, traceback) method is called with the exception details. If this
##method returns a false value, the exception is reraised; otherwise, the exception is terminated. The exception should normally be
##reraised so that it is propagated outside the with statement.
##
##* If the with block does not raise an exception, the __exit__ method is still called, but its type, value, and traceback arguments
##are all passed in as None.

##Let's take an example considering these rules to write a custom context manager object:

class TraceBlock:
        def message(self, arg):
                print 'running', arg
        def __enter__(self):
                print 'starting with block'
                return self
        def __exit__(self, exc_type, exc_value, exc_tb):
                if exc_type is None:
                        print 'exiting Normally\n'
                else:
                        print 'exception raised !', exc_type
                        return False                    # propagate exception. If there's no return or if None, it is also false.

with TraceBlock() as action:
        action.message('test 1')
        print 'reached'

with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print 'not reached'

# Output
starting with block
running test 1
reached
exiting Normally

starting with block
running test 2
exception raised ! <type 'exceptions.TypeError'>
Traceback (most recent call last):
  File "C:\Users\localhost\Documents\Eclipse\Exercises\test.py", line 947, in <module>
    raise TypeError
TypeError


## -----------------
## EXCEPTION OBJECTS
## -----------------

##Exceptions are of two types, string based and class based. String exceptions were matched by simple object identity: the raised exception
##was matched to except clauses by Python’s is test:

myexc = 'My exception string'

try:
        raise myexc
except myexc:
        print 'caught'

caught

##For a class based exception, when a try statement’s except clause lists a superclass, it catches instances of that superclass, as well as
##instances of all its subclasses lower in the class tree. The net effect is that class exceptions support the construction of exception
##hierarchies: superclasses become category names, and subclasses become specific kinds of exceptions within a category. By naming a general
##exception superclass, an except clause can catch an entire category of exceptions—any more specific subclass will match.

##class-based exceptions better support exception state information (attached to instances) and allow exceptions to participate in inheritance
##hierarchies (to obtain common behaviors).


##Coding Exception classes

##This example illustrates the notion of exception categories — General is a category name, and its two subclasses are specific types of
##exceptions within the category. Handlers that catch General will also catch any subclasses of it, including Specific1 and Specific2:

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
        X = General()                   # raise superclass instance
        raise X

def raiser1():
        X = Specific1()                 # raise subclass instance
        raise X

def raiser2():
        X = Specific2()                 # raise subclas instance
        raise X

for func in (raiser0, raiser1, raiser2):
        try:
                func()
        except General:                 # match general or any subclass of it. Catches General exceptions and all subclass exceptions of General
                import sys
                print 'caught: ' + str(sys.exc_info()[0]) # sys.exc_info() gives info about most recently raised exception. 

# Output

caught: <class '__main__.General'>
caught: <class '__main__.Specific1'>
caught: <class '__main__.Specific2'>


##Briefly, the first item in sys.exc_info() result is the class of the exception raised, and the second is the actual instance raised. In a general
##except clause like the one here that catches all classes in a category, sys.exc_info is one way to determine exactly what’s occurred. In this
##particular case, it’s equivalent to fetching the instance’s __class__ attribute. When an exception is caught, the instance raised is an instance
##of the class listed in the except, or one of its more specific subclasses. Because of this, the __class__ attribute of the instance also gives
##the exception type.

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0(): raise General()
def raiser1(): raise Specific1()
def raiser2(): raise Specific2()

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as X:
        print 'caught: ' + str(X.__class__)


# Output

caught: <class '__main__.General'>
caught: <class '__main__.Specific1'>
caught: <class '__main__.Specific2'>


##Why Exception hierarchies?

##Class based exceptions have the advantage that if a superclass is listed in an except clause, with subclasses as supported exception
##categories that can be caught, new exception categories can be added as additional subclasses. That way, any existing except clause
##with an exception class is automatically updated to catch new exception categories. This won't be possible, if we list individual
##exception subclass names in except clauses as exception categories, as any new exception subclass would have to be updated in the clause
##explicitly, increasing maintenance:

# Ex1
class Divzero(Exception): pass          # Two exception classes are subclasses of the Exception class as exception categories
class Oflow(Exception): pass

def func():
        raise Divzero()                 # create an instance of an exception subclass                  

try:
        func()                          # will raise an exception, and catch the instance
except (Divzero, 0flow):                # only supports catching and recovering from two exception categories
        <handle1>

# Ex2
class Divzero(Exception): pass
class Oflow(Exception): pass
class Uflow(Exception): pass            # new exception subclass category added

def func():
        raise Divzero()

try:
        func()
except (Divzero, 0flow, Uflow):         # have to manually update the exception category list, increasing maintenance          
        <handle1>

# Ex3                                   # ideal way to write custom exception categories
class NumErr(Exception): pass           # create a class derived from the Exception class
class Divzero(NumErr): pass             # all exception categories derived from a superclass
class Oflow(NumErr): pass
class Uflow(NumErr): pass

def func():
        raise DivZero()

try:
        func()                          # raising an exception
except NumErr:                          # will catch the instance of the superclass as well as all the subclasses below it.
        <handle1>

##Also, you can create a module with just the exception classes as a library, and import it. Any new exception categories could be
##added in the __main__ module by:

class NewError(NumErr): pass


##Built-in Exception classes

##Built-in exceptions are predefined class objects from general superclasses. These exceptions live in __builtin__ and are also
##attributes of the standard library module 'exceptions'. The built-in exceptions are organized in a hierarchy to support a variety
##of catching modes. Here's are a few:

##BaseException - The top-level root superclass of exceptions. This class is not supposed to be directly inherited by user-defined
##classes (use Exception instead). It provides default printing and state retention behavior inherited by subclasses by its constructor.

##Exception - The top-level root superclass of application-related exceptions. This is an immediate subclass of BaseException and is
##superclass to every other built-in exception, except the system exit event classes (SystemExit, KeyboardInterrupt, and GeneratorExit).

##ArithmeticError - The superclass of all numeric errors (and a subclass of Exception).

##OverflowError - A subclass of ArithmeticError that identifies a specific numeric error.

##And so on.

##To see the exceptions class tree, see the PyDoc generated from exceptions

>>> import exceptions
>>> help(exceptions)



##Built-in Exception Categories

##The built-in exception class hierarchy allows us to choose the specific type of exception we want to catch. If you're creating user
##defined exceptions, it is better, to derive it from Exception class. Sometimes, it may not be required.

try:
        action()
except ArithmeticError:         # this class will catch all exceptions raised as numeric error
        <handle all application exceptions>
else:
        <handle no-exception case>
        

try:
        action()
except Exception:               # this class has a catchall effect, but it allows system exit to pass as they should
        <handle all application exceptions>
else:
        <handle no-exception case>



##Default Printing and State Information in exception classes

##If an exception class derives from Exception, which derives from BaseException with __init__ and __str__ methods. Unless you redefine
##the constructors your classes inherit from them, any constructor arguments you pass to these classes are saved in the instance’s args
##tuple attribute and are automatically displayed when the instance is printed (an empty tuple and display string are used if no
##constructor arguments are passed).

>>> raise IndexError                    # same as IndexError(): no arguments
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    raise IndexError
IndexError


>>> raise IndexError('spam')            # Constructor argument attached, printed
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    raise IndexError('spam')
IndexError: spam                        # printed here


>>> I = IndexError('spam')              # Available in object attribute
>>> I.args
('spam',)


# Here's an example, when a custom exception class is derived from Exception and raised.

class Exp(Exception): pass

try:
    raise Exp                           # raise exception. No input arguments for the constructor.
except Exp as X:                        # assign exception class instance to a variable
    print 'Exp exception'
    print X, X.args                     # display and saves constructor arguments
print 'Out'

# Output
Exp exception
 ()                                     # Empty display string and tuple are used as default arguments for the constructor.
Out


try:
        raise Exp('spam')               # Input arguement for the constructor
except Exp as X:                        
    print 'Exp exception'
    print X, X.args                     
print 'Out'

# Output
Exp exception
spam ('spam',)                          # argument displayed as instance and as args tuple
Out


try:
        raise Exp('spam', 'eggs', 'ham')
except Exp as X:                        
    print 'Exp exception'
    print X, X.args                     
print 'Out'

# Output
Exp exception
('spam', 'eggs', 'ham') ('spam', 'eggs', 'ham')
Out


##Custom Print Displays

##In the previous example, for printing the constructor arguments, the __str__ method in the BaseException is used, from which Exception
##is derived. It is possible to define custom print __str__ in your exception class derived from Exception, which will override the
##default print method. It's better to use __str__ instead of __repr__ here. Whatever your method returns is included in error messages
##for uncaught exceptions and used when exceptions are printed explicitly.

class MyBad(Exception):
        def __str__(self):
                return 'Always look on the bright side!'

try:
        raise MyBad

except MyBad as X:
        print X

# Output
Always look on the bright side!
        


##Custom Data and Behaviour

##Although the default constructor behaviour is sufficient for most applications, sometimes it is feasible to have custom state retention
##in exception classes. When an exception is raised, Python passes the class instance object along with the exception. Code in try
##statements can access the raised instance by listing an extra variable after the as keyword in an except handler. This provides a
##natural hook for supplying data and behavior to the handler.

class FormatError(Exception):
        def __init__(self, line, file):
                self.line = line
                self.file = file

def raiser():
        raise FormatError(42, file = 'myfile.txt')              # keyword argument as well

try:
        raiser()
except FormatError as X:
        print 'Error at, %s %s' % (X.file, X.line)


Error at, myfile.txt 42

        
##Now, without custom constructor override, the state information reference is less relevant.
class FormatError(Exception): pass

def raiser():
        raise FormatError(42, 'myfile.txt')                     # no keywords allowed
try:
        raiser()
except FormatError as X:
        print 'Error at, %s %s' % (X.args[0], X.args[1])
        

Error at, 42 myfile.txt
        
##On a side note, the raised instance object (X) is also available generically as the second item in the result tuple of the
##sys.exc_info() call


##The exception class can also include methods that can be called inside the exception handler. Here it runs a method that
##saves state information in a file:

class FormatError(Exception):
        logfile = 'formaterror.txt'
        def __init__(self, line, file):
                self.line = line
                self.file = file
        def logerror(self):                             # handler method
                log = open(self.logfile, 'a')
                import sys
                out = sys.stdout
                sys.stdout = log
                print 'Error at, %s %s' % (self.line, self.file)
                sys.stdout = out

def raiser():
	raise FormatError(42, file = 'myfile.txt')

try:
	raiser()
except FormatError as exc:
	exc.logerror()

# output in formaterror.txt file
Error at, 42 myfile.txt
                

##--------------------------
## DESIGNING WITH EXCEPTIONS
##--------------------------

##Nesting Exception Handlers

##Nested try/except statements: When an exception is raised (by you or by Python), control jumps back to the most recently entered try
##statement with a matching except clause, and the program resumes after that try statement. except clauses intercept and stop the
##exception—they are where you process and recover from exceptions. When an exception is caught and handled by an except, its life
##is over. 

##Nested try/finally statements: When an exception is raised here, control returns to the most recently entered try to run its finally
##statement, but then the exception keeps propagating to all finallys in all active try statements and eventually reaches the default
##top-level handler, where an error message is printed. finally clauses intercept (but do not stop) an exception—they are for actions
##to be performed “on the way out.”

# Control flow nesting
def action2():
        print(1 + [])                   # general type error

def action1():
        try:
                action2()
        except TypeError: 
                print 'Inner try'
try:
        action1()
except TypeError:                       # here only if action1() re-raises
        print 'Outer try'

# Output
Inner try                               # the exception is handled at the inner action1(). The prgram continues from there.


# Syntactic Nesting with try/except:
try:
        try:
                action2()
        except TypeError:               # Most recent matching try
                print 'Inner try'
except TypeError:                       # here only if the inner except handler re-raises
        print 'Outer try'

# Output
Inner try

# Syntactic Nesting with try/finally:
try:
        try:
                raise IndexError
        finally:
                print 'spam'
finally:
        print 'SPAM'

# Output
spam
SPAM
Traceback (most recent call last):
  File "C:\Users\localhost\Documents\Eclipse\Exercises\test.py", line 1038, in <module>
    raise IndexError
IndexError


# Syntactic nesting with try/except/finally:

def raise1(): raise IndexError
def noraise(): return
def raise2(): raise SyntaxError

for func in (raise1, noraise, raise2):
        print '\n {0}'.format(func)
        try:
                try:
                        func()                          # raise exception with raise1 and raise2
                except IndexError:                      # if SyntaxError, it will propagate
                        print 'caught IndexError'       
        finally:                                        # will run regardless of an exception
                print 'finally run'

# Output

 <function raise1 at 0x000000000249DCF8>
caught IndexError
finally run

 <function noraise at 0x000000000249DD68>
finally run

 <function raise2 at 0x000000000249DDD8>
finally run
Traceback (most recent call last):
  File "C:\Users\localhost\Documents\Eclipse\Exercises\test.py", line 1051, in <module>
    func()
  File "C:\Users\localhost\Documents\Eclipse\Exercises\test.py", line 1045, in raise2
    def raise2(): raise SyntaxError
SyntaxError: None



##Exception Idioms

## * All errors are exceptions, but not all exceptions are errors: In file operations, the end-of-file in a file read methods is
##indicated by an empty string at the end of a file. In user input method such as raw_input, when a line of text is read from the
##standard input stream, sys.stdin, at each call raises the built-in EOFError at end-of-file. Despite its name, it's just a signal
##in this context, not an error. Because of this behavior, unless the end-of-file should terminate a script, input often appears
##wrapped in a try handler and nested in a loop, as in the following code:

while True:
        try:
                line = input()          # Read line from stdin
        except EOFError:
                break                   # Exit loop at end-of-file
        else:
                ...process next line here...
                
##Several other built-in exceptions are similarly signals, not errors—calling sys.exit() and pressing Ctrl-C on your keyboard,
##respectively, raise SystemExit and KeyboardInterrupt, for example. Python also has a set of built-in exceptions that represent
##warnings rather than errors; some of these are used to signal use of deprecated (phased out) language features.


## * User-defined exceptions can also signal nonerror conditions: Functions can signal conditions with raise

class Found(Exception): pass            # create an exception for success

def searcher():
        if <search-success>:
                raise Found()
        else:
                return

try:
        searcher()
except Found:
        <success>
else:
        <failure>



class Failure(Exception): pass          # create an exception for failure

def searcher():
        if <search-success>:
                return <found-item>
        else:
                raise Failure()

try:
        searcher()
except Failure:
        <report>
else:
        <use found-item here>
        



## * Closing Files and Server Connections: For example, some servers require connections to be closed in order to terminate a session.
##Similarly, output files may require close calls to flush their buffers to disk, and input files may consume file descriptors if
##not closed; although file objects are automatically closed when garbage collected if still open, it’s sometimes difficult to be
##sure when that'll occur.


myfile = open('myFile.txt', 'a')                
try:                                            # using try/finally and with/as context to manage file operations
        <process myfile>
finally:
        myfile.close()


with open('myFile.txt', 'a') as myfile:
        <process myfile>
        

## * Debugging with outer try statements: use of exception handlers to replace Python’s default top-level exception-handling behavior.
##By wrapping an entire program (or a call to it) in an outer try in your top-level code, you can catch any exception that may occur
##while your program runs, thereby subverting the default program termination. You can also use sys.exc_info() call to grab info about
##the recent exception raised.

try:
        <main-program>
except:                         # All uncaught exceptions come here
        import sys
        print 'uncaught! {0} {1}'.format(sys.exc_info()[0], sys.exc_info()[1]) # first and second item of tuple returned by exc_info() are exception’s class and the instance object raised.



## * Running In-Process Tests:

import sys
log = open('testlog.txt', 'a')
from testapi import moreTests, runNextTest, testName
def testdriver():
        while moreTests():
                try:
                        runNextTest()
                except:
                        print('FAILED', testName(), sys.exc_info()[:2], file=log)
                else:
                        print('SUCCESS', testName(), file=log)
testdriver()

##The testdriver function here cycles through a series of test calls (the module testapi is left abstract in this example). Because
##an uncaught exception in a test case would normally kill this test driver, you need to wrap test case calls in a try if you want to
##continue the testing process after a test fails. The empty except catches any uncaught exception generated by a test case as usual,
##and it uses sys.exc_info to log the exception to a file. The else clause is run when no exception occurs—the test success case.

##Such type of code can also be written for more sophisticated use, to test external programs. You could instead check status codes or
##outputs generated by program-launching tools such as os.system and os.popen, covered in the standard library manual (such tools do not
##generally raise exceptions for errors in the external programs—in fact, the test cases may run in parallel with the test driver).            



##The sys.exc_info() call

##This function call is useful when using the empty except clause to catch everything blindly, to determine what was raised. If no
##exception is being handled, this call it returns a tuple containing three None values. Otherwise, the values returned are
##(type, value, traceback), where:
##        
##• type is the exception class of the exception being handled.
##• value is the exception class instance that was raised.
##• traceback is a traceback object that represents the call stack at the point where the exception originally occurred.
##
##As seen before, you can also get the exception type by fetching the __class__ attribute of the instance obtained with the as clause,
##sys.exc_info is mostly used by the empty except.

try:
        ...
except General as instance:
        # instance.__class__ is the exception class








##Exception Design Tips and Gotchas




##What to be wrapped in try statements:

## * Operations that commonly fail, such as interface with system state (file opens, socket calls, an the like) are prime candidates for trys.
##Sometimes, you may want failures of such operations to kill your program instead of being caught and ignored, and is often the best outcome.
##
## * Implementing termination actions in try/finally statements to guarantee their execution, unless a context manager is available as a with/as
##option.
##
## * It is sometimes more convenient to wrap the call to a large function in a single try statement, rather than littering the function itself with
##many try statements. That way, all exceptions in the function percolate up to the try around the call, and you reduce the amount of code within
##the function.






##Catching Too Much: Avoid Empty except and Exception

##An empty except is easy to code, and sometimes desirable, but you may also wind up intercepting an error that’s expected by a try handler higher
##up in the exception nesting structure. Furthermore, except catches all exceptions including system and programming exceptions and SystemExit.

def func():
        try:
                <action>                # IndexError is raised here
        except:
                <handler1>              # But every exception is caught and ended here

try:
        func()
except IndexError:                      # Exception should be processed here
        <handler2>

##For ending a script prematurely , you can raise a SystemExit, which would be caught by sys.exit() to allow early terminations. An empty except
##without this exception would not be able to catch the raise and allow timely termination.

import sys

def bye():
        sys.exit(40)                    # Crucial Error! Abort Now. It raises SystemExit

try:
        bye()
except:                                 # Will catch SystemExit, but since there's no sys.exit(), it will ignore exit. Exception will not intercept SystemExit, because it is not a superclass of SystemExit.
        print 'Got it!'                 # Have to call sys.exit() in order to exit.
print 'Continuing!'


Got it!
Continuing!


##A related call os._exit, also ends a program, but via an immediate termination—it skips cleanup actions and cannot be intercepted with
##try/except or try/finally blocks. It is usually only used in spawned child processes, a topic beyond this book’s scope.

##Another example of a pitfall with an empty except:

mydictionary = {...}

try:
        x = myditchtionary['spam']              # Misspelled - will raise NameError
except:                                         # will catch all exceptions. Should have been KeyError
        x = None                                # This assignment only if KeyError. Will mistakenly assign value to x.
        <continue here>

##The solution is to be as specific in creating handlers as one can be. Make it explicit.





##Catching Too Little: Use Class-based categories

##We saw this example where we had to manually add exception categories to the except statement to update new exceptions to be caught, if
##you're listing only specific exceptions to be caught. There may be a requirement where we need more categories of exceptions and updated.
##So its better to use a superclass exception category and add newer exception subclasses to it:

try:
        ...
except (MyExcept1, MyExcept2):                  # Breaks if you add a MyExcept3
        ...                                     # Non-errors
else:
        ...                                     # Assumed to be an error

# Instead:
try:
        ...
except SuccessCategoryName:                     # OK if I add a myerror3 subclass
        ...                                     # Non-errors
else:
        ...                                     # Assumed to be an error


##Read notes on toolsets available for python, pg.887
