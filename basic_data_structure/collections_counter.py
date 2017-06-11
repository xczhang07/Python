# the Counter is a container that keeps track of how many times equivalent values are added.
# It can be used to implement the same algorithms for which bag or multise data structures are
# commonly used in other languages

import	collections

if __name__=="__main__":
	# Counter Initialization
	# case1
	print "\ncollections.Counter initialization\n"
	c1 = collections.Counter(['a', 'b', 'c'])
	print c1
	# case2
	c2 = collections.Counter({'a':1, 'b':1, 'c':1})
	print c2
	# case3
	c3 = collections.Counter(a=1, b=1, c=1)
	print c3
	
	# demo update function of Counter, update function as a insert function of Counter
	print "\n update function of collections.Counter \n"
	c4 = collections.Counter()
	c4.update("aabcccdee")
	print c4
	c4.update({'a':1, 'f':1})
	print c4

	# Counter access, once a counter is populated, its values can be retrieved by dictionary API
	c5 = collections.Counter("abbcccdddd")
	for ele in "abcde":
		print '%s : %d' % (ele, c5[ele])
	
	c6 = collections.Counter('extremely')
	c6['n'] = 0
	print c6
	print list(c6.elements())

	# Arithmetic of collections.Counter
	c7 = collections.Counter(['a','b','c','d','e','f','g'])
	c8 = collections.Counter('google')
	
	print "c7: ", c7
	print "c8: ", c8 
	print "\nCombined counts:"
	print c7 + c8
	
	print "\nSubtraction:"
	print c7 - c8

	print "\nIntersection:"
	print c7 & c8

	print "\nUnion"
	print c7 | c8

	
Output
collections.Counter initialization

Counter({'a': 1, 'c': 1, 'b': 1})
Counter({'a': 1, 'c': 1, 'b': 1})
Counter({'a': 1, 'c': 1, 'b': 1})

 update function of collections.Counter 

Counter({'c': 3, 'a': 2, 'e': 2, 'b': 1, 'd': 1})
Counter({'a': 3, 'c': 3, 'e': 2, 'b': 1, 'd': 1, 'f': 1})
a : 1
b : 2
c : 3
d : 4
e : 0
Counter({'e': 3, 'm': 1, 'l': 1, 'r': 1, 't': 1, 'y': 1, 'x': 1, 'n': 0})
['e', 'e', 'e', 'm', 'l', 'r', 't', 'y', 'x']
c7:  Counter({'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1})
c8:  Counter({'o': 2, 'g': 2, 'e': 1, 'l': 1})

Combined counts:
Counter({'g': 3, 'e': 2, 'o': 2, 'a': 1, 'c': 1, 'b': 1, 'd': 1, 'f': 1, 'l': 1})

Subtraction:
Counter({'a': 1, 'c': 1, 'b': 1, 'd': 1, 'f': 1})

Intersection:
Counter({'e': 1, 'g': 1})

Union
Counter({'g': 2, 'o': 2, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'f': 1, 'l': 1})
