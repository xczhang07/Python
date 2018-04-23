'''
 Created by: Xiaochong Zhang
 Time: 2018/04/23
 Demo for the thread signal
'''

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


def wait_for_event(e):
	"""waiting for the event to be set before doing anything"""
	logging.debug('wait_for_event starting')
	event_is_set = e.wait()
	logging.debug('calling in wait_for_event function. event set: %s', event_is_set)

def wait_for_event_timeout(e,t):
	"""wait until t seconds expire"""
	while not e.isSet():
		logging.debug('wait_for_event_timeout starting')
		event_is_set = e.wait(t)
		logging.debug('calling in wait_for_event_timeout function. event is set: %s', event_is_set)
		if event_is_set:
			logging.debug('processing event') 
		else:
			logging.debug('do the other work')	


if __name__ == "__main__":
	e = threading.Event()
	t1 = threading.Thread(name='block', target=wait_for_event, args=(e,))
	t1.start()
	t2 = threading.Thread(name='non-block', target=wait_for_event_timeout, args=(e,2))
	t2.start()
	
	logging.debug('Waiting before calling Event.set()')
	time.sleep(10)
	e.set()
	logging.debug('Event is set')
		


