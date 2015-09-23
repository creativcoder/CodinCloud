import subprocess
import psutil
import os
<<<<<<< HEAD
import time
TIMEOUT = 1
=======
TIMEOUT = 3
>>>>>>> 14f7f628486a4a9fd2e92e95a70f1249f6813f4c
subp = subprocess.Popen([os.path.abspath('a.out')])


p = psutil.Process(subp.pid)
while 1:
<<<<<<< HEAD
    if (time.time()-p.create_time())>TIMEOUT:
        p.kill()
        break
        #raise RuntimeError('timeout')
=======
    if (time.time()-p.create_time)>TIMEOUT:
        p.kill()
        raise RuntimeError('timeout')
>>>>>>> 14f7f628486a4a9fd2e92e95a70f1249f6813f4c
    time.sleep(5)
