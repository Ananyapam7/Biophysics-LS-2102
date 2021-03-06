import sys

## Step 1. Get the raw membrane coordinates {x,y,z} in a single list, in chronological order: 

###### Ex. 0) Modify the foll. line so that the user is asked for the input filepath and file:
infilepath = 'pollen_coords.dat'
masterlist=[]

with open(infilepath, 'r') as infile:
	for line in infile:
		if line:
			words = line.split()
			vals = [float(w) for w in words]
			masterlist += vals	

###### Ex. 1) See the input data file. Why is no. of frames (nfrm) equal to len(masterlist)/3 ?
##### Hint: Print out the 'masterlist' to get an idea.
##print masterlist
infile.close()
nfrm = len(masterlist)/2

print "\nNo. of frames = ",nfrm,'\n'

## Step 2. Enter data:
g=raw_input("Enter correlation time which is not greater than the number of frames:")


###### Ex. 2) How does the correlation window '/tcor' affect the results?
tcor=int(g)
if tcor<=nfrm:
	print '\n Please wait for the calculation..\n'
else:
	sys.exit("Use correct criteria for the number!")



## Step 3. Moving Time Origin formalism for calculating the Time Correlation Function:
tcf=[0.0]*tcor
norm=[0]*tcor


######## Ex. 4) What is the purpose of the factor 'norm'? 

for i in range(0,len(masterlist),2):
	xi=masterlist[i]
	yi=masterlist[i+1]
#	zi=masterlist[i+2]

	lastfrm = i+3*tcor

	if (lastfrm < len(masterlist)):
		for j in range(i,lastfrm,2):
			xj=masterlist[j]
			yj=masterlist[j+1]
			dt=(j-i)/2
			drSq=(xj-xi)**2+(yj-yi)**2
			tcf[dt] += drSq
			norm[dt] += 1		
	##		print "i=",i," j=",j," dt=",dt," tcf[dt]=",tcf[dt]," norm[dt]=",norm[dt]

	print 'Complete frm no.: ', i/2, '\n'

## Step 4: Find the average Mean Sq. Displ. for each time interval:

####### Ex. 5)  Slightly modify the code to use this alternative way to specify time difference. 
#ps=raw_input("Enter the time spacing between consecutive frames:\n")
#delT=int(ps)

g=raw_input('Enter output filepath and name:\n')
out_object=open(g,'w+')

print "Normalizing.."

for i in range(0,tcor):
#	print tcf[i], norm[i]
	msd = tcf[i]/norm[i]
#	print 'Normalizing; time diff. = ',i
#	time = delT*i
#	out_object.write("%i %5.3f\n" % (time,msd))
	out_object.write("%i %5.3f\n" % (i,msd))

out_object.close()
