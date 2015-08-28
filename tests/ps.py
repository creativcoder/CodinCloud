import subprocess
import psutil
import os
TIMEOUT = 3
subp = subprocess.Popen([os.path.abspath('a.out')])


p = psutil.Process(subp.pid)
while 1:
    if (time.time()-p.create_time)>TIMEOUT:
        p.kill()
        raise RuntimeError('timeout')
    time.sleep(5)
