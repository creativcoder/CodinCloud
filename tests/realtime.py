from multiprocessing import Process
import psutil
import subprocess
import shlex
import os
import time

from subprocess import Popen,PIPE

process = None

def run_my_program():
	my_inp = '34\n56\n32\n768'
	global process
	process = subprocess.Popen([os.path.abspath('a.out')], stdout=subprocess.PIPE,stdin=subprocess.PIPE)
	print "communicating now"
	stdout = process.communicate(my_inp)[0]
	print stdout
	
	print "done communicating"

TIMEOUT = 1

if __name__=='__main__':
	p = Process(target=run_my_program,args=())
	print 'Starting process'
	p.start()
	print 'Process was started'
	pp = psutil.Process(process.pid)
	
	print 'The pid is : ',p.pid
	print time.time()-pp.create_time()
	time.sleep(0.0036)
	pp.kill()
	# while 1:
	# 	if(time.time()-pp.create_time())>TIMEOUT:
	# 		pp.kill()
 #        	print("This was an infinte loop")
 #        	raise RuntimeError('timeout')
 #        	break
	# #print 'The process took time: ',time.time()-j.create_time()
	p.join()