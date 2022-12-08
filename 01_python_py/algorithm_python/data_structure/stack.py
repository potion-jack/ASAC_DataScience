from collections import deque
my_stack = deque()

def push(element):
    global my_stack
    my_stack.append(element)
    return None

def top():
    global my_stack
    try:
        print(my_stack[-1])
    except:
        print(-1)
    return None

def pop():
    global my_stack
    try:
        print(my_stack.pop())
    except:
        print(-1)
    return None

def empty():
    global my_stack
    if len(my_stack):
        print(0)
    else:
        print(1)
    return None

def size():
    global my_stack
    print(len(my_stack))
    return None

n = int(input())
li_command = list()
for __ in range(n):
    command = input().split()
    if len(command) == 2:
        _command = (command[0],int(command[1]))
        li_command.append(_command)
        continue
    li_command.append(command)

for command in li_command:
    if len(command) == 2:
        locals()[command[0]](command[1])
    else:
        locals()[command[0]]()
