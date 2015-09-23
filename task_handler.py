import subprocess
import time
import sys
import os
import psutil

import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class CodeTask:

	def __init__(self,lang_name):
		self.lang_id=lang_name
		if self.lang_id == 1:
			if os.path.exists(os.path.abspath('a.out')):
				subprocess.Popen(['rm',os.path.abspath('a.out')])
			else:
				pass
			# self.f=open('temp.c','w')
			# self.f.write('#include <stdio.h>\nint main(){printf("");}')
			# self.f.close()
			# subprocess.Popen(['gcc',os.path.dirname(os.path.abspath(__file__))+'/temp.c','-o','main'])
		if self.lang_id == 2:
			self.f=open('temp.py','w')
			self.f.write("print ''")
			self.f.close()
			subprocess.Popen(['python',os.path.dirname(os.path.abspath(__file__))+'/temp.py'])

	def compile(self,file_name,source_code,std_input):
		if self.lang_id == 2:
			#print source_code
			self.source_code=source_code
			self.file_name=file_name
			self.o=open('{}.py'.format(self.file_name),'w')
			#self.o=open('{}.c'.format(self.file_name),'w')
			self.o.write(self.source_code)
			self.o.close()
			#subprocess.Popen(['gcc',os.path.dirname(os.path.abspath(__file__))+'/{}.c'.format(self.file_name),'-o','main'])
			self.output_string = subprocess.Popen(['python',os.path.dirname(os.path.abspath(__file__))+'/{}.py'.format(self.file_name)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			#logging.debug(self.output_string)
			time.sleep(0.7)	
			#self.output_string = subprocess.Popen([os.path.dirname(os.path.abspath(__file__))+'/main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			print self.output_string.stdout.read()
			return self.output_string.stdout.read()
		elif self.lang_id == 1:
			self.source_code = source_code
			self.std_input = std_input
			self.file_name = file_name
			self.o = open('{}.c'.format(self.file_name),'w')
			self.o.write(self.source_code)
			self.o.close()
			subprocess.Popen(['gcc',os.path.abspath(self.file_name+'.c')],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			time.sleep(0.5)
			logging.debug(os.path.abspath('a.out'))
			self.output_string = subprocess.Popen([os.path.abspath('a.out')],stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
			if self.std_input:
				return self.output_string.communicate(str(std_input))[0]

			# check if process runs for prolonged time
			TIMEOUT = 1
			p = psutil.Process(self.output_string.pid)
			while 1:
    				if(time.time()-p.create_time())>TIMEOUT:
        				p.kill()
        				break
        			#raise RuntimeError('timeout')

			return self.output_string.stdout.read()

