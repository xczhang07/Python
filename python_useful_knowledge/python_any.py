# python any() function
# syntax of any function: any(iterable)
# the parameters may: list, string, dictionary (iterable objects and types)
# return value of any() function:
#   True: if any of the elements in the iterable object is true
#   False: if all of the elements in the iterable object is false, or an iterable is empty
#   Condition Table as following:
#   All values are true:    True
#   Any value is true:      True
#   All values are false:   False
#   Iterable is empty:      False

l = [1,2,3,4]
print any(l)

l = [0, False]
print any(l)

l = [0, False, 5]
print any(l)

l = []
print any(l)

s = "This is great"
print any(s)

s = '000'
print any(s)

s = ''
print any(s)

d = {0: 'False'}
print(any(d))

d = {0: 'False', 1: 'True'}
print(any(d))

d = {0: 'False', False: 0}
print(any(d))

d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))



result:

True
False
True
False
True
True
False
False
True
False
False
True

Process finished with exit code 0
