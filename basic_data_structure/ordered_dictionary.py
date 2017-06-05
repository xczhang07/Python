# Ordered Dictionary is a dictionary subclass that remembers the order in which its contents are added.
# Ordered Dictionary is ordered sensitive! for example, two ordered dictionaries, contents is the same, they
# are considered different if the ordered is different
import collections

def regular_dictionary():
    """demo for regular dictionary"""
    d = dict()
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    d['d'] = 'D'
    d['e'] = 'E'
    print "print out the regular dictionary"
    for k,v in d.items():
        print k,v

def ordered_dictionary():
    """demo for regular dictionary"""
    d = collections.OrderedDict()
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    d['d'] = 'D'
    d['e'] = 'E'
    print "print out the ordered dictionary"
    for k,v in d.items():
        print k,v

if __name__ == "__main__":
    regular_dictionary()
    ordered_dictionary()



Output:
print out the regular dictionary
a A
c C
b B
e E
d D
print out the ordered dictionary
a A
b B
c C
d D
e E

Process finished with exit code 0
