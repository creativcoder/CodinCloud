import subprocess

subprocess.Popen(['gcc','main.c'])

f = open('file.txt','r')
proc = subprocess.Popen(['./a.out'],stdin=f,stdout=subprocess.PIPE)
print proc.communicate()
f.close()