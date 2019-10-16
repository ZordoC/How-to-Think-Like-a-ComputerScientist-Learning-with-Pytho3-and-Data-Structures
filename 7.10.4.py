'''''

Write a program that undoes the numbering of the previous exercise:
it should read a file with numbered lines and produce another file without line numbers

'''''

numbers['1','2','3','4','5','6','7','8','9','0']


with open ("5.4.6.1_without_col_5_numbered.py","r") as infile, open("5.4.6.1_without_col_5.py",'w') as output:


    for line in (infile):
        
        if line[:4] in numbers

            line = line[1::]
        
        print(line)

        output.write(line)

