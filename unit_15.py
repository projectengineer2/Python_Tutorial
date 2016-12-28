__author__ = 'Nguyen'
filename = "C:\Users\Nguyen\PycharmProjects\Text\unit_15.txt"
txt = open(filename)
print "Here're your file %r" %filename
print txt.read()
print "Type the file name again:"
file_again = raw_input("> ")
txt_again = open (file_again)
print txt_again.read()
