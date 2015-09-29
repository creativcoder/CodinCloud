import subprocess
from subprocess import PIPE,Popen
import psutil
import os
import time
TIMEOUT = 2

inputs = ['23','45','34','46']

subprocess.Popen(['gcc',os.path.abspath('main.c')])
time.sleep(0.4)
subp = subprocess.Popen([os.path.abspath('a.out')],stdin=PIPE,stdout=PIPE,stderr=PIPE)

for i in inputs:
	subp.stdin.write(i)
subp.stdin.write('\n')
print(subp.stdout.read())
print("communicate ran")
p = psutil.Process(subp.pid)
while 1:
    if (time.time()-p.create_time())>TIMEOUT:
        p.kill()
        print("This was an infinte loop")
        raise RuntimeError('timeout')
        break
        
