## CHAPTER 1

## Check for methods in a pymel obj.

import inspect
import pymel.core as pmc

xform, shape = pmc.polySphere()

methods = []

for a in dir(xform):
    attr = getattr(xform, a)
    if inspect.ismethod(attr):
        methods.append(attr)
        
attrs = xform.listAttr()

>>> methods
[<bound method Transform.__add__ of nt.Transform(u'pSphere1')>, ...]
>>> attrs
[Attribute(u'pSphere1.message'), ...]


## Appending substrings to a list of strings is faster than incrementally 
# concatenating them into a larger string.


## Express and evaluate using pymel types, use __bases__ and __mro__.
>>> j = pmc.joint()
>>> j.type()
u'joint'
>>> type(j)
<class 'pymel.core.nodetypes.Joint'>
>>> type(j).__bases__
(<class 'pymel.core.nodetypes.Transform'>,)
>>> j.translate, j.rotate
(Attribute(u'joint2.translate'), Attribute(u'joint2.rotate'))

# __mro__ or method resolution order is what python visits different types
# so it can figure out what to actually call.

>>> type(j).__mro__
(<class 'pymel.core.nodetypes.Joint'>,
<class 'pymel.core.nodetypes.Transform'>,
<class 'pymel.core.nodetypes.DagNode'>,
<class 'pymel.core.nodetypes.Entity'>,
<class 'pymel.core.nodetypes.ContainerBase'>,
<class 'pymel.core.nodetypes.DependNode'>,
<class 'pymel.core.general.PyNode'>,
<class 'pymel.util.utilitytypes.ProxyUnicode'>,
<type 'object'>)

# When a call to j.name() is invoked, python will walk along the MRO
# looking for the first appropriate method to call.

## minspect.py

def info(obj):
    """Prints information about the object."""
    
    lines = ['Info for %s' % obj.name(),
    'Attributes:']
    
    # Get the name of all attributes
    for a in obj.listAttr():
    lines.append(' ' + a.name())
    lines.append('MEL type: %s' % obj.type())
    lines.append('MRO:')
    lines.extend([' ' + t.__name__ for t in type(obj).__mro__])
    result = '\n'.join(lines)
    print result
    
    
## All maya objects are PyNodes. Anything that inherits from 'DependNode'
# has attributes. 'Attributes' are not a 'DependNode', but our 'Transform' is,
# and that 'Transform' is a 'DagNode'.


## The 'ProxyUnicode' class should be treated as an implementation detail.
# The only important user-facing detail is that it allows PyNodes to have
# strings methods on them (.replace, .strip, etc). WHO uses that? 


## Ambiguous string representation for pymel.core.datatypes.Vector
# It returns correct representation with repr() call, or it can be 
# confused with a list type.

>>> vect = xform.translate.get()
>>> lst = [0.0, 0.0, 0.0]
>>> str(vect)
'[0.0, 0.0, 0.0]'
>>> str(lst)
'[0.0, 0.0, 0.0]'
>>> print t, lst # The print implicitly calls str(t)
[0.0, 0.0, 0.0] [0.0, 0.0, 0.0]
>>> repr(t) # repr returns a more detailed string for an object
'dt.Vector([0.0, 0.0, 0.0])'
>>> repr(lst)
'[0.0, 0.0, 0.0]'


## pymel.core.datatypes.Vector has __getitem__ and __iter__ methods, supporting
# iteration and index lookups.

>>> t = xform.translate.get()
>>> for c in t:
... print c
0.0
0.0
0.0

>>> t[0], t[1], t[2]
(0.0, 0.0, 0.0)


## pymel.core.datatypes.Vector supports adding vectors mathematically.

>>> [1, 2, 3] + [4, 5, 6] # Regular Python lists
[1, 2, 3, 4, 5, 6]
>>> repr(t + [1, 2, 3])
'dt.Vector([1.0, 2.0, 3.0])'

# And other useful methods.

# Using Vector with list

>>> def move_along_x(xform, vec):
... t = xform.translate.get()
... t[0] += vec[0]
... xform.translate.set(t)

>>> j = pmc.joint()
>>> move_along_x(j, [1, 0, 0])
>>> j.translate.get()
dt.Vector([1.0, 0.0, 0.0])
>>> move_along_x(j, j.translate.get())
>>> j.translate.get()
dt.Vector([2.0, 0.0, 0.0])


## Creating a query function for PyMEL object

