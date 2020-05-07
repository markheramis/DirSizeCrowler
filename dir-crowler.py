#!/usr/bin/python

import sys, os, subprocess, math
args = sys.argv[1:]

#print 'Number of arguments:', len(args), 'arguments.'
#print 'Argument List:', str(args)

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def convert_size(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])

def scan_path(path = ''):
	size = 0
	try:
		if os.path.exists(path):
			if os.path.isfile(path):
				# deal with file
				size = os.stat(path).st_size
			elif os.path.isdir(path) :
				# deal with directory
				size = get_size(path)
			print "(" + convert_size(size) + ")", path
			return size
		else:
			print("path does not exists")
	except:
		print "Can't read path", path

for path in args:
	contents = os.listdir(path)
	total_size = 0
	for val in contents:
		val = path + "/" + val
		size = scan_path(val)
		if size :
			total_size += scan_path(val)
	print "Total Size:", convert_size(total_size)
