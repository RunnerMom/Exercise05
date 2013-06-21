# ex15.py
# from LPTHW
#before exercise 5 GIT for hackbright

#imports the argv module
from sys import argv

#specifies 2 arguments in argv, names them script and filename
script, filename = argv

#takes a file <filename>,and turns it into a file object, assigning the object the name txt
txt = open(filename)

#prints the filename 
print "Here's your file %r:" % filename
#prints the entire contents of file object txt
print txt.read()
txt.close() 
print "Closed!"
#prints string
#print "Type the filename again:"
#asks for user input and assigns to file_again variable
#file_again = raw_input(">")

#creates new file object, file_again, and assigns it to the name txt_again
#txt_again = open(file_again)

#prints entire contents of file object txt_again
#print txt_again.read()