def divided_difference(x_n, y_n):
    res = [] #Create the result array 
    a_k = y_n[0] #This is the first coefficient

    for i in range(1,len(x_n)):
        res.append(a_k)

        a_k = y_n[i] - a_k
        a_k *= 1 / (x_n[i] - x_n[i-1])
    
    return res

#Test the coefficient function 
x = [0,1,-1,2,-2]
y = [-5,-3,-15,39,-9]
print(divided_difference(x, y))