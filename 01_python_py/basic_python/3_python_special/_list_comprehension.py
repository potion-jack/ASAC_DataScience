my_tuple = (i for i in range(1,10,2))
my_list = [i for i in range(1,10,2)]
my_set = {i for i in range(1,10,2)}
my_dict = {i:j for i,j in zip(range(1,10,2),range(10,20,2))}

print(f"{my_tuple} type : {type(my_tuple)}")
print(f"{my_list} type : {type(my_list)}")
print(f"{my_set} type : {type(my_set)}")
print(f"{my_dict} type : {type(my_dict)}")


