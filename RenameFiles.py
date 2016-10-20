# Udacity course - PROGRAMMING FOUNDATIONS WITH PYTHON
# Programm 1.1: Rename files

def rename_files():
	# 1st get files names from a folder
	file_list = os.listdir("/Users/clara/Descargas/prank")
	print(file_list)
	# 2nd for each file, rename file name