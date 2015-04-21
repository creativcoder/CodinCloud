import subprocess
import os
import time
cmd="ls"

out=subprocess.check_output(['date'],shell=True)
mem=subprocess.Popen(['date'],stdout=subprocess.PIPE)


print mem

