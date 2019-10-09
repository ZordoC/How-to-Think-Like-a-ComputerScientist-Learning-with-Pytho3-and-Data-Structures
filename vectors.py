

def add_vectors(vector1,vector2):
    """""
        Adds two vectors of the same size together, element wise 
        
        :input(vector1): list
        :input(vector2): list
        :output(vec_s): list

    """""
    if len(vector1) != len(vector2):
        return None

    else:

        vec_s = []
        size = len(vector1) 
        
        # for v in range(size):
        #     vec_s.append(vector1[v]+vector2[v])

        vec_s = [vector1[i] + vector2[i] for i in range(size)]


        return vec_s
        


def scalar_mult(scalar,vector):
    '''''
    Element wise multiplication with scalar value 
    
    :input(scalar):  int,float 
    :input(vector):  vector  
    :output:  list 
    '''''

    vec_mult = [scalar* i for i in vector]

    return vec_mult
    

def dot_product(vector1,vector2):
    '''''
    Dot product between two vectors

    :input(vector1): list
    :input(vector2): list
    :output(): scalar
    '''''
    if len(vector1) != len(vector2):
        return None

    size = len(vector1)
    vect_dot = [vector1[i]*vector2[i] for i in range(size)] # Does the multiplication but not the adding!

    return sum(vect_dot)    # Sums the values of the mults 
    



# Tests

print("--"*10)

print(add_vectors([1,1],[1,1]))
print(add_vectors([1,2],[1,4]))
print(add_vectors([1,2,1],[1,4,3]))

print("--"*10)

print(scalar_mult(5,[1,2]))
print(scalar_mult(3,[1,0,-1]))
print(scalar_mult(7,[3,0,5,11,2]))

print("--"*10)

print(dot_product([1,1],[1,1]))
print(dot_product([1,2],[1,4]))
print(dot_product([1,2,1],[1,4,3]))

print("--"*10)
