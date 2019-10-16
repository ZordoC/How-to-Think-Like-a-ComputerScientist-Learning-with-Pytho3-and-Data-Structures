#Write a program that reads a file and writes out a new file with the lines in reversed order
#(i.e.  the first line inthe old file becomes the last one in the new file.)

with open ('alice_in_wonderland.txt','r') as infile , open("alice_reversed.txt",'w') as outfile:

    reverse = infile.readlines()[::-1]

    for line in reverse:
        outfile.write(line)
        