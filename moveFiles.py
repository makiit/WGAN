import os
import shutil
path = "/home/mak/Desktop/Stroboscopy"
dest = "/home/mak/Desktop/Stroboscopy/AllImages/"
c = 0

for r,d,f in os.walk(path):
	for file in f:
		full_file_name = os.path.join(r, file)
		# print full_file_name
		if (os.path.isfile(full_file_name)):
			c+=1
			d = dest+str(c)+".png"
			shutil.copy(full_file_name,d)

print c," Files"