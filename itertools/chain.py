Python itertools functions study

chain(): takes several iterators as arguments and return a single iterator
eg: chain([1,2,3], ['A', 'B'])-->[1,2,3,'A','B']


# import the itertools before using it
from itertools import *

# demo the useful functions in itertools lib: functions create iterator for efficient looping
def demo_chain(l1, l2, l3):
    new_list = list()
    for i in chain(l1, l2, l3):
        new_list.append(i)
    return new_list

if __name__ == "__main__":
    l1 = [1,2,3,4,5]
    l2 = ['a', 'b', 'c', 'd']
    l3 = [[4,5,6], (7,8,9)]
    new_list = demo_chain(l1, l2, l3)
    print new_list
    
output:
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', [4, 5, 6], (7, 8, 9)]
