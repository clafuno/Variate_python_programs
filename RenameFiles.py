# Udacity course - PROGRAMMING FOUNDATIONS WITH PYTHON
# Programm 1.1: Rename files
# Rename esch photo in the folder, deleting the numbers

import os

def rename_files():
	# 1st get files names from a folder
	file_list = os.listdir(os.path.expanduser('/Users/clara/Downloads/prank'))
	#print(file_list)
	#saved_path = os.getcwd()
	os.chdir(os.path.expanduser('/Users/clara/Downloads/prank'))
	# 2nd for each file, rename file name
	for file_name in file_list:
		#os.rename(old_name, new_name)
		#string.translate(s, table[, deletechars])
		os.rename(file_name, file_name.translate(None,"0123456789"))


rename_files()


