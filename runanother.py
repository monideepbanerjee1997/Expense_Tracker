import os
e=input("Enter The NameOf the File You Want to Print with proper Extenion : ")
print('The source code of Another program is\n')
try:
	os.system(e)
except:
	print("File Not Found In The Directory.")

