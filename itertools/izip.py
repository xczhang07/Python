izip() function
from itertools import *

# demo the useful functions in itertools lib: functions create iterator for efficient looping

# izip() returns an iterator that combines the elements of several iterators into tuples
# it works like the built-in zip() function, except returns iterator than list

def demo_izip(l1, l2):
    new_list = list()
    for i in izip(l1, l2):
        new_list.append(i)
    return new_list

if __name__ == "__main__":
    l1 = [1,2,3]
    l2 = ['a', 'b', 'c']
    new_list = demo_izip(l1, l2)
    print new_list

    l3 = ['d', 'e']
    new_list = demo_izip(l1, l3)
    print new_list
  
output:
[(1, 'a'), (2, 'b'), (3, 'c')]
[(1, 'd'), (2, 'e')]
