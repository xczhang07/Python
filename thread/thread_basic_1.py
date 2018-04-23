'''
learning script for python threading module, includes:
	1. how to create thread target function
	2. how to pass the target function into thread constructor
	3. how to pass arguments to thread target function
	4. how to set a thread as daemon thread (a daemon thread does not block the main program exit)

04/07 2018
author Xiaochong Zhang
'''

import threading
import time
import logging  #logging is thread safe
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def worker(num):
	logging.debug('starting')
	print "Worker : %s" % num
	logging.debug('ending')
	return

def daemon():
	logging.debug('starting')
	time.sleep(5)	# we should not see the ending message of daemon thread, the main program has already exit
	logging.debug('ending')

def generate_threads(num):
	threads = []
	for i in range(num):
		t = threading.Thread(target=worker, args=(i,))
		threads.append(t)
		t.start()


def generate_daemon_thread():
	dt = threading.Thread(name="daemon_thread", target=daemon) # using the "name" attribute of Thread can specify the name of a thread
	dt.setDaemon(True)
	dt.start()
	dt.join()  #after calling join() function of thread, main program will wait until all sub-thread ending

if __name__ == "__main__":
	generate_threads(3)
	generate_daemon_thread()
