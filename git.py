import sys
import os
name = ""
if sys.argv[2]:
	name = sys.argv[2]
if "/" in sys.argv[1]:
	os.system("git clone http://github.com/"+sys.argv[1]+" "+name)
else:
	os.system("git clone http://github.com/"+sys.argv[1]+"/"+sys.argv[1]+".github.io "+sys.argv[2])
