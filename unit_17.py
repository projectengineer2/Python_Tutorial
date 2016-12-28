__author__ = 'Nguyen'
from os.path import exists
from_file = "C:\Users\Nguyen\PycharmProjects\Text\unit_15.txt"
to_file = "C:\Users\Nguyen\PycharmProjects\Text\unit_16.txt"
print "Copying from %s to %s" %(from_file,to_file)
in_file = open(from_file)
in_data = in_file.read()
print "the input file is %d bytes long" % len(in_data)
print "Does the output file exist? %r" % exists(to_file)
print "ready, hit Return to continue, CTRL-C to abort."
raw_input()
out_file = open(to_file,'w')
out_file.write(in_data)
print "Alright, all done"
out_file.close()
out_file = open(to_file).read()
print "Unit_16.txt:%s" % out_file
in_file.close()
