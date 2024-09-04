print ("Print sums of current and previous number range(10)")
Previous_Num = 0

#Loop from 1 to 10
for i in range(1,11):
    x_sum = Previous_Num + i
    print ("Current Number",i, "Previous Number",Previous_Num, "Sum:",x_sum)

    Previous_Num = i
    
