# Write a program that computes the sum of the squares of the numbers in the
# listnumbers. For example a callwith,numbers = [2, 3, 4]
# should print 4+9+16 which is 29.



numbers = [2,3,4]

squares =[i**2 for i in numbers ]

print(sum(squares))

    