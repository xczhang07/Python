'''
Created By: Xiaochong Zhang
Time: 2018/04/23
Demo file object processing operation

the code in this file:
1. create a file in current directory (will overwrite if the file exists)
2. read the whole file and return the content as string
3. read the file line by line
'''

def create_file_in_current_directory(file_name, context):
	'''created file in current directory with the given filename
	   , if the file exist, will overwrite the file'''
	fd = open(file_name, 'wt')
	fd.write(context)
	fd.close()

def read_file_in_current_directory(file_name):
	'''read file in current directory with the given filename
	   return value will be a string which represent the content of the file
	'''
	fd = open(file_name, 'rt')
	content = fd.read()
	fd.close()
	return content

def read_file_line_by_line_in_current_directory(file_name):
	'''read the file in current directory with the given filename line by line'''
	fd = open(file_name, "rt")
	while True:
		line = fd.readline()
		if not line:
			break
		else:
			print line
	fd.close()

def close_file_automatically(file_name):
	'''open a file with key word "with", the keyword will close file automatically instead of 
	calling the close() function'''
	with open(file_name, "at") as fd:
		content = "open file using 'with' keyword"
		fd.write(content)
	with open(file_name, "rt") as fd:
		content = fd.read()
		print content

if __name__ == "__main__":
	file_name1 = "file1"
	context1 = "Hello world, Python, My major is computer engineer and I like programming.\n" \
		   "C++ is my favourite programming language, what is yours? "
	create_file_in_current_directory(file_name1, context1)
	file_content = read_file_in_current_directory(file_name1)
	print "length of the content file is: %d" % len(file_content)
	print "content of the file is: %s" % file_content
	
	print "========testing read file line by line========"
	read_file_line_by_line_in_current_directory(file_name1)
	
	print "========testing with keyword========"
	close_file_automatically(file_name1)
