def fibonacci():
    box = [0,1]
    a = 0
    b = 1
    i = 0    
    for i in range(8):
        c = a+b
        a = b
        b = c
        box.append(c)
    return box
print(fibonacci()) 


# a = 0
# b = 1
# f[1] = a+b 
# f[2] =  b + f[1] 
# f[3] =  f[1] + f[2]


# def fibonacci(how_many_numbers):
#     my_list_of_numbers = [0, 1]
    
#     for i in range(how_many_numbers - 2):
#         next_number = my_list_of_numbers[-1] + my_list_of_numbers[-2]
#         my_list_of_numbers.append(next_number)
        
#     return my_list_of_numbers

# print(fibonacci(10))
