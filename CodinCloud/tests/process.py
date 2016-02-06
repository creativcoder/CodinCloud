import multiprocessing
import threading
import time

def worker():
	name = multiprocessing.current_process().name
	print name,'starting'
	time.sleep(2)
	print name,'Exiting'

def my_service():
	name = multiprocessing.current_process().name
	print name,'Starting'
	time.sleep(3)
	print name,'Exiting'

def daemon_example():
	p = multiprocessing.current_process().name
	p.daemon = True
	print 'Starting',p.name


def non_daemon_example():
	p = multiprocessing.current_process().name


if __name__=='__main__':
	worker = multiprocessing.Process(name='WorkerProcess',target=worker)
	service = multiprocessing.Process(name='Service',target=my_service)
	worker.start()
	service.start()
	
