__author__ = 'Nguyen'
filename = "C:\Users\Nguyen\PycharmProjects\Text\unit_16.txt"
print "We're going to erase %r" % filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename,'w')
print "Truncating the file. Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print " And finally, we close it."
target.close()
target = open(filename,'r')
print "I'm reading the file..."
print "Hole file \n:%s" %target.read()
target.close()
target = open(filename,'r')
print "I'm reading the first line..."
print "The first line:%s" %target.readline()
target.close()

