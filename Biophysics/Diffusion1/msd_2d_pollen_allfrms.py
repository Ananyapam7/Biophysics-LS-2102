import sys

## Step 1. Get the raw coordinates {x,y} in a single list, in chronological order: 
infilepath = 'pollen_coords.dat'
masterlist=[]

with open(infilepath, 'r') as infile:
	for line in infile:
		if line:
			words = line.split()
			vals = [float(w) for w in words]
			del vals[0]
			masterlist += vals	


#print masterlist
infile.close()
nfrm = len(masterlist)/2
##print nfrm,  masterlist[nfrm-1],  masterlist[ntime-2] 
print "\nNo. of frames = ",nfrm,'\n'

## Step 2. Enter data:
g=raw_input("Enter correlation time which is not greater than the number of frames:")
tcor=int(g)
if tcor<=nfrm:
	print '\n Please wait for the calculation..\n'
else:
	sys.exit("Use correct criteria for the number!")



## Step 3. Moving Time Origin formalism for calculating the Time Correlation Function:
tcf=[0.0]*nfrm
norm=[0]*nfrm

for i in range(0,len(masterlist),2):
	xi=masterlist[i]
	yi=masterlist[i+1]

	for j in range(i,len(masterlist),2):
		xj=masterlist[j]
		yj=masterlist[j+1]
		dt=(j-i)/2
		drSq=(xj-xi)**2+(yj-yi)**2
		tcf[dt] += drSq
		norm[dt] += 1		
	##	print "i=",i," j=",j," dt=",dt," tcf[dt]=",tcf[dt]," norm[dt]=",norm[dt]

	print 'Complete frm ', i/2, '\n'

## Step 4: Find the average Mean Sq. Displ. for each time interval:

#ps=raw_input("Enter the spacing between consecutive frames in picoseconds:")
g=raw_input('Enter output filepath and name:\n')
out_object=open(g,'w+')

for i in range(0,tcor):
#	print tcf[i], norm[i]
	msd = tcf[i]/norm[i]
##	print 'Normalizing; time diff. = ',i
	out_object.write("%i %5.3f\n" % (i,msd))


out_object.close()
