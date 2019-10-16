'''''

Write a program that reads a text file and produces an output file which is a copy of the file, 
except the first five columns of each line contain a four digit line number, followed by a space. 
Start numbering the first line inthe output file at 1. Ensure that every line number is formatted
 to the same width in the output file. Use one ofyour Python programs as test data for this exercise:
  your output should be a printed and numbered listing of thePython program.

'''''


with open ("5.4.6.1.py","r") as infile, open("5.4.6.1_without_col_5_numbered.py",'w') as output:
    
    for i,line in enumerate(infile):
        line = str(i) + line[0 : 5 : ] + line[5 + 1  :]
        print(line)

        output.write(line)
        


