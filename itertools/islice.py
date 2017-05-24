from itertools import *

# demo the useful functions in itertools lib: functions create iterator for efficient looping

# islice() returns an iterator which returns selected items from input iterator, by index.
# it takes the same parameter as the slice operator for list: start, stop, and step.
# islice(sequence, [start], stop, [step]): the start and step are optional

def demo_islice(l1):
    print "the input list is: ", l1
    print "get and print the 1st 2 elements"
    ret = islice(l1, 2)
    for ele in ret:
        print ele

    print "get and print the last 2 elements"
    ret = islice(l1, len(l1)-2, len(l1))
    for ele in ret:
        print ele

    print "get and print every 3 elements"
    ret = islice(l1, 0, len(l1), 3)
    for ele in ret:
        print ele



if __name__ == "__main__":
    l1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    demo_islice(l1)

output:
the input list is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
get and print the 1st 2 elements
1
2
get and print the last 2 elements
14
15
get and print every 3 elements
1
4
7
10
13
