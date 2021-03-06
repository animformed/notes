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

pmc.undoInfo(openChunk=True) # When used, all operations after this can be undoed in a single operation.
try:
	for f in pmc.ls(type='file'):
		f.ftn.set(f.ftn.get().lower())
	pmc.undoInfo(closeChunk=True)

# Check the Error message first, as RuntimeError in pymel is ubiquitous.
# We're doing this since we can't catch a locked attribute with an exception class.
except RuntimeError as ex:	
	pmc.undoInfo(closeChunk=True)
	if ex.args[0].startswith('setAttr: The attribute '):
		pmc.undo()

# For all other errors.
except Exception:
	pmc.undoInfo(closeChunk=True)

## Building a high-level exception handler.
# The exception hook takes the top unhandled exception caught and sent by the interpreter.
# It's not possible for exceptionhook to pass control back to the script.
# The function to be defined for exceptionhook takes three arguments like in sys.exc_info().
# The original function for sys.excepthook is available as sys.__excepthook__

# Using sys.excepthook
>>> 1 + '1'
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'int' and 'str'

>>> import sys
>>> def ehook(etype, evalue, tb):
...     print 'Hello!'
>>> sys.excepthook = ehook
>>> 1 + '1'
Hello!

# In maya, the sys.excepthook is only available for mayapy and can't be used in the gui mode.
# Instead, use the hook, maya.utils.formatGuiException. This can't be used in mayapy.

import maya.utils
def excepthook(tb_type, exc_object, tb, detail=2):
	return 'Hello!'
maya.utils.formatGuiException = excepthook

# It accepts an additional "detail" argument. It should also return a string containing
# the error message to be printed to the script editor. Normal sys.excepthook doesn't 
# return anything.

# To reset the default handler, assign maya.utils._formatGuiException.

import maya.utils 

