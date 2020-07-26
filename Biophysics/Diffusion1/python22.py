#!/usr/bin/python2

# please don't use python 2, it is deprecated!
# use python 3 instead

import sys
old_stdout = sys.stdout
f= open("tcor_6000.dat","r")
if f.mode == "r"
	contents =f.read()
	f.close()
	
log_file = open("logfile.log","w")
sys.stdout = log_file
print contents
sys.stdout = old_stdout

log_file.close()
