""" demo the scope of python
    global: tells python that a function plans to change one or more global names/variables
    nested function: will show up the variable scope in the nested function
"""

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

v1 = 25 # a global variable

v2 = 100

def func1():
	"""the function will change global variable"""
	global v1  # use global keyword at here to refer the outside variable v1
	v1 = 88

def outer():
	v2 = 99 # define a local variable in outer function
	def inner():
		print v2  # inner() function will access v2 which belongs to outer() function
	inner()

if __name__ == "__main__":
	logging.debug("before calling func1() to change global variable v1 is: %d" % v1)
	func1()
	logging.debug("after calling func1() to change global variable v1 is: %d" % v1)
	logging.debug("calling outer() function")
	outer()
