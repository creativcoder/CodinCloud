import subprocess

# from subprocess import Popen, PIPE, STDOUT

# p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
# grep_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
# print(grep_stdout.decode())


subprocess.Popen(['gcc','main.c'])

f = open('file.txt','r')
proc = subprocess.Popen(['./a.out'],stdin=f,stdout=subprocess.PIPE)
print proc.communicate()
f.close()