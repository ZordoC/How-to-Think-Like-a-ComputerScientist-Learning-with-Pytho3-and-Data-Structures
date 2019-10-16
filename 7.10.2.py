# Write a program that reads a file and prints only those lines that contain the substring Alice.

with open ('alice_in_wonderland.txt','r') as infile:
    for line in infile:
       if 'Alice' in line:
           print(line)