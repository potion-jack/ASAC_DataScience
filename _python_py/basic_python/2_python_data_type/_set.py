my_set = {1,2,1,1,3}
print(f"{my_set} type : {type(my_set)}")
try:
    print(f"{my_set[:-1]} slicing are available")
except:
    print("slicing aren't available")

my_set = {1,'1',1,2,2,2.0}
print(f"{my_set} type : {type(my_set)}")
print("different types are fine")

