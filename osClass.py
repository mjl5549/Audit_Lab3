import os
import sys
import subprocess, platform

###################################
# Name: Oluwadunsola (Sola) Alabi # 
# Date: 3/5/18			  #
# File: osClass.py		  #
# Group: 1		          #
###################################

#Parses a file and returns a lists of its contets
def parseFile( file ):
        file = open ( file)
        lst = []
        for line in file :
                line = line.strip()
                lst.append(line)
        return lst

#Tries to ping the ip given. If an exception is raised (IP is down) then returns false else returns the output
def pingTest( ipaddr ):
	try:
		print('Testing IP Address: ' + ipaddr + ' ...\n')
		output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', ipaddr), shell=True)
	except Exception, e:
		return False
	return output

def main():
        lst = parseFile(sys.argv[1])
       	final = [] # IPDown = 0, Win = 1,  Unix = 2, BSD = 3
	for item in lst:
		output = pingTest(item)
		if (output != False):
			s = output.split(' ')[11][4:]
			s = int(s)
			if (s == 64):
				final.append(2)
			if (s == 255 ):
				final.append(3)
			if (s == 128 ):
				final.append(1)
		else :
			final.append(0)
	print('Results: \n')
	for i in range(0,len(final)):
		if (final[i] == 0):
			print('Ip address: ' + lst[i] + ' is down' + '\n')
			continue
		if (final[i] == 1):
			print('Ip address: ' + lst[i] + ' is up. OS: Windows \n')
			continue
		else:
			print('Ip address: ' + lst[i] + ' is up. OS: Unix \n')
			continue
	return 0

if __name__ == "__main__":
    	main()
