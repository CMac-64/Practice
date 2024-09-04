def M_orS (Number1,Number2):
    Product = Number1 * Number2
    if Product <= 1000:
        return Product
    else:
        return Number1 + Number2

# First Calc
result = M_orS(20,30)
print ("The result is ", result)

# Second Calc
result = M_orS(40,50)
print ("the result is ", result)