def _py_to_helpstr(obj):
    
    # If object to be queried is a string, search using that.
    if isinstance(obj, basestring):
        return 'search.html?q=%s' % (obj.replace(' ', '+'))
    
    # To go further, test if the obj is a pymel object.
    if not _is_pymel(obj):
        return None
        
    # If the object is a module.
    # URL: <base_url>/generated/<module name>.html#module-<module_name>
    # >>> pymel.core.nodetypes.__name__
    # 'pymel.core.nodetypes'
    #
    if isinstance(obj, types.ModuleType):
        return ('generated/%(module)s.html#module-%(module)s' %
                dict(module=obj.__name__))
                
    # If the object type is a method.
    # To support:
    # Class methods: @classmethod
    # Static method: @staticmethod. This is really a function type and not a method. Avoid using with instance.
    # Bound method: MyClass().mymethod
    # Unbound method: MyClass.mymethod
    #
    if isinstance(obj, types.MethodType):
        return ('generated/classes/%(module)s/'
                '%(module)s.%(typename)s.html'
                '#%(module)s.%(typename)s.%(methname)s' % dict(
                    module=obj.__module__,
                    typename=obj.im_class.__name__,
                    methname=obj.__name__))
    
    # If the object is a function type.
    # Any def which is not a part of a class definition, first argument is not cls or self.
    # lambdas and staticmethods are also functions.
    #
    if isinstance(obj, types.FunctionType):
        return ('generated/functions/%(module)s/'
                '%(module)s.%(funcname)s.html'
                '#%(module)s.%(funcname)s' % dict(
                    module=obj.__module__,
                    funcname=obj.__name__))
                    
    # Treat a type as a last case. If we pass something that is not 
    # a type, we can just get the object's type and use that.
    # URL: generated/classes/<module>/<module>.<type>.html#<module>.<type> 
    #
    if not isinstance(obj, type):
        obj = type(obj)
        
    return ('generated/classes/%(module)s/'
            '%(module)s.%(typename)s.html'
            '#%(module)s.%(typename)s' % dict(
                module=obj.__module__,
                typename=obj.__name__))

def _is_pymel(obj):
    '''Tests whether an obj is a pymel object.'''
    
    # If obj is part of a module, get its module name.
    try: # (1)
        module = obj.__module__ # (2)
    
    # Else, if obj is a module, get its name.
    except AttributeError: # (3)
        try:
            module = obj.__name__ # (4)
        except AttributeError:
            return None # (5)
    
    # Check if the module is a pymel module.
    return module.startswith('pymel') # (6)
    
