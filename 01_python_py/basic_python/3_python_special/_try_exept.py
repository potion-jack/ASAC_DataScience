for i in range(10):
    try :
        print(100/i)
    except:
        print("something_wrong")
print("--- ---")
for i in range(10):
    try :
        print(100/i)
    except ZeroDivisionError as e :
        print(e)
