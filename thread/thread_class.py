"""
create a subclass for python thread

04/07 2018
Author: Xiaochong Zhang

"""

import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


class MyThread(threading.Thread):
	
	def run(self):
		logging.debug("running")
		return

class ThreadWithArguments(threading.Thread):
	def __init__(self, group=None, target=None, name=None, 
			args=(), kwargs=None, verbose=None):
		threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)

		self.args = args
		self.kwargs = kwargs
		return
	
	def run(self):
		logging.debug("running with %s and %s", self.args, self.kwargs)
		return

if __name__ == "__main__":
	for i in range(3):
		t = MyThread()
		t.start()
	#test thread with arguments
	for i in range(3):
		t = ThreadWithArguments(args=(i,), kwargs={'c':'I like it', 'c++':'I love it'})
		t.start()
