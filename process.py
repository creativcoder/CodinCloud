import subprocess
import os
import time
cmd="ls"

out=subprocess.check_output(['date'],shell=True)
try:
	mem=subprocess.Popen(['rm','main'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	print mem.stderr.read()
except OSError:
	print "Could not identify command"