def excepthook(etype, evalue, tb, detail=2):
   s = maya.utils._formatGuiException(etype, evalue, tb, detail)
   lines = [
	   s,
	   'An unhandled exception occurred.',
	   'Please copy the error info above this message',
	   'and a copy of this file and email it to',
	   'mayasupport@robg3d.com. You should get a response',
	   'in three days or less.'
   return '\n'.join(lines)
maya.utils.formatGuiException = excepthook

# This will print the default error message and the custom message.


# Implementing the custom error handler to check for the exception generated
# from our script files. This will collect the system info and send an email 
# in case of an exception.

import os
import platform
import pymel.core as pmc
import maya.utils
from email.mime.text import MIMEText
import smtplib

LIB_DIR = _normalize(os.path.dirname(__file__))
EMAIL_ADDR = 'mayasupport@robg3d.com'
EMAIL_SERVER = 'localhost'

# Store the original current exception hook. The _formatGuiException
# is not stored directly since other running scripts may have modified 
# formatGuiException and will malfunction.
# When the module is imported, it stores the value of formatGuiException, 
# which could have been the original _formatGuiException or something installed 
# by another script.
_orig_excepthook = maya.utils.formatGuiException

def _normalize(p):
	return os.path.normpath(os.path.abspath(p))

def _collect_info():
	lines = []
	lines.append('Scene Info')
	lines.append('	Maya Scene: ' + pmc.sceneName())
	
	lines.append('Maya/Python Info')
	lines.append('  Maya Version: ' + pmc.about(version=True))
	lines.append('  Qt Version: ' + pmc.about(qtVersion=True))
	lines.append('  Maya64: ' + str(pmc.about(is64=True)))
	lines.append('  PyVersion: ' + sys.version)
	lines.append('  PyExe: ' + sys.executable)
	
	lines.append('Machine Info')
	lines.append('  OS: ' + pmc.about(os=True))
	lines.append('  Node: ' + platform.node())
	lines.append('  OSRelease: ' + platform.release())
	lines.append('  OSVersion: ' + platform.version())
	lines.append('  Machine: ' + platform.machine())
	lines.append('  Processor: ' + platform.processor())
	
	lines.append('Environment Info')
	lines.append('  EnvVars')
	for k in sorted(os.environ.keys()):
		lines.append('	%s: %s' % (k, os.environ[k]))
	lines.append('	SysPath')
	for p in sys.path:
		lines.append('		' + p)
	return lines
	
def _send_mail(body):
	msg = MIMEText(body)
	msg['To'] = EMAIL_ADDR
	msg['From'] = EMAIL_ADDR
	msg['Subject'] = 'Maya Tools Error'
	server = smtplib.SMTP(EMAIL_SERVER)
	try:
		server.sendmail(msg['From'], msg['To'], msg.as_string())
	finally:
		server.quit()

def _handle_our_exc(etype, evalue, tb, detail):
	s = maya.utils._formatGuiException(etype, evalue, tb, detail)
	body = [s]
	body.extend(_collect_info())
	_send_email('\n'.join(body))
	lines = [s,
			'An unhandled exception occurred.',
			'An error report was send to ',
			EMAIl_ADDR + ' with details about the error.']
	
	return '\n'.join(lines)
	
def _is_important_tb(tb):
	while tb:
		codepath = tb.tb_frame.f_code.co_filename
		# Check the directory for the script source in the stack trace,
		# ad see if it matches with our library path.
		if _normalize(codepath).startswith(LIB_DIR):
			return True
		tb  = tb.tb_next
		
	return False
	
def excepthook(etype, evalue, tb, detail=2):
	result = _orig_excepthook(etype, evalue, tb, detail)
	if _is_important_tb(tb):
		result = _handle_our_exc(etype, evalue, tb, detail)
	return result
	
maya.utils.formatGuiException = excepthook

# Use a background thread to send the email.

def _send_email_in_background(body):
	t = threading.Thread(target=_send_email, args=(body,),
	name = 'send_email_in_background')
	t.start()
# You would call _send_email_in_background instead of _send_email inside
# the _handle_our_exc function.

# Another way to see if the exception is generated from our script source is
# to set a module level __author__ attribute on all of files and key 
# off of that. All of the scripts will have the following line at the
# module level.

__author__ = 'rob.galanakis@gmail.com'

# Then the "_is_important_tb" will look like as follows:

def _is_important_tb(tb):
	while tb:
		auth = tb.tb_frame.f_globals.get('__author__')
		
		if auth == __author__:
			return True
		
		tb = tb.tb_next
		
	return False
	

## If you're writing multiple tools, make sure that excepthandling is imported
# early on in each of the tools.

## You can also add a user interface to the error reporting.

## Beyond error reporting via email, you can use taks management system as
# jira.com or trello.com

## You can also check out the traceback2 project at https://code.google.com/p/traceback2/

## Check out the open source sentry server, http://sentry.readthedocs.org/ and 
# the raven client http://raven.readthedocs.org/

## See pg.108 for using logging for error reporting.

import logging
log_filenames = set()	# Avoid duplicates
for logger in logging.Logger.manager.loggerDict.values():
	for handler in getattr(logger, 'handlers', []):
		try:
			log_filenames.add(handler.baseFilename)
		except AttributeError:
			pass
			
# To echo the maya script editor to a file and include that in your e-mail.
pmc.scriptEditor(writeHistory=True, historyFilename='.log')


## CHAPTER 4

# Leveraging Context managers and decorators in maya

## Decorator is a basically smarter syntax to assign a wrapper to an existing function,
# to extend around its functionality

def announce(func):
	def inner(*args, **kwargs):
		print "Calling", func.__name__
		result = func(*args, **kwargs)
		print 'Result', result
		return result	# (2)
	return inner	# (1)

# Function to be decorated
def subtract(a, b):		
	return a - b

>>> announce(subtract)(1, 2)
Calling subtract
Result -1

>>> call = announce(subtract)	# (1) is returned
>>> value = call(1, 2)		# (2) is returned


# The subtract can now be decorated as:

@announce
def subtract(a, b):		
	return a - b
	
>>> subtract(1, 2)
Calling subtract
Result -1

## Using decorator to preserve selection for an exporter function in maya
# 

def preserve_selection(func):
	# Decorator / wrapper
	def inner(*args, **kwargs):
		sel = pymel.core.selected()
		result = func(*args, **kwargs)
		pymel.core.select(sel)
		return result
	return inner
		
@preserve_selection
def export_char_meshes(path):
	"Perform the operation which modifies selection"
	
	
## Using context managers to deal with exceptions

# Writing the undo_chunk context manager

import pymel.core as pc

class undo_chunk(object):
	def __enter__(self):
		pc.undoInfo(openChunk=True)
	def __exit__(self):
		pc.undoInfo(closeChunk=True)
		
with undo_chunk():		# Usage
	pymel.core.joint(), pymel.core.joint()

>>> pymel.core.undo()
>>> pymel.core.ls(type='joint')


# Writing undo_on_error context manager.

class undo_on_error(object):
	def __enter__(self):
		pymel.core.undoInfo(openChunk=True)
	def __exit__(self, exc_type, exc_val, exc_tb):
		pymel.core.undoInfo(closeChunk=True)
		if exc_val is not None:
			pymel.core.undo()

with undo_on_error():	# Usage
	for f in pymel.core.ls(type='file'):
		f.ftn.set(f.ftn.get().lower())

>>> [f.ftn.get() for f in pymel.core.ls(type='file')]
[u'FTN0', u'FTN1', u'FTN2']


## Using decorators or context managers - 
# When calling a function and to have the setup and teardown to happen every time something
# is called, you should prefer to use a decorator. If you want the caller to control the setup
# and teardown (as we would expect for undo), use a context manager.

# It may be required to have the same functionality as a context manager and a decorator.

# Various context managers in maya

# set_file_prompt. file command's prompt sets a maya state, not like a command flag.
#
class set_file_prompt(object):
	def __init__(self, state):
		self.state = state
		self.oldState = None
	def __enter__(self):
		self.oldState = cmds.file(q=True, prompt=True)
		cmds.file(prompt=self.state)
	def __exit__(self, *args):
		cmds.file(prompt=self.oldState)
		
# at_time. Context to maintain the current time in maya, if a command modifies it
#
class at_time(object):
	def __init__(self, time):
		self.time = time
		self.oldTime = None
	def __enter__(self):
		self.oldTime = cmds.currentTime(q=True)
		cmds.currentTime(self.time)
	def __exit__(self):
		cmds.currentTime(self.oldTime)
		
# with_unit context manager, uses cmds.currentUnit(linear=, angle=, time=)
# to change and restore them.

# set_renderlayer_active context manager changes and restores the current render layer.

# set_namespace_active context manager makes a namespace active for a block of code.

# denormalized_skin temporarily toggles the weight normalization and set max influences
# when modifying the skin weighting in a block of code. To speed up the process, you can 
# create a cache of skinClusters that are currently denormalized.


## Creating a decorator to record metrics

# Use a decorator to get a unique key for callable item. Record the time it takes to 
# invoke the callable item. Report the time.

# Getting a unique key for function/method.
import types

def _getkey(func):
	if isinstance(func, types.FunctionType):
		return '%s.%s' % (func.__module__, func.__name__)
	if isinstance(func, types.MethodType):
		return '%s.%s.%s' % (func.__module__,
							func.im_class.__name__,
							func.__name__)
	raise TypeError('%s must be a function or a method' % func)

# Reporting duration
import errno, traceback

def _report_duration(key, duration):
	global _reporting_enabled
	if not _reporting_enabled:
		return
	
	try:
		with open('durations.txt', 'a') as f:
			f.write('%s: %s\n' % (key, duration))
	except OSError as ex:
		if ex.errno == errno.EACCES:
			print 'durations.txt in use, cannot record'
		else:	# Other fatal error
			_reporting_enabled = False
			traceback.print_exc()
			print 'Disabling metrics recording.'

# decorator
import time

def record_duration(func):
	
	key = _getkey(func)
	
	def inner(*args, **kwargs):
		starttime = time.clock()
		
		result = func(*args, **kwargs)
		
		endtime = time.clock()
		duration = endtime - starttime
		_report_duration(key, duration)
		
		return result
		
	return inner

@profiling.record_duration
def export_scene():
	# code
	
	
## Defining decorators with arguments

def deco_using_args(key):
	def _deco(func):
		def inner(*args, **kwargs):
			print 'Hello from', key
			return func(*args, **kwargs)
		return inner
	return _deco

class deco_using_args(object):
	def __init__(self, key):
		self.key = key
	def __call__(self, func):
		def inner(*args, **kwargs):
			print 'Hello from', key
			return func(*args, **kwargs)
		return inner
		
# Use
@deco_using_args('func deco')
def decorated_func():
	#code
	return
	
## Decorating pymel

# Decorating pymel is difficult since so many pymel calls are dynamically dispatched,
# use the reassignment pattern of decoration, decorating and replacing methods,

DagNode.setTranslation = announce(DagNode.setTranslation)

# Avoid decorating pymel as much as possible.


## Stacking decorators

@deco1	# prints deco1
@deco2	# prints deco2
def func():
	print 'inside func'
>>> func()
deco1
deco2
inside func

>>> f = deco1(deco2(func))
>>> f()
deco1
deco2
inside func


## See - https://wiki.python.org/moin/PythonDecoratorLibrary
## https://pypi.python.org/pypi/wrapt



## GUI

# Write a qtshim module as a helper to import the QtCore, QtGui and Signal
# module based on whether PySide or PyQt is available on the system.

# qtshim.py

try:
	from PySide import QtCore, QtGui
	import shiboken
	Signal = QtCore.Signal
	
	def _getcls(name):
		result = getattr(QtGui, name, None)
		if result is None:
			result = getattr(QtCore, name, None)
		return result
	
	def wrapinstance(ptr):
		"""
		Converts a pointer (int or long) into the 
		concrete PyQt/PySide object it represents.
		"""
		ptr = long(ptr)
		qobj = shiboken.wrapInstance(ptr, QtCore.QObject)
		metaobj = qobj.metaObject()
		realcls = None
		while realcls is None:
			realcls = _getcls(metaobj.className())
			metaobj = metaobj.superClass()
		return shiboken.wrapInstance(ptr, realcls)

except ImportError:
	from PyQt4 import QtCore, QtGui
	Signal = QtCore.pyqtSignal
	import sip
	def wrapinstance(ptr):
		return sip.wrapinstance(long(ptr), QtCore.QObject)
		
# Now we can use it for writing with PySide or PyQt

from qtshim import QtGui, QtCore, Signal

def create_window():
	win = QtGui.QMainWindow()
	return win
	
if __name__ == '__main__':
	app = QtGui.QApplication([])
	win = create_window()
	win.show()
	app.exec_()
	