# Do tests for pymel objects. 
def test_py_to_helpstr():

    def dotest(obj, ideal):
        '''Check if the obj's returned query string matches the one provided.'''
        result = _py_to_helpstr(obj)
        assert result == ideal, '%s != %s' % (result, ideal)
    
    # TESTS
    # String.
    dotest('maya rocks', 'search.html?q=maya+rocks')
    
    # Module.
    dotest(pmc.nodetypes,
           'generated/pymel.core.nodetypes.html'
           '#module-pymel.core.nodetypes')
    
    # Type.
    dotest(pmc.nodetypes.Joint,
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint')
    
    # Instance.
    dotest(pmc.nodetypes.Joint(),
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint')
    
    # Bound method.
    dotest(pmc.nodetypes.Joint().getTranslation,
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint.getTranslation')
    
    # Function.
    dotest(pmc.joint,
           'generated/functions/pymel.core.animation/'
           'pymel.core.animation.joint.html'
           '#pymel.core.animation.joint')
           
    dotest(object(), None)
    dotest(10, None)
    dotest([], None)
    dotest(sys, None)
    
    
## Designing with EAFP verus LBYL.
# Easier to ask for forgiveness than permission and look before you leap.
# The try instatement in _is_pymel written can be done in the following ways:

# Version 1             # LBYL, since we're interested in getting the __name__
module = None
if isinstance(obj, types.ModuleType):
    module = obj.__name__

# Version 2             # EAFP
module = None
if hasattr(obj, '__name__'):
    module = obj.__name__

# Version 3             # EAFP, more concise.
module = getattr(obj, '__name__', None)

# Version 4             # Full EAFP, with room for error.
try:
    module = obj.__name__
    except AttributeError:
        module = None

# You may wish to use LBYL instead of EAFP in cases where a RuntimeError is generated.
# It's unhelpful since it can be raised for any number of reasons (for example, creating 
# a circular parent/child relationship). Rather than potentially swallowing an unexpected
# error, or doing something ugly like parsing the error message, we use LBYL.
        
## Opening _py_to_helpstr() links in a browser

import webbrowser # (1)
HELP_ROOT_URL = ('http://download.autodesk.com/global/docs/'
                 'maya2013/en_us/PyMel')# (2)


def pmhelp(obj): # (3)
    """Gives help for a pymel or python object.

    If obj is not a PyMEL object, use Python's built-in
    `help` function.
    If obj is a string, open a web browser to a search in the
    PyMEL help for the string.
    Otherwise, open a web browser to the page for the object.
    """
    tail = _py_to_helpstr(obj)
    if tail is None:
        help(obj) # (4)
    else:
        webbrowser.open(HELP_ROOT_URL + tail) # (5)
        
        
## Pass in a select object in maya to pmhelp,
# can be installed as a shelf button.

"import pymel.core as pmc; import minspect;
minspect.pmhelp(pmc.selected()[0])"


## CHAPTER 2

## Writing composable code

# Try to break functions in such a way that they do a single thing. One 
# exmaple is the cmds.ls() function performing the selection and filtering.
# If each piece of code does just what it says, and does only what it can 
# comfortably guarantee, our codebase will be simpler overall.

# Avoid using too many boolean argument flags in functions.

# Use list comprehensions as possible

# Implementing 'is_exact_type'

def is_exact_type(node, typename):
    """node.type() == typename"""
    return node.type() == typename


def is_type(node, typename):
    """Return True if node.type() is typename or
    any subclass of typename."""
    return typename in node.nodeType(inherited=True)
    
# In a function, an argument with _var name with _ suggests that it's 
# a protected parameter, and should not be called outside the module.
# A name with _ prefix indicates it's protected.
    

## Writing the docstring and pseudocode, see PEP 257. If using sphinx for
# documenting python code, using reST inside docstrings is supported.


## Writing skeletonutils.py


## Implementing an alternate pymel method for "setParent", safe_setparent
# which may return error if the node is already under the passed in transform.


## Using nested functions or closures


## Writing character creator. Try to maximise function reuse and write functions
# which do one thing at a time. See the code repository.


## Defining performance

# Type 1
def remove_selected(objs):
... return [item for item in objs if item not in pmc.selected()]

def remove_selected_faster(objs):   # evaluate selected() once
... selected = pmc.selected()
... return [item for item in objs if item not in selected]

# Type 2
def get_type_hierarchy(typename):
... node = pmc.createNode(typename)
... result = node.nodeType(inherited=True)
... pmc.delete(node)
... return result

>>> get_type_hierarchy('joint')
[u'containerBase', u'entity', u'dagNode', u'transform', u'joint']

def get_type_hierarchy_faster(typename):    # Use caching
... result = _hierarchy_cache.get(typename)
... if result is None:
...     node = pmc.createNode(typename)
...     result = node.nodeType(inherited=True)
...     pmc.delete(node)
...     _hierarchy_cache[typename] = result
... return result

# Type 3
j1 = pmc.joint()
cluster = pmc.skinCluster(j1, pmc.polyCube()[0])
def add_influences(cl, infls):
    for infl in infls:
        cl.addInfluence(infl)
        
def add_influences(cl, infls):  # SkinCluster.addInfluence() takes in a list of arguments
    cl.addInfluence(infls)
    

# Rewriting inner loops to use maya.cmds, since pymel may have to go through several layers 
# of abstraction. Use API even possible, for even faster performance.

# Use the standard library cProfile module for profiling python code.



## CHAPTER 3

## Exception types

>>> ex = SystemError('a', 1)
>>> [t.__name__ for t in type(ex).__mro__]
['SystemError', 'StandardError', 'Exception', 'BaseException', 'object']
>>> ex.args
('a', 1)
>>> dir(ex)
['__class__', '__delattr__', ...'args', 'message']

# Use the Exception class as the base exception type. 


## Explaining the exc_info tuple

## Only catch errors you can handle

# Avoid partial mutations during an exception, which may leave the operation in an unresolved state.


## Practical error handling in maya

# Consider the following example with the fileTextureName being modified in a maya scene.
for f in pmc.ls(type='file'):
    f.ftn.set(f.ftn.get().lower())
    
Traceback (most recent call last):
RuntimeError: setAttr: The attribute 'file2.fileTextureName' is locked or connected and cannot be modified.
>>> [f.ftn.get() for f in pmc.ls(type='file')]
[u'ftn0', u'FTN1', u'FTN2']

# Avoiding mutation to address this problem cannot be done because of maya's design.

# Second strategy of read-copy-update cannot be done since when a maya node is copied, it makes complex
# changes to the scene. The read-copy-update pattern involves reading the value of some data, creating a 
# copy of that data, changing that data, and updating the original value. It is commonly used as a 
# synchronization mechanism (for example, between threads). It can also be used to ensure some data
# is not left partially mutated in the case of an error, by ensuring that the original data is not 
# changed unless the entire mutation succeeds.

# The third strategy is to roll back any changes if any error occurs. Store the original value of
# fileTextureName attribute and revert to it during an exception.

# The last strategy is to use undo blocks and is the recommended method.



