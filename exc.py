def strToFloat(val):
    for i in val:
        if i not in '1234567890+-.':
            print('invalid')
            return None
    return float(val)

while True:
    # get input and store in x
    # check to see if x contains any invalid characters; not 0-9, only 1 decimal and only one - or + if it's at the beginning
    x = input("Enter a number")
    x = strToFloat(x)
    print(x)
    
    