#!/usr/bin/python2

# please don't use python 2, it is deprecated!
# use python 3 instead

import sys
old_stdout = sys.stdout
f = open("memprot_DPPC_310K_2.dat", "r") 
if f.mode == "r":
	contents =f.read()
	f.close()
	
out = open(g, "r")
if g.mode == "r":
	outcontents =g.read()
	g.close()

	
log_file = open("logfile.log","w")
sys.stdout = log_file
print "Input file \n"
print contents
print "\n"
print "Correlation time \n"
print tcor
print "\n"
print "Output File \n"
print outcontents
sys.stdout = old_stdout

log_file.close()
