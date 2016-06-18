import subprocess
import time
import sys
import os
import psutil
import re
from template import code_templates

import logging	

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
				subprocess.Popen(['gcc',os.path.abspath('main'+'.c')],
					stdout=subprocess.PIPE,stderr=subprocess.PIPE)
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
			self.output_string = subprocess.Popen(['python',
				os.path.dirname(os.path.abspath(__file__))+'/{}.py'.format(self.file_name)],
				stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			print self.output_string.stdout.read()
			return self.output_string.stdout.read()

		elif self.lang_id == 1:
			self.PROCESS_IDENT = 'a.out'
			self.final_output = None
			self.source_code = source_code
			self.std_input = std_input.split('\n')
			self.file_name = file_name
			self.o = open('{}.c'.format(self.file_name),'w')
			self.o.write(self.source_code)
			self.o.close()
			self.proc = subprocess.Popen(['gcc',os.path.abspath(self.file_name+'.c')],
				stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			(self.stdin,self.stderr) = self.proc.communicate()
			if self.stderr != '':
				return "Error:\n" + self.stderr # early return if compilation error
			self.output = subprocess.Popen([os.path.abspath('a.out')],stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,stdin=subprocess.PIPE)

			if len(self.std_input) == 0:
				self.final_output = self.output.stdout.read()
			else:
				self.final_output = self.output.communicate(std_input)[0]
			return self.final_output
