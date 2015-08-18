#! /usr/bin/python
import os
import threading
import time
import subprocess

p = None

def prog():
	# while True:
	# 	print("Hello")
	global p
	p = subprocess.Popen([os.path.abspath('a.out')],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def timed_func():
	time.sleep(10)



#task = threading.Thread(target=program)
timed_thread = threading.Thread(target=prog)

#task.start()
timed_thread.start()

time.sleep(5 )

print(timed_thread.is_alive())
thread
# while True:
# 	print(int(time.clock()))




# while True:
		
# 	if timed_thread.is_alive() and int(time.clock())>1:
# 		timed_thread._Thread__stop()
# 		
# 		break

# print(timed_thread.is_alive())
# print("Halted in ",time.clock())
