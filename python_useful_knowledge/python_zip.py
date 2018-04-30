"""
Author: Xiaochong Zhang
Time: 2018/04/29
learnning experience of python zip() function

zip() function returns an iterator of tuples based on iterable object

"""
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)




if __name__ == "__main__":
	logging.debug("combine number list and charactor list with zip() function")
	number_list = [1,2,3]
	charactor_list = ['a','b','c']
	ret = zip(number_list, charactor_list)
	logging.debug(ret)
	
	logging.debug("different numbers of elements passed in zip()")
	str_list = ['this is 1', 'this is 2', 'this is 3', 'this is 4']
	number_tuple = ('one', 'two')
	ret = zip(number_list, str_list, number_tuple)
	logging.debug(ret)

	logging.debug("testing unzip function")
	ret = zip(number_list, charactor_list)
	logging.debug("before the unzip, zip return value is: {0}".format(ret))
	k, v = zip(*ret)
	logging.debug("after the unzip, result is: {0}, {1}".format(k,v))
