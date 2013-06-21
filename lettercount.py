#Exercise 5 in Hackbright Curriculum

#open a file named on the command line
from sys import argv

script, file_name = argv 
#open it in read mode

in_file = open(file_name) #create an object of type=file, named in_file
indata = in_file.read()

# print len(indata)

# try #1 this method would require 26 for loops - but it works!
# count_a = 0
# for i in range(len(indata)):
# 	if	ord(indata[i]) == 65 or ord(indata[i]) == 97:
# 		count_a = count_a +1
# print count_a

#for loop to loop through the alphabet, with a counter?, print how many times it occurred

# try # 2 with nested for loops:
for letter in range(65,91):
	count = 0
	for i in range(len(indata)):
		if	ord(indata[i]) == letter or ord(indata[i]) == letter+32:
				count = count +1
	print chr(letter), count

# This try did not work. Coming back to this one. 
# alphabet="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"

# list_alpha = alphabet.split(" ")


# for character_index in range(len(indata)):
# 	for alpha_index in range (26):
# 		if indata[character_index] == list_alpha[alpha_index] or indata[character_index] == list_alpha[alpha_index + 26]:
# 			alpha_index = alpha_index + 1
# 	print alpha_index

in_file.close()
print "we are done!!!!!!!!!!!!!"