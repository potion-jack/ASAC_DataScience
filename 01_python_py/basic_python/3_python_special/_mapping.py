# without mapping
a = [1.2, 2.5, 3.7, 4.6]
print(a)

for i in range(len(a)):
    a[i] = int(a[i])
print(a)

# by mapping
a = [1.2, 2.5, 3.7, 4.6]
print(a)

a = list(map(int,a))
print(a)

print("--- ---")
a = list(map(str,range(10)))
print(a)

print("--- ---")
# add 10 each
my_list = [1,2,3,4,5]
# by loop
result = []
for i in my_list:
    result.append(i+10)
print(result)

# by list_comprehension
result = []
result = [i+10 for i in my_list]
print(result)

# by mapping
result = []
def add_10(n):
    return n+10
result = list(map(add_10,my_list))
print(result)
