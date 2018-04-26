'''
Author: Xiaochong Zhang
Time: 2018/04/26
Closure: whatever the label, the function object in question remembers values in enclosing scopes
regardless of whether those scopes are still present in memory.

'''
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def maker(N):
	'''
	return a function object to the caller, and the return function object will
	remember all the state which keeps in the action function
	'''
	def action(x):
		return x ** N
	return action


if __name__ == "__main__":
	f_obj1 = maker(2)  # we pass 2 to N, and return the function object to f_obj1
	logging.debug(type(f_obj1))
	ret = f_obj1(4)   # we pass 4 to x, then the ret value should be 16
	logging.debug("the resulte is: %d\n" %ret)
