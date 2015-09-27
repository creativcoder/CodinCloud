import subprocess
import psutil
import os
import time
TIMEOUT = 1
subp = subprocess.Popen([os.path.abspath('a.out')])


p = psutil.Process(subp.pid)
while 1:
    if (time.time()-p.create_time())>TIMEOUT:
        p.kill()
        break
        #raise RuntimeError('timeout')
    time.sleep(5)
