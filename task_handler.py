import subprocess
import time
import sys
import os
import psutil
import re
from template import code_templates

import logging


def infinite(process,inp):
	TIMEOUT = 2
	INFINITE = False
	subp_obj = subprocess.Popen([os.path.abspath('a.out')],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
	p = psutil.Process(subp_obj.pid)
	# logging.debug("communicate ran")
	# while 1:
	# 	if (time.time()-p.create_time())>TIMEOUT:
	# 		p.kill()
	# 		print("This was an infinite loop")
	# 		raise RuntimeError('timeout')
	return INFINITE
	

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class CodeTask:

	def __init__(self,lang_name):
		self.lang_id=lang_name
		if self.lang_id == 1:
			if os.path.exists(os.path.abspath('a.out')):
				subprocess.Popen(['rm',os.path.abspath('a.out')])
				f=open('main.c','w')
				f.write(code_templates.get('c'))
				f.close()
				time.sleep(0.5)
				subprocess.Popen(['gcc',os.path.abspath('main'+'.c')],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			else:
				pass
		if self.lang_id == 2:
			self.f=open('temp.py','w')
			self.f.write("print ''")
			self.f.close()
			subprocess.Popen(['python',os.path.dirname(os.path.abspath(__file__))+'/temp.py'])

	def compile(self,file_name,source_code,std_input=''):
		if self.lang_id == 2:
			self.source_code=source_code
			self.file_name=file_name
			self.o=open('{}.py'.format(self.file_name),'w')
			self.o.write(self.source_code)
			self.o.close()
			self.output_string = subprocess.Popen(['python',os.path.dirname(os.path.abspath(__file__))+'/{}.py'.format(self.file_name)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			time.sleep(0.4)	
			#self.output_string = subprocess.Popen([os.path.dirname(os.path.abspath(__file__))+'/main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			print self.output_string.stdout.read()
			return self.output_string.stdout.read()

		elif self.lang_id == 1:
			self.PROCESS_IDENT = 'a.out'
			self.final_output = None
			self.output_string = None
			self.source_code = source_code
			self.std_input = std_input.split('\n')
			self.file_name = file_name
			self.o = open('{}.c'.format(self.file_name),'w')
			self.o.write(self.source_code)
			self.o.close()
			time.sleep(0.5)
			
			subprocess.Popen(['gcc',os.path.abspath(self.file_name+'.c')],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			logging.debug("process checker has started")
			logging.debug(len(self.std_input))
			# check for an infinite process
			# logging.debug(infinite(self.PROCESS_IDENT,self.std_input))
			if not infinite(self.PROCESS_IDENT,self.std_input):
				self.output_string = subprocess.Popen([os.path.abspath('a.out')],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
				# logging.debug('THE STANDARD INPUT'+self.std_input)
				if len(self.std_input) == 0:
					logging.debug("std input is empty")
					self.final_output = self.output_string.stdout.read()
				elif len(self.std_input) != 0:
					logging.debug("std input is present proceeding ahead")
					logging.debug(len(self.std_input))
					# for i in range(len(self.std_input)):
					# 	print("running")
					# 	self.output_string.stdin.write(str(i))
					# 	#logging.debug(self.output_string.stdout.readline())
					# 	# self.final_output += self.output_string.stdout.read()
					# logging.debug("Writing EOF")
					# logging.debug("Ended EOF")
				self.final_output = self.output_string.communicate(std_input)[0]
				logging.debug("Output Stream Read Complete")
			return self.final_output

