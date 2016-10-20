# Udacity course - PROGRAMMING FOUNDATIONS WITH PYTHON
# Programm 1.1: Rename files
import os


def rename_files():
	# 1st get files names from a folder
	file_list = os.listdir(os.path.expanduser('/Users/clara/Downloads/prank'))
	print(file_list)
	# 2nd for each file, rename file name
	for file_name in file_list:
		#os.rename(old_name, new_name)
		os.rename(file_name,)


rename_files()
