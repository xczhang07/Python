# python lambda function: anonymus python function, which is different from the normal python functions. It origin from lambda calculus,
# it allows developer to write very short functions.

# a simple example as following:

if __name__ == "__main__":
    f = lambda x, y: x+y
    g = lambda x: x > 10
    print f(5,6)
    print g(11)
    
# output as following:
# 11
# True

# map function
# signature: map(function, sequence[, sequence, ...]) --> list
# return a list of the results of applying the input function to each item of iterable.
# following example:
>>> f = lambda x, y : x*y
>>> l1 = [1,2,3,4]
>>> l2 = [5,6,7,8]
>>> product_list = map(f, l1, l2)
>>> product_list
[5, 12, 21, 32]

# filter function:
# signature: filter(function or None, sequence) --> list, tuple, or string
# return those items of sequence for which function(item) is true.
# if function is None, return the items are ture of the sequence
# if the sequence is tuple or string, return the same type; else, return list
# following is the example of the filter function for different cases

# input is list and the function is not None
>>> l = [1,2,3,4,5,6,7,8]
>>> f = lambda x: x%2 == 0
>>> ret = filter(f,l)
>>> ret
[2, 4, 6, 8]

# input is string and the function is not None
>>> f = lambda x: x == 'a'
>>> ret = filter(f, 'abcaa')
>>> ret
'aaa'

# input is tuple and the function is not None
>>> f = lambda x: x>10
>>> ret = filter(f, (9,10,11,4,3,16))
>>> ret
(11, 16)
>>> type(ret)
<type 'tuple'>

# input function is none
>>> l = [1,0,-1,1,2]
>>> ret = filter(None, l)
>>> ret
[1, -1, 1, 2]

# reduce function：
# signature: reduce(function, sequence) --> value
# apply a function of two arguments cumulatively to the items of a sequence from left to right.
# examples as following:
>>> l = [1,2,3,4]
>>> f = lambda x,y:x+y
>>> ret = reduce(f,l)
>>> ret
10

>>> list = [10,6,7,5,2,1,8,5]
>>> s = reduce(lambda x,y: x if (x > y) else y, list)
>>> print s
10

