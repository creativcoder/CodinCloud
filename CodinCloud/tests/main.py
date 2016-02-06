#! /usr/bin/python
import os
import threading
import time
import subprocess
import unittest

class SubprocessTimeoutError(RuntimeError):
	pass

class CommandWithTimeoutTest(unittest.TestCase):
   def test_natural_success(self):
       """Try one that should complete naturally and successfully"""
       self.assertEqual(0, run_command_with_timeout(['sleep', '0.1'], 1.0))
   def test_natural_failure(self):
       """Try one that should complete naturally with an error code"""
       self.assertEqual(1, run_command_with_timeout(['sleep', '-w00t'], 1.0))
   def test_timeout(self):
       """Try one that should be killed after the timeout"""
       with self.assertRaises(SubprocessTimeoutError):
           run_command_with_timeout(['sleep', '10'], 1.0)


# def run_command_with_timeout(cmd,timeout_sec):
# 	proc = subprocess.Popen([cmd],stdout=subprocess.PIPE)
# 	timer = Timer(timeout_sec,proc.kill)
# 	timer.start()
# 	proc.communicate()

# run_command_with_timeout(os.path.abspath('a.out'),5)


# p = None

# def prog():
# 	# while True:
# 	# 	print("Hello")
# 	global p
# 	p = subprocess.Popen([os.path.abspath('a.out')],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# def timed_func():
# 	time.sleep(10)

# def run_command_with_timeout(cmd,timeout_sec):




# #task = threading.Thread(target=program)
# timed_thread = threading.Thread(target=prog)

# #task.start()
# timed_thread.start()

# time.sleep(5 )

# print(timed_thread.is_alive())
# thread
# while True:
# 	print(int(time.clock()))




# while True:
		
# 	if timed_thread.is_alive() and int(time.clock())>1:
# 		timed_thread._Thread__stop()
# 		
# 		break

# print(timed_thread.is_alive())
# print("Halted in ",time.clock())

# if '__main__' == __name__:
#     unittest.main()